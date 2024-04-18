import csv

from flask import Flask, render_template, redirect
from flask_restful import Api

from flask_login import LoginManager, login_manager, login_user, login_required, logout_user, current_user


from data import db_session, users_resources
from data.users import User
from data.cities import City

from forms.user import RegisterForm, LoginForm

from wether_api import call

from datetime import datetime


app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/")
def index():
    if not current_user.is_authenticated:
        return redirect('/register')
    db_sess = db_session.create_session()
    city = db_sess.query(City).filter(City.id == current_user.city_id).first()
    all_weather = call(city.lat, city.lng)
    print(all_weather)
    time_UTC = datetime.utcnow().time().hour
    print(time_UTC)
    direction = float(all_weather['wind_direction_10m'][time_UTC])
    if 337.5 <= direction <= 380 or 0 <= direction <= 22.5:
        direction = 'С'
    elif 22.5 <= direction <= 67.5:
        direction = 'СВ'
    elif 67.5 <= direction <= 112.5:
        direction = 'В'
    elif 112.5 <= direction <= 157.5:
        direction = 'ЮВ'
    elif 157.5 <= direction <= 202.5:
        direction = 'Ю'
    elif 202.5 <= direction <= 247.5:
        direction = 'ЮЗ'
    elif 247.5 <= direction <= 292.5:
        direction = 'З'
    elif 292.5 <= direction <= 337.5:
        direction = 'СЗ'
    else:
        direction = 'С'
    weather = {'temperature_2m': round(float(all_weather['temperature_2m'][time_UTC]), 1),
               'weather_code': int(all_weather['weather_code'][time_UTC]),
               'wind_speed_10m': str(round(float(all_weather['wind_speed_10m'][time_UTC]), 2)) + 'м/с',
               'wind_direction_10m': direction}
    # return weather
    return render_template('index.html', weather=weather)


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
            city_id=form.list.data
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

    db_sess = db_session.create_session()

    with open('db/worldcities_our.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for row in reader:
            city = City()
            city.city, city.lat, city.lng = row
            db_sess.add(city)
        db_sess.commit()

    api.add_resource(users_resources.UsersListResource, '/api/v2/users')

    api.add_resource(users_resources.UsersResource, '/api/v2/users/<int:id>')

    app.run(port='8080')


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