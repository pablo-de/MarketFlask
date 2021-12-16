from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.simple import SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='Nombre: ')
    email = StringField(label='Email: ')
    password1 = PasswordField(label = 'Contraseña: ')
    password2 = PasswordField(label = 'Confirmar contraseña: ')
    submit = SubmitField(label='Enviar')