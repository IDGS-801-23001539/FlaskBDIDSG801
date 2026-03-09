from wtforms import Form, RadioField
from wtforms import StringField, IntegerField, PasswordField, FloatField,RadioField,SelectField, validators
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


class UserForm(Form):
    matricula=IntegerField("Matricula",
                    [validators.number_range(min=1, max=30000000,message="valor no valido")])
    nombre=StringField("Nombre",[
        validators.DataRequired(message="El nombre es requerido"),
        validators.length(min=4,max=20,message="requiere min =4 y max = 20")
    ])
    apellidos=StringField("Apellidos",[
        validators.DataRequired(message="Los apellidos son requeridos")
    ])
    especialidad=StringField("Especialidad",[
        validators.DataRequired(message="La especialidad es requerida")
    ])
    email=EmailField("Correo",[
        validators.DataRequired(message="El correo es requerido"),
        validators.Email(message="Ingrese un correo valido")
    ])

class UserForm3(Form):
    id=IntegerField("ID",[validators.number_range(min=1, max=120, message='Valor no valido')])
    nombre=StringField("Nombre",[
        validators.DataRequired(message="El nombre es requerido"),
        validators.length(min=3, max=50,message="Requiere minimo 3 y maximo 50 caracteres")
    ])
    descripcion=StringField("Descripcion",[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=50,message="Requiere minimo 3 y maximo 50 caracteres")
    ])
    id_maestro=  SelectField("Maestro", coerce=int)

class InscripcionesForm(Form):
    id=IntegerField("ID",[validators.number_range(min=1, max=120, message='Valor no valido')])
    alumno_id = SelectField("Alumno",
        coerce=int,
        validators=[validators.DataRequired(message="Seleccione un alumno")]
    )

    curso_id = SelectField("Curso",
        coerce=int,
        validators=[validators.DataRequired(message="Seleccione un curso") ]
    )