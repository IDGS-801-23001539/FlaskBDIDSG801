from wtforms import Form, RadioField
from wtforms import StringField, IntegerField, PasswordField, FloatField,RadioField, validators
from wtforms import EmailField
from wtforms import validators

class UserForm2(Form):
    id=IntegerField('ID',[
       validators.NumberRange(min=1, max=20, message='valor no valido')
    ])
    nombre=StringField('Nombre',[
        validators.DataRequired(message='El nombre es requerido'),
        validators.length(min=4, max=20, message='requiere min=4 max=20')
    ])
    apellidos=StringField('Apellidos',[
        validators.DataRequired(message='Los  apellidos es requerido'),
        validators.length(min=4, max=20, message='requiere min=4 max=20')
    ])
    email=EmailField('Correo',[
        validators.DataRequired(message='El correo es requerido'),
        validators.Email(message='Ingrese un correo Valido')
    ])
    telefono=StringField('Telefono',[
        validators.DataRequired(message='El telefono es requerido'),
        validators.length(min=10, max=10, message='requiere minimo 10 numeros')
    ])