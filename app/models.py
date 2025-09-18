from django.db import models

class Pokemon(models.Model):
    nome = models.CharField(max_length=100)
    icon = models.URLField()
    tipo = models.CharField(max_length=100)