from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class RegisterForm(FlaskForm):
    username = StringField(label='Nombre: ', validators=[Length(min=4, max=12), DataRequired()])
    email = StringField(label='Email: ', validators=[Email(), DataRequired()])
    password1 = PasswordField(label = 'Contraseña: ', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label = 'Confirmar contraseña: ', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Enviar')