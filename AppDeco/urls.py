from django.urls import path
from AppDeco.views import *

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('espejo/', espejo, name='Espejos'),
    path('lampara/', lampara, name='Lámparas'),
    path('espejoFormulario/', espejoForm, name='EspejoFormulario'),
    path('buscarAlto/', busquedaAlto, name='BusquedaAlto'),
    path('resultados/', resultados, name='ResultadosBusqueda'),
    path('buscarAltoL/', busquedaAltoL, name='BusquedaAltoL'),
    path('buscarAltoS/', busquedaAltoS, name='BusquedaAltoS'),
    path('sillonFormulario/', sillonForm, name='SillonFormulario'),
    path('lampFormulario/', lampForm, name='LamparaFormulario'),
]