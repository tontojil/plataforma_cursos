from django.contrib import admin
from .models import Instructor
from .models import Curso
from .models import Estudiante
from .models import Inscripcion

# Registro del modelo de datos para verlo en el admin
admin.site.register(Instructor)
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Inscripcion)
