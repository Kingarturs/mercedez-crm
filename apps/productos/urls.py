from django.urls import path
from apps.productos import views as productos_views

urlpatterns = [
    path('car', productos_views.agendarView),
]