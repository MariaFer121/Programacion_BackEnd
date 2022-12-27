from django.db import models

# Create your models here.
class Genero (models.Model):
    descripcion =models.CharField(max_length=45)

class Grupos( models.Model):
    nombre =models.CharField(max_length=45)
    formacion= models.DateField()
    desintegracion = models.DateField()
    genero = models.ManyToManyField(Genero, through='GenerosGrupos')


class Musico ( models.Model):
    nombre= models.CharField(max_length=45)
    instrumento = models.CharField(max_length=45)
    lugar_nacimiento = models.CharField(max_length=45)
    fecha_nacimiento = models.DateField()
    fecha_muerte = models.DateField()

class GenerosGrupos (models.Model):
    grupos = models.ForeignKey('Grupos', on_delete=models.PROTECT)
    genero = models.ForeignKey('Genero', on_delete=models.PROTECT)

class MusicosGrupos (models.Model):
    grupos = models.ForeignKey ('Grupos', on_delete=models.PROTECT)
    musicos =models.ForeignKey ('Musico',on_delete=models.PROTECT)
    instrumento = models.CharField(max_length=45)
    fecha_inicio= models.DateField()
    fecha_fin= models.DateField()