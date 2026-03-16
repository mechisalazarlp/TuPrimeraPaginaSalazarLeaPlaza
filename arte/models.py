from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    biografia = models.TextField()

    def __str__(self):
        return self.nombre

class Obra(models.Model):
    titulo = models.CharField(max_length=200)
    anio = models.IntegerField()
    tecnica = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class MovimientoArtistico(models.Model):
    nombre = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre