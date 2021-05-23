from django.db import models

class Anuncio(models.Model):
    fecha = models.DateTimeField(auto_now=True)
    nombre = models.CharField(null=False, blank=False, max_length=40)
    imagen = models.URLField(null=True, blank=True, default=None)
    direccion = models.CharField(null=False, blank=False, max_length=40)
    latitud = models.CharField(null=False, blank=False, max_length=20)
    longitud = models.CharField(null=False, blank=False, max_length=20)
    titulo = models.CharField(null=False, blank=False, max_length=50)
    precio = models.DecimalField(null=False, blank=False, max_digits=5, decimal_places=2)
    descripcion = models.TextField(null=True, blank=True, max_length=500, default=None)
    email = models.EmailField(null=False, blank=False)
    celular = models.CharField(null=True, blank=True, max_length=20, default=None)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'anuncio'
        ordering = ["-fecha"]
