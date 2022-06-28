from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Clientes, Articulos, Pedidos

# Create your views here.

def busqueda_productos(request):
    return render(request, 'busqueda_productos.html')

def buscar(request):
    if request.GET['busqueda']:
        #mensaje = 'Articulo buscado: ' + request.GET['busqueda']
        producto = request.GET['busqueda']
        articulos = Articulos.objects.filter(nombre__icontains=producto)
        return render(request, 'resultados_busqueda.html', {'articulos': articulos, "producto": producto})
    else:
        mensaje = 'No se ha introducido ningun articulo'

    return HttpResponse(mensaje)

def contacto(request):

    if request.method == 'POST':
        return render(request, 'gracias.html')

    return render(request, 'contacto.html')