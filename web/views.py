from django.shortcuts import render
from .models import Categoria, Producto

# Create your views here.
""" VISTAS PARA EL CATALOGO DE PRODUCTOS """

def index(request):
    listaProductos = Producto.objects.all()
    listaCategorias = Categoria.objects.all()

    context = {
        'productos': listaProductos,
        'categorias': listaCategorias
    }

    return render(request, 'index.html', context)

def productosPorCategoria(request, categoria_id):
    """ VISTA PARA FILTRAR LOS PRODUCTOS POR CATEGORIA """
    objCategoria = Categoria.objects.get(pk=categoria_id)
    listaProductos = objCategoria.producto_set.all()

    listaCategorias = Categoria.objects.all()

    context = {
        "categorias": listaCategorias,
        "productos": listaProductos
    }

    return render(request, "index.html", context)

def productosPorNombre(request):
    """" VISTA PARA FILTRADO DE PRODUCTOS POR NOMBRE """
    nombre = request.POST["nombre"]
    
    listaProductos = Producto.objects.filter(nombre__icontains=nombre)
    listaCategorias = Categoria.objects.all()
    
    context = {
        "categorias": listaCategorias,
        "productos": listaProductos
    }
    
    return render(request,"index.html",context)
