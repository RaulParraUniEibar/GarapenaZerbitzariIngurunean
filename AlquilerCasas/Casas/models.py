from django.db import models

# Create your models here.
class Casas(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=300)
    numerodepersonas = models.IntegerField()
    
    def __unicode__ (self):
        return self.nombre
    
class Personas(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    dni = models.CharField(max_length=100)

    def __unicode__ (self):
        return self.nombre


class Alquiler(models.Model):
    dia = models.CharField(max_length=20)
    casaalquiler = models.ForeignKey(Casas, on_delete= models.CASCADE)
    personaalquiler = models.ForeignKey(Personas, on_delete= models.CASCADE)

    def __unicode__ (self):
        return self.personaalquiler