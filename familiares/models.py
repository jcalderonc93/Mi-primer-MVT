from pyexpat import model
from xml.dom.minidom import Document
from django.db import models



# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=15)
    documento = models.IntegerField()
    nacimiento = models.DateField()

    def __str__(self):
        return f"nombre: {self.nombre} documento: {self.documento} nacimiento: {self.nacimiento}"