from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Cliente)
admin.site.register(TipoMascota)
admin.site.register(HistoriaClinica)



class HistoriaClinica_inline(admin.StackedInline):
    model= HistoriaClinica
    extra=0
    
class Mascota_Admin(admin.ModelAdmin):
    inlines=[
    HistoriaClinica_inline,
    ]
    
admin.site.register(Mascota, Mascota_Admin)