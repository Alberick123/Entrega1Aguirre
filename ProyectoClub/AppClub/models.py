from django.db import models

class Jugador(models.Model):
    
    nombre = models.CharField(max_length=40)
    altura = models.FloatField()
    edad = models.IntegerField()
    
    def __str__(self):
        return "{} - {}".format(self.nombre, self.altura)

class Disciplina(models.Model):
    
    nombre = models.CharField(max_length=40)
    sede = models.CharField(max_length=40)
    dias_realizacion = models.CharField(max_length=40)

    def __str__(self):
        return "{} - {}".format(self.nombre, self.sede)
    
class Estadio(models.Model):
    nombre = models.CharField(max_length=40)    
    direccion = models.CharField(max_length=40)
    anioFund = models.DateField()

    def __str__(self):
        return "{} - {}".format(self.nombre, self.direccion)
