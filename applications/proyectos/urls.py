from django.urls import path
from .views import gestionar_proyectos, inicio, sobre_nosotros

urlpatterns = [
    path('', inicio, name='inicio'),
    path('gestionar/', gestionar_proyectos, name='gestionar_proyectos'),
    path('sobre-nosotros/', sobre_nosotros, name='sobre_nosotros'),   
]