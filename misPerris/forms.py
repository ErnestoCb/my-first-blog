from django import forms
from .models import perro

class perroForm(forms.ModelForm):

    class Meta:
        model = perro
        fields = ('nombre_perro','raza_predominante','descripcion','estado',)


