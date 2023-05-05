from django.db import models
from apps.veterinaria.models.Mascota import Mascota


class HistoriaClinica(models.Model):

    mascota = models.ForeignKey(
        Mascota, verbose_name='Mascota', on_delete=models.PROTECT,)
    fecha_consulta = models.DateField(verbose_name='Fecha de consulta')
    observaciones = models.CharField(
        verbose_name="observaciones", max_length=255, null='false')

    class Meta:
        ordering = ['id']
        db_table = 'Historia'
        verbose_name_plural = 'historias clinica'
        verbose_name = 'historia clinica'

    def __str__(self):
        return '{}'.format(
            self.mascota
        )
