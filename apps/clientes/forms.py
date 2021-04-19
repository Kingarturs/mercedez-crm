from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import Empleado


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Empleado
        fields = ('username', 'nombre', 'apellido', 'telefono', 'email', 'status', 'tipo')
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Empleado
        fields = ('username', 'nombre', 'apellido', 'telefono', 'email', 'status', 'tipo')
    
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class CustomEmpleadoCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Empleado
        fields = ('username', 'nombre', 'apellido', 'telefono', 'email')
    
    def __init__(self, *args, **kwargs):
        super(CustomEmpleadoCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    