from django.shortcuts import render, redirect
from .models import Venta
from .forms import nuevaVentaForm
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
def ventasView(request):
    ventas = Venta.objects.all().order_by('fecha_venta')
    user = User.objects.filter(username=request.user).first()

    return render(request, 'ventas.html', {"ventas": ventas, "User": user})

def nuevaVentaView(request):
    user = User.objects.filter(username=request.user).first()

    if request.method == 'POST':
        form = nuevaVentaForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect("/ventas")
        else: 
            return render(request, 'nuevaVenta.html', {"User": user, 'form': form})
    else:
        form = nuevaVentaForm()

    return render(request, 'nuevaVenta.html', {"User": user, 'form': form})