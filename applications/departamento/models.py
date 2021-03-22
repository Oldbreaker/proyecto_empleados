from django.db import models


class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre_corto', max_length=50, unique=True)
    anulate = models.BooleanField('Anulado', default=False)

    def __str__(self):
        return self.name + ' - ' + self.short_name
