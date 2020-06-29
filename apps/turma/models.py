from django.db import models


class Turma(models.Model):

    turma = models.CharField(max_length=50)
    catequista = models.CharField(max_length=50)

    def __str__(self):
        return self.turma+' - '+self.catequista
