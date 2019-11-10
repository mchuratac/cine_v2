from django.db import models
from django.utils import timezone

# Create your models here.
class Local(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    direccion = models.CharField(max_length=220, blank=False, null=False)
    tiposervicio = models.CharField(max_length=200, blank=False, null=False)
    precio = models.DecimalField(max_digits=10, decimal_places = 2)
    distrito = models.CharField(max_length=220, blank=False)
    imagen = models.ImageField(upload_to="pictures/%y", null=True)

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locales'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre



class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    id_local = models.ForeignKey(Local,on_delete=models.CASCADE)
    trailer = models.CharField(max_length=220, blank=False, null=False)
    titulo= models.CharField(max_length=220, blank=False, null=False)
    genero= models.CharField(max_length=220, blank=False, null=False)
    duracion= models.CharField(max_length=220, blank=False, null=False)
    categoria= models.CharField(max_length=220, blank=False, null=False)
    imagen= models.ImageField(upload_to="pictures/%y", null=True)
    psinosis = models.CharField(max_length=220, blank=False, null=True)
    director = models.CharField(max_length=220, blank=False, null = True)
    idioma = models.CharField(max_length=220, blank=False, null=True)

    class Meta:
        verbose_name = 'Pelicula'
        verbose_name_plural = 'Peliculas'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo


class Sala(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('nombre', max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Funcion (models.Model):
    id = models.AutoField(primary_key = True)
    id_local = models.ForeignKey(Local,on_delete=models.CASCADE)
    id_sala = models.ForeignKey(Sala,on_delete=models.CASCADE)
    id_pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    hora_funcion = models.CharField(max_length=220, blank=True, null=True)

    class Meta:
        verbose_name = 'Funcion'
        verbose_name_plural = 'Funciones'
        ordering = ['id_pelicula']
    
    def __str__(self):
        return self.hora_funcion

class Actor(models.Model):
    id = models.AutoField(primary_key = True)
    id_pelicula= models.ManyToManyField(Pelicula)
    nombre = models.CharField(max_length=220, blank=True, null=True)
    imagen = models.ImageField(upload_to="pictures/%y", null=True)

    
    class Meta:
        verbose_name = 'Actor'
        verbose_name_plural = 'Actores'
        ordering = ['nombre']

    def __str__(self):
        return (self.nombre)

        
class Venta(models.Model):
    id = models.AutoField(primary_key = True)
    id_usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    id_funcion = models.ForeignKey(Funcion, null=False, blank=False, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null = False)
    fecha_venta = models.DateTimeField (
        default=timezone.now)    
        
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id_usuario']

    def __str__(self):
   
        return f'{self.id_usuario} - {self.id_funcion} - {self.cantidad} - {self.fecha_venta}'