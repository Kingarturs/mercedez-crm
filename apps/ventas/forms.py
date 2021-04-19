from django.forms import ModelForm
from .models import Venta

class nuevaVentaForm(ModelForm):
    class Meta:
        model = Venta
        fields = [
            'fecha_venta',
            'tipo_venta',
            'producto',
            'sucursal',
            'empleado',
            'cliente'
        ]