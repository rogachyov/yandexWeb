import csv

from flask import Flask, render_template, redirect, url_for
from flask_restful import Api

from flask_login import LoginManager, login_manager, login_user, login_required, logout_user, current_user


from data import db_session, users_resources
from data.users import User
from data.cities import City

from forms.user import RegisterForm, LoginForm, EditForm

from wether_api import call

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/")
def index():
    wether = call(52.52, 13.41)
    return 'Hello World!'
    # return render_template('index.html', wether=wether)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    print('a')
    form = RegisterForm()
    if form.validate_on_submit() and form.password.data == form.confirm_password.data:
        print('b')
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            print('c')
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            username=form.username.data,
            email=form.email.data,
        )
        print('d')
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    if form.password.data != form.confirm_password.data:
        return render_template('register.html', title='Регистрация',
                               form=form, message='Пароли не соответствуют')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


def main():
    db_session.global_init("db/weather.db")

    # db_sess = db_session.create_session()
    #
    # with open('db/worldcities_our.csv', 'r', encoding='utf-8') as csvfile:
    #     reader = csv.reader(csvfile, delimiter=',')
    #     next(reader)
    #     for row in reader:
    #         city = City()
    #         city.city, city.lat, city.lng = row
    #         db_sess.add(city)
    #     db_sess.commit()

    api.add_resource(users_resources.UsersListResource, '/api/v2/users')

    api.add_resource(users_resources.UsersResource, '/api/v2/users/<int:id>')

    app.run()


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


if __name__ == '__main__':
    main()