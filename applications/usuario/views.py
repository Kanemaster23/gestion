import random
import datetime
from django.core.mail import send_mail
from django.conf import settings

from django.shortcuts import render, redirect
from .forms import UsuarioRegistroForm
from django.contrib.auth.hashers import check_password
from applications.usuario.models import Usuario

def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioRegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            from django.contrib.auth.hashers import make_password
            usuario.contraseña = make_password(form.cleaned_data['contraseña'])
            usuario.save()
            return redirect('registro_exitoso')
    else:
        form = UsuarioRegistroForm()

    return render(request, 'usuario/registro.html', {'form': form})

def login_usuario(request):
    error = None
    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombre_usuario')
        contraseña = request.POST.get('contraseña')
        
        try:
            usuario = Usuario.objects.get(nombre_usuario=nombre_usuario)
            if check_password(contraseña, usuario.contraseña):  # ✅ Comparación segura
                request.session['usuario_id'] = usuario.id
                request.session['nombre_usuario'] = usuario.nombre_usuario
                return redirect('verificacion_2fa')
            else:
                error = "Contraseña incorrecta"
        except Usuario.DoesNotExist:
            error = "Usuario no encontrado"

    return render(request, 'usuario/login.html', {'error': error})

def enviar_codigo_verificacion(request):
    if 'usuario_id' not in request.session:
        return redirect('login_usuario')  # seguridad

    codigo = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    expiracion = datetime.datetime.now() + datetime.timedelta(minutes=5)

    request.session['codigo_2fa'] = codigo
    request.session['codigo_expira'] = expiracion.strftime('%Y-%m-%d %H:%M:%S')

    usuario = Usuario.objects.get(id=request.session['usuario_id'])

    send_mail(
    'Tu codigo de verificacion',
    f'Tu codigo de verificacion es: {codigo}',
    settings.DEFAULT_FROM_EMAIL,
    [usuario.correo],
    fail_silently=False,
    )

    return render(request, 'usuario/2fa.html', {
        'correo': usuario.correo,
        'expiracion': expiracion.strftime('%Y-%m-%d %H:%M:%S')
    })

def verificar_codigo_2fa(request):
    if request.method == 'POST':
        ingresado = request.POST.get('codigo')
        expiracion = datetime.datetime.strptime(request.session['codigo_expira'], '%Y-%m-%d %H:%M:%S')
        actual = datetime.datetime.now()

        if actual > expiracion:
            return render(request, 'usuario/2fa.html', {'error': 'El código ha expirado.'})

        if ingresado == request.session.get('codigo_2fa'):
            return redirect('login_exitoso')
        else:
            return render(request, 'usuario/2fa.html', {'error': 'Código incorrecto.'})
        
def logout_usuario(request):
    request.session.flush()
    return redirect('inicio')