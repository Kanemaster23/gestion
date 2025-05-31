from django.urls import path
from .views import gestionar_proyectos, inicio

urlpatterns = [
    path('', inicio, name='inicio'),
    path('gestionar/', gestionar_proyectos, name='gestionar_proyectos'),   
]