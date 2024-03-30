from flask import Flask, render_template, redirect
from flask_restful import Api

from data import db_session, users_resources, cities_resources
from data.users import User
from data.cities import City

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    return 'Hello World!'


# @app.route('/register', methods=['GET', 'POST'])
# def reqister():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         if form.password.data != form.password_again.data:
#             return render_template('register.html', title='Регистрация',
#                                    form=form,
#                                    message="Пароли не совпадают")
#         db_sess = db_session.create_session()
#         if db_sess.query(User).filter(User.email == form.email.data).first():
#             return render_template('register.html', title='Регистрация',
#                                    form=form,
#                                    message="Такой пользователь уже есть")
#         user = User(
#             name=form.name.data,
#             email=form.email.data,
#             about=form.about.data
#         )
#         user.set_password(form.password.data)
#         db_sess.add(user)
#         db_sess.commit()
#         return redirect('/login')
#     return render_template('register.html', title='Регистрация', form=form)


# @app.route('/login')
# def login():
#     return 'Все записано!'

def main():
    db_session.global_init("db/weather.db")

    db_sess = db_session.create_session()

    user = User()
    user.username = "semen"
    user.email = 'semen@gmail.com'
    user.password = User.set_password(user, password="hdgfvjfsh")

    db_sess.add(user)
    db_sess.commit()

    city = City()
    city.city = 'Omsk'

    db_sess.add(city)
    db_sess.commit()

    api.add_resource(users_resources.UsersListResource, '/api/v2/users')
    api.add_resource(cities_resources.CitiesListResource, '/api/v2/cities')

    api.add_resource(users_resources.UsersResource, '/api/v2/users/<int:id>')
    api.add_resource(cities_resources.CitiesResource, '/api/v2/cities/<int:id>')

    app.run()


if __name__ == '__main__':
    main()