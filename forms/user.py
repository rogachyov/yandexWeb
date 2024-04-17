from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, EmailField, SubmitField, BooleanField, FieldList
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()],
                           render_kw={"class": "user_name_form"})
    email = StringField(' Email', validators=[DataRequired()], render_kw={"class": "email_form"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-password_form"})
    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired()],
                                     render_kw={"class": "confirm_password_form"})
    list = FieldList('city', validators=[DataRequired()])

    submit = SubmitField('Зарегистрироватся', render_kw={"class": "confirm_btn"})


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти', render_kw={"class": "confirm_btn"})


class EditForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')