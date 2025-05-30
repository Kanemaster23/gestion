from django.shortcuts import render, redirect
from applications.proyectos.models import Proyecto
from applications.usuario.models import Usuario

def gestionar_proyectos(request):
    usuario = Usuario.objects.get(id=request.session['usuario_id'])

    if request.method == 'POST':
        nombre = request.POST['nombre']
        fecha_final = request.POST['fecha_final']
        integrantes = request.POST['numero_integrantes']
        descripcion = request.POST.get('descripcion', '')

        Proyecto.objects.create(
            usuario=usuario,
            nombre=nombre,
            fecha_final=fecha_final,
            numero_integrantes=integrantes,
            descripcion=descripcion
        )
        return redirect('gestionar_proyectos')

    proyectos = Proyecto.objects.filter(usuario=usuario).order_by('-creado_en')
    return render(request, 'proyectos/gestionar.html', {'proyectos': proyectos})