from django.forms import (
    Form,
    CharField,
    PasswordInput,
    EmailInput,
    TextInput
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class Registro(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['password1'].widget.attrs = { 'class':'form-control', 'placeholder':'password' }
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].widget.attrs = { 'class':'form-control', 'placeholder':'password(Confirmar)' }
        self.fields['password2'].label = 'Contraseña(CF)'
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email'
        ]
        widgets = {
            'username': TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Usuario'
                }
            ),
            'first_name': TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre'
                }
            ),
            'last_name': TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Apellido'
                }
            ),
            'email': EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'email@gmail.com'
                }
            )
        }
        
        labels = {
            'username':'Usuario',
            'first_name': 'Nombre',
            'last_name' : 'Apellido',
            'email' : 'Correo',
            'password1' : 'Contraseña',
            'password2' : 'Contraseña(CF)',

        }

class FormularioIniciar(Form):
    usuario = CharField(
        required = True,
        label = 'Ingrese su usuario',
        widget = TextInput(
            attrs = {
                'class':'form-control rounded-5 shadow text-center',
                'placeholder':'Usuario'
            }
        )
    )
    contrasena = CharField(
        required = True,
        min_length = 4,
        max_length = 16,
        label = 'Ingrese su contraseña',
        widget = PasswordInput(
            attrs = {
                'class':'form-control rounded-5 shadow text-center',
                'placeholder':'Contraseña'
            }
        )
    )