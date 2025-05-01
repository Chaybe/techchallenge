from django.db import models

class Processamento(models.Model):
    num1 = models.PositiveIntegerField()
    num2 = models.PositiveIntegerField()
    num3 = models.PositiveIntegerField()
    status = models.CharField(max_length=20)
    media = models.PositiveIntegerField()
    mediana = models.PositiveIntegerField()