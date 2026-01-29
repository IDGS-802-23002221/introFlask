# crear formularios a traves de librerias que descargamos 

from wtforms import Form 
from wtforms import StringField, IntegerField, PasswordField
from wtforms import EmailField
from wtforms import validators 

class UserForm(Form):
    # lo que aparece en el html 
    matricula = IntegerField("Matricula", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=100, max=1000, message="ingrese un valor valido")
    ])

    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"), 
        validators.length(min=3, max=10, message="Ingrese un nombre valido")    
    ])
    
    apaterno = StringField("aPaterno",[
        validators.DataRequired(message="El campo es requerido")
    ])
    amaterno = StringField("aMaterno", [
        validators.DataRequired(message="El campo es requerido")
    ])
    correo = EmailField("Correo", [
        validators.Email(message="Ingrese un correo valido")
    ])

