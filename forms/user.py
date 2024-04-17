from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, EmailField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired

from data import db_session
from data.cities import City


class RegisterForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()],
                           render_kw={"class": "user_name_form"})
    email = StringField(' Email', validators=[DataRequired()], render_kw={"class": "email_form"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-password_form"})
    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired()],
                                     render_kw={"class": "confirm_password_form"})
    session = db_session.create_session()
    cities = session.query(City).all()
    list = SelectField('Город', validators=[DataRequired()], choices=[(city.id, city.city) for city in cities])

    submit = SubmitField('Зарегистрироватся', render_kw={"class": "confirm_btn"})


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти', render_kw={"class": "confirm_btn"})


class EditForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')