from django.db import models


# Profesor que dicta los cursos
class Instructor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    especialidad = models.CharField(max_length=100)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


# Curso publicado en la plataforma
class Curso(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    duracion_horas = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE,
        related_name='cursos'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['titulo']

    def __str__(self):
        return self.titulo


# Persona que se inscribe a los cursos
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


# Inscripcion de un estudiante a un curso
class Inscripcion(models.Model):
    ESTADOS = [
        ('inscrito', 'Inscrito'),
        ('en_curso', 'En curso'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ]

    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='inscrito')
    nota_final = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)

    class Meta:
        ordering = ['-fecha_inscripcion']
        # Un estudiante no se puede inscribir dos veces al mismo curso
        unique_together = ['estudiante', 'curso']

    def __str__(self):
        return f'{self.estudiante} en {self.curso}'
