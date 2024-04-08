from flask import Flask, render_template, redirect
from flask_restful import Api

from flask_login import LoginManager, login_manager, login_user, login_required, logout_user, current_user


from data import db_session, users_resources, cities_resources
from data.users import User
from data.cities import City

from forms.user import RegisterForm, LoginForm

from wether_api import call

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/")
def index():

    return 'Hello World!'


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    print('a')
    form = RegisterForm()
    if form.validate_on_submit():
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

    # city = City()
    # city.city = 'Omsk'
    #
    # db_sess.add(city)
    # db_sess.commit()
    #
    # user = User()
    # user.username = "semen"
    # user.email = 'semen@gmail.com'
    # user.set_password(password="hdgfvjfsh")
    #
    # db_sess.add(user)
    # db_sess.commit()

    api.add_resource(users_resources.UsersListResource, '/api/v2/users')
    api.add_resource(cities_resources.CitiesListResource, '/api/v2/cities')

    api.add_resource(users_resources.UsersResource, '/api/v2/users/<int:id>')
    api.add_resource(cities_resources.CitiesResource, '/api/v2/cities/<int:id>')

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