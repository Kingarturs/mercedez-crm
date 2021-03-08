from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Empleado


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Empleado
        fields = ('username', 'nombre', 'apellido', 'telefono', 'email', 'status', 'tipo')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Empleado
        fields = ('username', 'nombre', 'apellido', 'telefono', 'email', 'status', 'tipo')