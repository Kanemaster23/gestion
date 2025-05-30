from django import forms
from .models import Usuario

class UsuarioRegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre_usuario', 'correo', 'contraseña',
            'telefono', 'nombres', 'apellidos'
        ]
        widgets = {
            'contraseña': forms.PasswordInput(),
        }

    def clean_contraseña(self):
        contraseña = self.cleaned_data.get('contraseña')
        # Puedes agregar validaciones aquí si deseas
        return contraseña