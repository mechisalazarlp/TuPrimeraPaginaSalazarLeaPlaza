from django import forms
from .models import Artista, Obra, MovimientoArtistico

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nombre', 'nacionalidad', 'biografia']

class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ['titulo', 'anio', 'tecnica']

class MovimientoForm(forms.ModelForm):
    class Meta:
        model = MovimientoArtistico
        fields = ['nombre', 'periodo', 'descripcion']

class BuscarArtistaForm(forms.Form):
    nombre = forms.CharField(label='Buscar artista', max_length=100)