from django import forms
from .models import perro, usuario

class perroForm(forms.ModelForm):

    class Meta:
        model = perro
        fields = ('nombre_perro','raza_predominante','descripcion','estado',)

class usuarios(forms.ModelForm):

    class Meta:
        model = usuario
        fields = ('userNick','password','userEmail','userRun','userName','fecNac','userFono','userRegion','userComuna','userTipo')



