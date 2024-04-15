from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, EmailField, SubmitField, BooleanField, FieldList
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired()])
    # list = FieldList('city', validators=[DataRequired()])
    # city = StringField('city', validators=[DataRequired()])

    submit = SubmitField('Зарегистрироватся')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class EditForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')