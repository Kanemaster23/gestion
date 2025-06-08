from django.shortcuts import render, redirect, get_object_or_404
from applications.proyectos.models import Proyecto
from applications.usuario.models import Usuario

def gestionar_proyectos(request):
    if 'usuario_id' not in request.session:
        return redirect('login_usuario')

    usuario = Usuario.objects.get(id=request.session['usuario_id'])

    if request.method == 'POST':
        if 'crear' in request.POST:
            # Crear un nuevo proyecto
            Proyecto.objects.create(
                usuario=usuario,
                nombre=request.POST['nombre'],
                fecha_final=request.POST['fecha_final'],
                numero_integrantes=request.POST['numero_integrantes'],
                descripcion=request.POST.get('descripcion', '')
            )

        elif 'actualizar' in request.POST:
            proyecto_id = request.POST.get('proyecto_id')
            proyecto = get_object_or_404(Proyecto, id=proyecto_id, usuario=usuario)
            proyecto.nombre = request.POST['nombre']
            proyecto.fecha_final = request.POST['fecha_final']
            proyecto.numero_integrantes = request.POST['numero_integrantes']
            proyecto.descripcion = request.POST.get('descripcion', '')
            proyecto.save()

        elif 'eliminar' in request.POST:
            proyecto_id = request.POST.get('proyecto_id')
            proyecto = get_object_or_404(Proyecto, id=proyecto_id, usuario=usuario)
            proyecto.delete()

        return redirect('gestionar_proyectos')

    proyectos = Proyecto.objects.filter(usuario=usuario).order_by('-creado_en')
    return render(request, 'proyectos/gestionar.html', {'proyectos': proyectos})