from django.urls import path
from AppDeco.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('buscarAlto/', busquedaAlto, name='BusquedaAlto'),
    path('resultados/', resultados, name='ResultadosBusqueda'),
    path('buscarAltoL/', busquedaAltoL, name='BusquedaAltoL'),
    path('buscarAltoS/', busquedaAltoS, name='BusquedaAltoS'),
    path('resultadoL/', resultadosL, name='ResultadosBusquedaL'),
    path('resultadoS/', resultadosS, name='ResultadosBusquedaS'),
    path('login/', inicioSesion, name='Login'),
    path('register/', registro, name='Registro'),
    path('logout/', LogoutView.as_view(template_name="AppDeco/logout.html"), name='Logout'),
    path('editar/', editarUsuario, name="EditarUsuario"),
    path('agregar/', agregarAvatar, name="Avatar"),
    path('about/', aboutMe, name="AboutMe"),

    #CRUD Espejos
    path('espejo/list/', ListaEspejo.as_view(), name='EspejosLeer'),
    path('espejo/<int:pk>', DetalleEspejo.as_view(), name='EspejosDetalle'),
    path('espejo/crear/', CrearEspejo.as_view(), name='EspejosCrear'),
    path('espejo/editar/<int:pk>', ActualizarEspejo.as_view(), name='EspejosActualizar'),
    path('espejo/borrar/<int:pk>', BorrarEspejo.as_view(), name='EspejosBorrar'),

    #CRUD Sillones
    path('sillon/list/', ListaSillon.as_view(), name='SillonesLeer'),
    path('sillon/<int:pk>', DetalleSillon.as_view(), name='SillonesDetalle'),
    path('sillon/crear/', CrearSillon.as_view(), name='SillonesCrear'),
    path('sillon/editar/<int:pk>', ActualizarSillon.as_view(), name='SillonesActualizar'),
    path('sillon/borrar/<int:pk>', BorrarSillon.as_view(), name='SillonesBorrar'),

    #CRUD Lámparas
    path('lampara/list/', ListaLampara.as_view(), name='LamparasLeer'),
    path('lampara/<int:pk>', DetalleLampara.as_view(), name='LamparasDetalle'),
    path('lampara/crear/', CrearLampara.as_view(), name='LamparasCrear'),
    path('lampara/editar/<int:pk>', ActualizarLampara.as_view(), name='LamparasActualizar'),
    path('lampara/borrar/<int:pk>', BorrarLampara.as_view(), name='LamparasBorrar'),
]