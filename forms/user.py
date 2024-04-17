from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, EmailField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired

import sqlite3

from data import db_session
from data.cities import City


class RegisterForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()],
                           render_kw={"class": "user_name_form"})
    email = StringField(' Email', validators=[DataRequired()], render_kw={"class": "email_form"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-password_form"})
    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired()],
                                     render_kw={"class": "confirm_password_form"})
    con = sqlite3.connect("db/weather.db")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM cities""").fetchall()
    list = SelectField('Город', validators=[DataRequired()], choices=[(city[0], city[1]) for city in result])
    con.close()

    submit = SubmitField('Зарегистрироватся', render_kw={"class": "confirm_btn"})


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти', render_kw={"class": "confirm_btn"})
