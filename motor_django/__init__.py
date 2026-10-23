# Paquete del proyecto motor_django
# Se usa PyMySQL como reemplazo de MySQLdb para no compilar mysqlclient en Windows
try:
    import pymysql
    # Django 6 pide mysqlclient 2.2.1 o mayor, se informa esa version
    pymysql.version_info = (2, 2, 1, 'final', 0)
    pymysql.install_as_MySQLdb()
except ImportError:
    pass
