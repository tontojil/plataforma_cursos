from django.urls import path, include
from rest_framework import routers
from cursos import views

# Enrutador que crea solo las urls del CRUD de cada modelo
enrutador = routers.DefaultRouter()
enrutador.register(r'instructores', views.InstructorViewSet)
enrutador.register(r'cursos', views.CursoViewSet)
enrutador.register(r'estudiantes', views.EstudianteViewSet)
enrutador.register(r'inscripciones', views.InscripcionViewSet)

urlpatterns = [
    path('', include(enrutador.urls)),
]
