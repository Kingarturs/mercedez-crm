# Generated by Django 3.1.7 on 2021-05-04 04:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sucursales', '0001_initial'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_venta', models.DateField(default=datetime.date.today)),
                ('tipo_venta', models.CharField(choices=[('FI', 'Financiado'), ('CR', 'Crédito'), ('CO', 'Contado')], default='FI', max_length=20)),
                ('status', models.CharField(choices=[('CA', 'Con Adeudo'), ('PG', 'Pagado')], default='CA', max_length=20)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
                ('prospecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.prospecto')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sucursales.sucursal')),
            ],
        ),
    ]
