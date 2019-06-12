from django.db import models
from django.utils import timezone


# Create your models here.
class Bulletin(models.Model):
   numero = models.CharField(max_length=42)
   date = models.DateField(verbose_name="Date de parution (AAAA-MM-JJ)")
   pdf = models.FileField(null = True)
   def __str__(self):
       return self.numero
