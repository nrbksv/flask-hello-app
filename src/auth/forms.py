from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import required, length
from wtforms.widgets import PasswordInput


class LoginForm(FlaskForm):
    login = StringField(label='Логин', validators=(required(), length(min=3, max=150)))
    password = StringField(label='Пароль', widget=PasswordInput(), validators=(required(), length(min=3, max=150)))
