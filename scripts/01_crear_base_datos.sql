CREATE DATABASE IF NOT EXISTS plataforma_cursos_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER 'plataforma_user'@'localhost' IDENTIFIED BY 'plataforma123';
CREATE USER 'plataforma_user'@'127.0.0.1' IDENTIFIED BY 'plataforma123';

GRANT ALL PRIVILEGES ON plataforma_cursos_db.* TO 'plataforma_user'@'localhost';
GRANT ALL PRIVILEGES ON plataforma_cursos_db.* TO 'plataforma_user'@'127.0.0.1';

FLUSH PRIVILEGES;

