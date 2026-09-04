from django.shortcuts import render

# Renderizado de pagina de bienvenida
def bienvenida(request):
    contexto = {
        'nombre_proyecto': 'Plataforma de Cursos Online',
        'descripcion': 'Plataforma para publicar cursos en linea y llevar el registro de sus estudiantes.',
    }
    return render(request, 'bienvenida.html', contexto)
