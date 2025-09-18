from django.db import models

class Pokemon(models.Model):
    no = models.IntegerField()
    nome = models.CharField(max_length=100)
    icon = models.URLField()
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    