from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from .constantes import ESTRELLAS_MAXIMAS, JUEGOS, NIVELES

# Create your models here.
class Progreso(models.Model):
    usuario=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='progresos',
    )
    juego = models.CharField(max_length=20, choices=JUEGOS)
    nivel=models.PositiveSmallIntegerField(choices=NIVELES)
    completado=models.BooleanField(default=False)
    estrellas=models.PositiveSmallIntegerField(
                default=0,
               validators=[MinValueValidator(0), MaxValueValidator] 

    )
    mehor_puntaje=models.PositiveSmallIntegerField(default=0)
    veces_jugado=models.PositiveSmallIntegerField(default=0)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)

    class meta:

        verbose_name='progreso'
        verbose_name_plural='progresos'
        ordering=['usuario','juego', 'nivel']

        constraints=[
        models.UniqueConstraint(
               fields=['usuario','juego', 'nivel'],
               name='progreso_unico_por_usuario_juego_nivel'
        ),
        
     ]
def __str__(self):
    return f'{self.usuario.username} . {self.get_juego_display()} . {self.get_nivel_display()}'