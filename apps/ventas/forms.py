from django.db.models.fields import DateField
from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget
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
            'prospecto'
        ]

        widgets = {
            'fecha_venta': SelectDateWidget(),
        }