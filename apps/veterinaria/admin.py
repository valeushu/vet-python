from django.contrib import admin

from apps.veterinaria.models.Clientes import Cliente
from apps.veterinaria.models.HistoriaClinica import HistoriaClinica
from apps.veterinaria.models.Mascota import Mascota
from apps.veterinaria.models.TipoMascota import TipoMascota


admin.site.register(Cliente)
admin.site.register(TipoMascota)
admin.site.register(HistoriaClinica)


class HistoriaClinica_inline(admin.StackedInline):
    model = HistoriaClinica
    extra = 0


class Mascota_Admin(admin.ModelAdmin):
    inlines = [
        HistoriaClinica_inline,
    ]


admin.site.register(Mascota, Mascota_Admin)
