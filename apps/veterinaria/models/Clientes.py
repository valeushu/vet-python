from django.db import models


class Cliente(models.Model):

    CIUDAD_CHOICES = (
        ('0', 'Ushuaia'),
        ('1', 'Tolhuin'),
        ('2', 'Rio grande'),
    )

    dni = models.CharField(verbose_name="dni", max_length=255,
                           unique='true', null='false', blank='false')
    nombre = models.CharField(verbose_name="nombre",
                              max_length=255, null='false')
    apellido = models.CharField(verbose_name="apellido", max_length=255)
    ciudad = models.CharField(verbose_name="ciudad",
                              max_length=255, choices=CIUDAD_CHOICES)
    direccion = models.CharField(verbose_name="direccion", max_length=255)
    telefono = models.CharField(verbose_name="telefono", max_length=255)
    fechaAlta = models.DateField(auto_now_add='true')
    estado = models.BooleanField(default='true')

    class Meta:
        ordering = ['id']
        db_table = 'cliente'
        verbose_name_plural = 'clientes'
        verbose_name = 'cliente'

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)
