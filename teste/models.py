from django.db import models

# Create your models here.

class Pessoa(models.Model):
   nome  = models.CharField(max_length=150)
   email = models.EmailField(max_length=200)

 

