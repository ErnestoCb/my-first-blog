from django.db import models

# Create your models here.

class perro(models.Model):
    id_perro = models.AutoField(max_length=5, primary_key=True)
    foto = models.ImageField(null=True)
    nombre_perro = models.CharField(max_length=30, null=False)
    raza_predominante = models.CharField(max_length=30, null=False)
    descripcion = models.CharField(max_length=30, null=False)
    estados = (('R','Rescatado'),('D','Disponible'),('A','adoptado'))
    estado = models.CharField(max_length=1, choices=estados, default='R', null=False)

    def __str__(self):
        return self.nombre_perro
