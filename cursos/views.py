from django.shortcuts import render
from rest_framework import viewsets
from .models import Instructor
from .models import Curso
from .models import Estudiante
from .models import Inscripcion
from .serializer import InstructorSerializer
from .serializer import CursoSerializer
from .serializer import EstudianteSerializer
from .serializer import InscripcionSerializer


# Renderizado de pagina de bienvenida
def bienvenida(request):
    contexto = {
        'nombre_proyecto': 'Plataforma de Cursos Online',
        'descripcion': 'Plataforma para publicar cursos en linea y llevar el registro de sus estudiantes.',
    }
    return render(request, 'bienvenida.html', contexto)


# Pagina personalizada para el error 404
def error_404(request, exception):
    return render(request, '404.html', status=404)


# CRUD completo de instructores con GET, POST, PUT, PATCH y DELETE
class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


# CRUD completo de cursos con GET, POST, PUT, PATCH y DELETE
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


# CRUD completo de estudiantes con GET, POST, PUT, PATCH y DELETE
class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer


# CRUD completo de inscripciones con GET, POST, PUT, PATCH y DELETE
class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer
