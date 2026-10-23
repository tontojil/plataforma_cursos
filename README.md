# Plataforma de Cursos Online - Eva 2

Proyecto de la Evaluacion 2 de Backend con Python, Django y Django REST Framework.
Continuacion de la Eva 1 con el mismo tema, hecho como en clases.

## Descripcion

Sobre la base de la Eva 1 (proyecto `motor_django` + app `cursos`
con pagina de bienvenida y 404 personalizado) se agrega:

- Modelo de datos completo en `cursos/models.py`
- Migraciones en `cursos/migrations/`
- API REST con Django REST Framework
- Serializadores en `cursos/serializer.py`
- ModelViewSet en `cursos/views.py`
- URLs con Router en `cursos/urls.py`
- Conexion MySQL con variables de entorno en `.env` (con `python-decouple`)
- Script SQL en `scripts/`

### Modelo de datos

- `Instructor`: nombre, email, especialidad. Un instructor dicta varios cursos.
- `Curso`: titulo, descripcion, duracion_horas, precio, instructor (FK), fecha_creacion.
- `Estudiante`: nombre, email, fecha_registro.
- `Inscripcion`: estudiante (FK), curso (FK), fecha_inscripcion, estado, nota_final.
  Un estudiante no se repite en el mismo curso (`unique_together`).

## Requisitos

- Python 3.12 o superior
- MySQL 8.0 corriendo en local (puerto 3306)
- Git

Nota: en clases el profe usa `Django==6.1` y `mysqlclient`. Aqui se usa
`Django==5.2.8` porque es compatible con MySQL 8.0, y `PyMySQL` en vez de
`mysqlclient` para no compilar en Windows. El codigo es el mismo de clases.

## Como ejecutar el proyecto

1. Crear la base de datos y el usuario con el script:

```sql
-- En MySQL Workbench como root:
SOURCE scripts/01_crear_base_datos.sql;
```

O por consola:

```
mysql -u root -p < scripts/01_crear_base_datos.sql
```

2. Crear el ambiente virtual:

```
python -m venv .venv
```

3. Activar el ambiente virtual:

```
.venv\Scripts\Activate
```

4. Instalar las dependencias:

```
pip install -r requirements.txt
```

5. Revisar el archivo `.env` (ya viene listo para la evaluacion).

6. Crear y aplicar migraciones:

```
python manage.py makemigrations
python manage.py migrate
```

7. Ejecutar el servidor:

```
python manage.py runserver
```

8. Abrir en el navegador:

- Bienvenida: http://127.0.0.1:8000/
- API: http://127.0.0.1:8000/cursos/
- Admin: http://127.0.0.1:8000/admin/

Para probar el 404 personalizado, entrar a una ruta que no existe, por ejemplo
http://127.0.0.1:8000/ruta-que-no-existe/ (con `DEBUG=False` en el `.env`).

## Endpoints de la API

Todos con CRUD completo: GET (listar y detalle), POST (crear), PUT (reemplazo
completo), PATCH (cambio parcial) y DELETE (borrar).

- http://127.0.0.1:8000/cursos/instructores/
- http://127.0.0.1:8000/cursos/cursos/
- http://127.0.0.1:8000/cursos/estudiantes/
- http://127.0.0.1:8000/cursos/inscripciones/

Ejemplo rapido con un instructor:

```
# Crear
curl -X POST http://127.0.0.1:8000/cursos/instructores/ -H "Content-Type: application/json" -d "{\"nombre\": \"Ana Rojas\", \"email\": \"ana@ejemplo.cl\", \"especialidad\": \"Python\"}"

# Listar
curl http://127.0.0.1:8000/cursos/instructores/
```

## Estructura minima pedida

```
plataforma_cursos/
  manage.py
  requirements.txt
  README.md
  .env
  .env.example
  scripts/01_crear_base_datos.sql
  motor_django/settings.py
  motor_django/urls.py
  cursos/models.py
  cursos/serializer.py
  cursos/views.py
  cursos/urls.py
  cursos/migrations/
  cursos/templates/bienvenida.html
  cursos/templates/404.html
```
