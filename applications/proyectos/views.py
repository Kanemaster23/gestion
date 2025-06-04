from django.shortcuts import render, redirect
from applications.proyectos.models import Proyecto
from applications.usuario.models import Usuario

def gestionar_proyectos(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        fecha_final = request.POST['fecha_final']
        integrantes = request.POST['numero_integrantes']
        descripcion = request.POST.get('descripcion', '')

        Proyecto.objects.create(
            nombre=nombre,
            fecha_final=fecha_final,
            numero_integrantes=integrantes,
            descripcion=descripcion
        )
        return redirect('gestionar_proyectos')

    proyectos = Proyecto.objects.all().order_by('-creado_en')
    return render(request, 'proyectos/gestionar.html', {'proyectos': proyectos})


def inicio(request):
    return render(request, 'proyectos/inicio.html')