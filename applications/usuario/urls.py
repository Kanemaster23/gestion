from django.urls import path
from .views import registro_usuario, login_usuario, logout_usuario
from .views import enviar_codigo_verificacion, verificar_codigo_2fa
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('registro/', registro_usuario, name='registro'),
    path('registro/exitoso/', TemplateView.as_view(template_name="usuario/registro_exitoso.html"), name='registro_exitoso'),
    path('login/', login_usuario, name='login_usuario'),
    path('login/exitoso/', TemplateView.as_view(template_name='usuario/login_exitoso.html'), name='login_exitoso'),
    path('verificacion/', enviar_codigo_verificacion, name='verificacion_2fa'),
    path('verificacion/confirmar/', verificar_codigo_2fa, name='confirmar_2fa'),
    path('logout/', logout_usuario, name='logout_usuario'),   
]
