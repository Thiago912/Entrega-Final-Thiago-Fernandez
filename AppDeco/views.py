from django.shortcuts import render
from django.http import HttpResponse
from AppDeco.forms import *
from AppDeco.models import *

# Create your views here.
def inicio(request):
    return render(request, 'AppDeco/inicio.html')
def espejo (request):
    return render(request, 'AppDeco/espejo.html')

def lampara (request):
    return render(request, 'AppDeco/lampara.html')

def espejoForm(request):

    if request.method == 'POST':

        formulario1 = EspejoFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            espejo = Espejo(nombre=info['nombre'], medida_alto=info['medida_alto'], medida_ancho=info['medida_ancho'], materiales=info['materiales'], precio=info['precio'])
        


            espejo.save()

            return render(request, 'AppDeco/inicio.html')
    else:

        formulario1=EspejoFormulario()

    return render(request, 'AppDeco/espejoFormulario.html', {'form1':formulario1})

def busquedaAlto(request):
    return render(request, 'AppDeco/inicio.html')

def resultados(request):
    if request.GET['medida_alto']:
        medida_alto = request.GET['medida_alto']
        nombre = Espejo.objects.filter(medida_alto__icontains=medida_alto)

        return render(request, 'AppDeco/inicio.html', {"nombre":nombre, "medida_alto":medida_alto})
    
    else:

        respuesta= 'No enviaste datos'

    return HttpResponse(respuesta)

def busquedaAltoL(request):
        return render(request, 'AppDeco/inicio.html')

def busquedaAltoS(request):
        return render(request, 'AppDeco/inicio.html')

def sillonForm(request):

    if request.method == 'POST':

        formulario1 = SillonFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            sillon = Sillon(nombre=info['nombre'], medida_alto=info['medida_alto'], medida_ancho=info['medida_ancho'], materiales=info['materiales'], precio=info['precio'])
        


            sillon.save()

            return render(request, 'AppDeco/inicio.html')
    else:

        formulario1=SillonFormulario()

    return render(request, 'AppDeco/sillonFormulario.html', {'form1':formulario1})

def lampForm(request):

    if request.method == 'POST':

        formulario1 = LamparaFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            lampara = Lampara(nombre=info['nombre'], medida_alto=info['medida_alto'], medida_ancho=info['medida_ancho'], materiales=info['materiales'], colorluz=info['colorluz'], precio=info['precio'])
        


            lampara.save()

            return render(request, 'AppDeco/inicio.html')
    else:

        formulario1=LamparaFormulario()

    return render(request, 'AppDeco/lampFormulario.html', {'form1':formulario1})

def resultadosS(request):
    if request.GET['medida_alto']:
        medida_alto = request.GET['medida_alto']
        nombre = Sillon.objects.filter(medida_alto__icontains=medida_alto)

        return render(request, 'AppDeco/inicio.html', {"nombre":nombre, "medida_alto":medida_alto})
    
    else:

        respuesta= 'No enviaste datos'

    return HttpResponse(respuesta)

def resultadosL(request):
    if request.GET['medida_alto']:
        medida_alto = request.GET['medida_alto']
        nombre = Lampara.objects.filter(medida_alto__icontains=medida_alto)

        return render(request, 'AppDeco/inicio.html', {"nombre":nombre, "medida_alto":medida_alto})
    
    else:

        respuesta= 'No enviaste datos'

    return HttpResponse(respuesta)

    
