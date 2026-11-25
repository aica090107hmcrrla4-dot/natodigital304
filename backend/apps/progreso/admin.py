
from django.contrib import admin
from .models import Progreso

# Register your models here.
@admin.register(Progreso)
class ProgresoAdmin(admin.ModelAdmin):
    list_display = (
        'usuario',
        'juego',
        'completado',
        'estrellas',
        'veces_jugado',
        'actualizado',
    )
    list_filter = ('juego', 'nivel', 'completado')
    search_fields = ('usuario__username', 'usuario__first_name')
