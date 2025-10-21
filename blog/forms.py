from django import forms

from blog.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'contraseña', 'apellido', 'email']
        widgets = {
            'contraseña': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs= {'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
        }
class LoginForm(forms.Form):
    """Formulario para iniciar sesión."""
    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'})
    )
    contraseña = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )


class BusquedaPostForm(forms.Form):
    """Formulario para buscar publicaciones por título o categoría."""
    consulta = forms.CharField(
        label='Buscar Post',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por título o categoría...'
        })
    )
