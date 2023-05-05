
from django.db import models
from apps.veterinaria.models.Clientes import Cliente
from apps.veterinaria.models.TipoMascota import TipoMascota


class Mascota(models.Model):
    propietario = models.ForeignKey(
        Cliente, verbose_name='Propietario', on_delete=models.PROTECT)
    tipo_mascota = models.ForeignKey(
        TipoMascota, verbose_name='Tipo de Mascota', on_delete=models.PROTECT,)
    numero_chip = models.IntegerField(
        verbose_name='Número de chip', blank=True,)
    nombre_mascota = models.CharField(
        verbose_name='Nombre de la Mascota', max_length=255,)
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    estado = models.BooleanField(verbose_name="Estado")

    def __str__(self):
        return f"{self.nombre_mascota} {self.propietario} {self.numero_chip}"

    class Meta:
        ordering = ['id']
        db_table = 'Mascota'
        verbose_name_plural = 'mascotas'
        verbose_name = 'mascota'
