from django.shortcuts import render
from django.http import HttpResponse
from AppDeco.forms import *
from AppDeco.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicioSesion(request):
      if request.method == 'POST':
            form = AuthenticationForm(request, data = request.POST)
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)

                  if user:
                        login(request, user)
                        return render(request, 'AppDeco/inicio.html', {'mensaje':f'Bienvenido {user}'})
            else:
                  return render(request, 'AppDeco/inicio.html', {'mensaje':'Datos incorrectos'})
      else:
            form = AuthenticationForm()
      return render(request, 'AppDeco/login.html', {'formulario':form})

def registro(request):
      if request.method == 'POST':
            form = UsuarioRegistro(request.POST)

            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request, 'AppDeco/inicio.html', {'mensaje':'Usuario Creado.'})
      
      else:
            form = UsuarioRegistro()
      return render(request, 'AppDeco/registro.html', {'formulario':form})

@login_required
def editarUsuario(request):
      usuario = request.user

      if request.method == 'POST':
            form = FormularioEditar(request.POST)

            if form.is_valid():
                  
                  info = form.cleaned_data
                  
                  usuario.email = info['email']
                  usuario.set_password(info['password1'])
                  usuario.first_name= info['first_name']
                  usuario.last_name= info['last_name']

                  usuario.save()

                  return render(request, 'AppDeco/inicio.html')
      else:
          
          form = FormularioEditar(initial={'email':usuario.email,'first_name':usuario.first_name,'last_name':usuario.last_name,})
        
      return render(request, 'AppDeco/editarPerfil.html', {'formulario':form, 'usuario':usuario})

def inicio(request):
    return render(request, 'AppDeco/inicio.html')

def busquedaAlto(request):
    return render(request, 'AppDeco/inicio.html')

def resultados(request):
    if request.GET['medida_alto']:
        medida_alto = request.GET['medida_alto']
        nombre = Espejo.objects.filter(medida_alto__icontains=medida_alto)

        return render(request, 'AppDeco/resultados.html', {"nombre":nombre, "medida_alto":medida_alto})
    
    else:

        respuesta= 'No enviaste datos'

    return HttpResponse(respuesta)

def busquedaAltoL(request):
        return render(request, 'AppDeco/resultadosLL.html')

def busquedaAltoS(request):
        return render(request, 'AppDeco/resultadosSS.html')

def resultadosS(request):
    if request.GET['medida_alto']:
        medida_alto = request.GET['medida_alto']
        nombre = Sillon.objects.filter(medida_alto__icontains=medida_alto)

        return render(request, 'AppDeco/resultadosS.html', {"nombre":nombre, "medida_alto":medida_alto})
    
    else:

        respuesta= 'No enviaste datos'

    return HttpResponse(respuesta)

def resultadosL(request):
    if request.GET['medida_alto']:
        medida_alto = request.GET['medida_alto']
        nombre = Lampara.objects.filter(medida_alto__icontains=medida_alto)

        return render(request, 'AppDeco/resultadosL.html', {"nombre":nombre, "medida_alto":medida_alto})
    
    else:

        respuesta= 'No enviaste datos'

    return HttpResponse(respuesta)

@login_required
def agregarAvatar(request):
      if request.method=='POST':
            form = AvatarFormulario(request.POST, request.FILES)

            if form.is_valid():
                  usuarioActual = User.objects.get(username=request.user)

                  avatar = Avatar(user=usuarioActual, imagen=form.cleaned_data['imagen'])

                  avatar.save()

                  return render(request, 'AppDeco/inicio.html')
      else:
            form = AvatarFormulario()

      return render(request, 'AppDeco/agregarAvatar.html', {'formulario':form})

def aboutMe(request):
      return render(request, 'AppDeco/about.html')

class ListaEspejo(ListView):
    model= Espejo

class DetalleEspejo(DetailView):
    model = Espejo

class CrearEspejo(LoginRequiredMixin, CreateView):
    model = Espejo
    success_url = '/AppDeco/espejo/list/'
    fields = ['nombre', 'medida_alto', 'medida_ancho', 'materiales', 'precio', 'imagen']

class ActualizarEspejo(LoginRequiredMixin, UpdateView):
        model = Espejo
        success_url = '/AppDeco/espejo/list'
        fields = ['nombre', 'medida_alto', 'medida_ancho', 'materiales', 'precio', 'imagen']

class BorrarEspejo(LoginRequiredMixin, DeleteView):
            model = Espejo
            success_url = '/AppDeco/espejo/list'

class ListaSillon(ListView):
    model= Sillon

class DetalleSillon(DetailView):
    model = Sillon

class CrearSillon(LoginRequiredMixin, CreateView):
    model = Sillon
    success_url = '/AppDeco/sillon/list/'
    fields = ['nombre', 'medida_alto', 'medida_ancho', 'materiales', 'precio', 'imagen']

class ActualizarSillon(LoginRequiredMixin, UpdateView):
        model = Sillon
        success_url = '/AppDeco/sillon/list'
        fields = ['nombre', 'medida_alto', 'medida_ancho', 'materiales', 'precio', 'imagen']

class BorrarSillon(LoginRequiredMixin, DeleteView):
            model = Sillon
            success_url = '/AppDeco/sillon/list'

class ListaLampara(ListView):
    model= Lampara

class DetalleLampara(DetailView):
    model = Lampara

class CrearLampara(LoginRequiredMixin, CreateView):
    model = Lampara
    success_url = '/AppDeco/lampara/list/'
    fields = ['nombre', 'medida_alto', 'medida_ancho', 'materiales', 'colorluz', 'precio', 'imagen']

class ActualizarLampara(LoginRequiredMixin, UpdateView):
        model = Lampara
        success_url = '/AppDeco/lampara/list'
        fields = ['nombre', 'medida_alto', 'medida_ancho', 'materiales', 'colorluz', 'precio', 'imagen']

class BorrarLampara(LoginRequiredMixin, DeleteView):
            model = Lampara
            success_url = '/AppDeco/lampara/list'

