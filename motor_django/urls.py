from django.contrib import admin
from django.urls import path, include
from cursos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.bienvenida, name='bienvenida'),
    path('cursos/', include('cursos.urls')),
]

# Pagina personalizada para el error 404
handler404 = 'cursos.views.error_404'
