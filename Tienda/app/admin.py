from django.contrib import admin
from .models import Producto

class TiendaAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','categoria','stock','descripcion','imagen']

admin.site.register(Producto,TiendaAdmin)