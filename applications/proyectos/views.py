from django.shortcuts import render, redirect, get_object_or_404
from applications.proyectos.models import Proyecto, Tarea
from applications.usuario.models import Usuario

def gestionar_proyectos(request):
    if 'usuario_id' not in request.session:
        return redirect('login_usuario')

    usuario = Usuario.objects.get(id=request.session['usuario_id'])

    if request.method == 'POST':
        # Crear proyecto
        if 'crear' in request.POST:
            Proyecto.objects.create(
                usuario=usuario,
                nombre=request.POST['nombre'],
                fecha_final=request.POST['fecha_final'],
                numero_integrantes=request.POST['numero_integrantes'],
                descripcion=request.POST.get('descripcion', '')
            )

        # Actualizar proyecto
        elif 'actualizar' in request.POST:
            proyecto = get_object_or_404(Proyecto, id=request.POST['proyecto_id'], usuario=usuario)
            proyecto.nombre = request.POST['nombre']
            proyecto.fecha_final = request.POST['fecha_final']
            proyecto.numero_integrantes = request.POST['numero_integrantes']
            proyecto.descripcion = request.POST.get('descripcion', '')
            proyecto.save()

        # Eliminar proyecto
        elif 'eliminar' in request.POST:
            proyecto = get_object_or_404(Proyecto, id=request.POST['proyecto_id'], usuario=usuario)
            proyecto.delete()

        # Añadir tarea a un proyecto
        elif 'agregar_tarea' in request.POST:
            proyecto = get_object_or_404(Proyecto, id=request.POST['proyecto_id'], usuario=usuario)
            Tarea.objects.create(
                proyecto=proyecto,
                descripcion=request.POST['descripcion_tarea']
            )

        # Marcar como completada o no
        elif 'toggle_completado' in request.POST:
            tarea = get_object_or_404(Tarea, id=request.POST['tarea_id'], proyecto__usuario=usuario)
            tarea.completada = not tarea.completada
            tarea.save()

        # Eliminar tarea
        elif 'eliminar_tarea' in request.POST:
            tarea = get_object_or_404(Tarea, id=request.POST['tarea_id'], proyecto__usuario=usuario)
            tarea.delete()

        # Editar tarea
        elif 'editar_tarea' in request.POST:
            tarea = get_object_or_404(Tarea, id=request.POST['tarea_id'], proyecto__usuario=usuario)
            nueva_desc = request.POST.get('nueva_descripcion', '').strip()
            if nueva_desc:
                tarea.descripcion = nueva_desc
                tarea.save()

        return redirect('gestionar_proyectos')

    proyectos = Proyecto.objects.filter(usuario=usuario).order_by('-creado_en').prefetch_related('tareas')
    return render(request, 'proyectos/gestionar.html', {'proyectos': proyectos})


def inicio(request):
    return render(request, 'proyectos/inicio.html')

def sobre_nosotros(request):
    return render(request, 'proyectos/sobre_nosotros.html')
