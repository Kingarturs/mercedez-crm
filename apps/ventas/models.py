from apps.productos.models import Producto
from apps.sucursales.models import Sucursal
from apps.clientes.models import Cliente
from django.db import models
from datetime import date
from django.contrib.auth import get_user_model

Empleado = get_user_model()

# Create your models here.
class Venta(models.Model):
    VENTA_CHOICES = (
        ('FI', 'Financiado'),
        ('CR', 'Crédito'),
        ('CO', 'Contado'),
    )

    STATUS_CHOICES = (
        ('CA', 'Con Adeudo'),
        ('PG', 'Pagado'),
    )

    fecha_venta = models.DateField(default=date.today)
    tipo_venta = models.CharField(max_length=20, choices=VENTA_CHOICES, null=False, default=VENTA_CHOICES[0][0])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=False, default=STATUS_CHOICES[0][0])
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

