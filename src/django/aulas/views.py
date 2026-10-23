#from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.
def hello(request):
    return HttpResponse("Hola Mundo")

def bye(request):
    return HttpResponse("Hasta Luego!")

def edad(request, anios, futuro):
    incremento = futuro - date.today().year
    cumplira = anios + incremento
    mensaje = "En el año %d cumplirás %d años"%(futuro, cumplira)
    
    return HttpResponse(mensaje)