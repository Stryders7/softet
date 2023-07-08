from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "alumnos/index.html")

def productos(request):
    return render(request, "alumnos/productos.html")

def cosas(request):
    return render(request, "alumnos/cosas.html")

def formulario(request):
    return render(request, "alumnos/formulario.html")