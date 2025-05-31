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
    
class UsuarioPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre_usuario', 'correo', 'telefono',
            'nombres', 'apellidos'
        ]
        labels = {
            'nombre_usuario': 'Nombre de usuario',
            'correo': 'Correo electrónico',
            'telefono': 'Teléfono celular',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
        }
        widgets = {
            'nombre_usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
        }