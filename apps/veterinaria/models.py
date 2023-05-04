from django.db import models

# Create your models here.


class Cliente(models.Model):

    CIUDAD_CHOICES = (
        ('0', 'ushuaia'),
        ('1', 'tolhuin'),
        ('2', 'rio grande'),
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
