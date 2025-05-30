from django.urls import path
from .views import gestionar_proyectos

urlpatterns = [
    path('', gestionar_proyectos, name='gestionar_proyectos'),
]