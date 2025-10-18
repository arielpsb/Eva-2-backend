from django.shortcuts import render
from .models import Producto

def index (request):
    context = {}
    productos = Producto.objects.all()
    context['productos'] = productos
    return render(request,'main.html', context)

def producto_cat (request, categoria):
    context = {}
    productos = Producto.objects.filter(categoria = categoria)
    context['productos'] = productos
    context['categoria'] = categoria
    return render(request, 'categorias.html', context)

def producto_detalle (request, id):
    context = {}
    productos = Producto.objects.get(id=id)
    context['productos'] = productos
    return render(request, 'detalle_producto.html',context)