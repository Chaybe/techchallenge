from django.db import models

class Calculation(models.Model):
    n1 = models.PositiveIntegerField()
    n2 = models.PositiveIntegerField()
    n3 = models.PositiveIntegerField()
    status = models.CharField(max_length=20)
    media = models.PositiveIntegerField()
    mediana = models.PositiveIntegerField()