from django import forms

class EspejoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    medida_alto = forms.IntegerField()
    medida_ancho = forms.IntegerField()
    materiales = forms.CharField(max_length=40)
    precio = forms.IntegerField()

class SillonFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    medida_alto = forms.IntegerField()
    medida_ancho = forms.IntegerField()
    materiales = forms.CharField(max_length=40)
    precio = forms.IntegerField()

class LamparaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    medida_alto = forms.IntegerField()
    medida_ancho = forms.IntegerField()
    materiales = forms.CharField(max_length=40)
    colorluz = forms.CharField(max_length=40)
    precio = forms.IntegerField()