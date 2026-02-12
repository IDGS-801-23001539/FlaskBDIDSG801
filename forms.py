from wtforms import Form, RadioField
from wtforms import StringField, IntegerField, PasswordField, FloatField,RadioField, validators
from wtforms import EmailField
from wtforms import validators

class UserForm2(Form):
    id=IntegerField('id',
        [validators.number_range(min=1, max=20. message='valor no valido')
    ])
    nombre=StringField('nombre',[
        validators.DataRequired(message='El nombre es requerido'),
        validators.length(min=4, max=20, message='requiere min=4 max=20')
    ])
     apaterno=StringField('apaterno',[
        validators.DataRequired(message='El apellido es requerido'),
        validators.length( message='requiere min=4 max=20')
    ])
     email=EmailField('correo',[
        validators.DataRequired(message='El correo es requerido'),
        validators.Email(message='Ingrese un correo Valido')
    ])