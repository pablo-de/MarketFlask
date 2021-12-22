from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError(
                'Ya existe un usuario con ese nombre, intente con otro')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(
            email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError(
                'Ya existe un usuario registrado con esa direccion de correo.')

    username = StringField(label='Nombre: ',
                           validators=[Length(min=4, max=12),
                                       DataRequired()])

    email_address = StringField(label='Email: ',
                                validators=[Email(), DataRequired()])

    password1 = PasswordField(label='Contraseña: ',
                              validators=[Length(min=6),
                                          DataRequired()])
    password2 = PasswordField(
        label='Confirmar contraseña: ',
        validators=[EqualTo('password1'), DataRequired()])

    submit = SubmitField(label='Crear cuenta')
    
    
class LoginForm(FlaskForm):
    username = StringField(label='Usuario', validators=[DataRequired()])
    password = PasswordField(label='Contraseña', validators=[DataRequired()])
    submit = SubmitField(label='Ingresar')