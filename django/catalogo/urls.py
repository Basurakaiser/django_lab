from django.urls import path
from . import views

urlpatterns = [
    path('', views.producto_lista, name='producto_lista'),
    path('productos/<int:id>/', views.producto_detalle, name='producto_detalle'),
]
