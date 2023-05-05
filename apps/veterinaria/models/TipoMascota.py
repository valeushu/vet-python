from django.db import models


class TipoMascota(models.Model):

    nombreTipo = models.CharField(
        max_length=255, verbose_name="Tipo de Mascota")

    class Meta:
        ordering = ['id']
        db_table = 'TipoMascota'
        verbose_name_plural = 'tipo mascotas'
        verbose_name = 'tipo mascota'

    def __str__(self):
        return '{}'.format(
            self.nombreTipo
        )
