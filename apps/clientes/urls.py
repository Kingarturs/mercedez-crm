from django.urls import path
from apps.productos import views as productos_views
from apps.clientes import views as clientes_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(clientes_views.admin_view, login_url='/')),
    path('productos', login_required(productos_views.productosView, login_url='/')),
    path('nuevoProducto', login_required(productos_views.nuevoProductoView, login_url='/')),
    path('vendedores', login_required(clientes_views.vendedoresView, login_url='/')),
    path('nuevoVendedor', login_required(clientes_views.nuevoVendedorView, login_url='/')),
]