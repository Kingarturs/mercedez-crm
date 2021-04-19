from django.shortcuts import redirect, render
from .models import Producto
from django.contrib.auth import get_user_model
from .forms import nuevoProductoForm

User = get_user_model()

# Create your views here.
def agendarView(request):
    return render(request, 'agendar.html')

def productosView(request):

    if request.method == "POST":
        pk = request.POST.get("pk")
        producto = Producto.objects.filter(pk=pk).first()
        if producto != None:
            producto.delete()

    productos = Producto.objects.all()
    user = User.objects.filter(username=request.user).first()

    if user.tipo == 'MA':
        return render(request, 'productos.html', {"productos": productos, "User": user})
    else:
        return redirect('/')

def nuevoProductoView(request):
    productos = Producto.objects.all()
    user = User.objects.filter(username=request.user).first()

    if user.tipo == 'MA':
        if request.method == 'POST':
            form = nuevoProductoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/menu/productos")
            else: 
                return render(request, 'nuevoProducto.html', {"productos": productos, "User": user, 'form': form})
        else:
            form = nuevoProductoForm()

        return render(request, 'nuevoProducto.html', {"productos": productos, "User": user, 'form': form})
    else:
        return redirect('/')
