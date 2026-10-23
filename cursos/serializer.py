from rest_framework import serializers
from .models import Instructor
from .models import Curso
from .models import Estudiante
from .models import Inscripcion


# Convierte instructores a JSON y viceversa
class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'


# Convierte cursos a JSON y viceversa
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


# Convierte estudiantes a JSON y viceversa
class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'


# Convierte inscripciones a JSON y viceversa
class InscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripcion
        fields = '__all__'
