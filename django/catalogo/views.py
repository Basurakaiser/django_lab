from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria 

def producto_lista(request):
    categoria_id = request.GET.get('categoria')
    
    productos = Producto.objects.select_related('categoria').all()
    categoria_seleccionada = None
    
    if categoria_id:
        categoria_seleccionada = get_object_or_404(Categoria, id=categoria_id)
        productos = productos.filter(categoria_id=categoria_id)
        
    contexto = {
        'productos': productos,
        'categoria_seleccionada': categoria_seleccionada,
    }
    return render(request, 'catalogo/lista.html', contexto)

def producto_detalle(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'catalogo/detalle.html', {'producto': producto})
