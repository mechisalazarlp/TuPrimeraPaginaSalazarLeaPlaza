from django.shortcuts import render, redirect
from .models import Artista, Obra, MovimientoArtistico
from .forms import ArtistaForm, ObraForm, MovimientoForm, BuscarArtistaForm

def inicio(request):
    return render(request, 'inicio.html')

def crear_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ArtistaForm()
    return render(request, 'crear_artista.html', {'form': form})

def crear_obra(request):
    if request.method == 'POST':
        form = ObraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ObraForm()
    return render(request, 'crear_obra.html', {'form': form})

def crear_movimiento(request):
    if request.method == 'POST':
        form = MovimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = MovimientoForm()
    return render(request, 'crear_movimiento.html', {'form': form})

def buscar_artista(request):
    resultados = []
    form = BuscarArtistaForm(request.GET or None)
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        resultados = Artista.objects.filter(nombre__icontains=nombre)
    return render(request, 'buscar_artista.html', {'form': form, 'resultados': resultados})