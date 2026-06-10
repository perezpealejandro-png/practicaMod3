-- Crear tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(255) UNIQUE,
    telefono VARCHAR(20),
    fecha_nacimiento DATE
);

-- Crear tabla de credenciales
CREATE TABLE IF NOT EXISTS credenciales (
    id_credencial SERIAL PRIMARY KEY,
    id_usuario INT NOT NULL,
username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    CONSTRAINT fk_usuario
      FOREIGN KEY (id_usuario)
      REFERENCES usuarios (id_usuario)
      ON DELETE CASCADE
);


-- Usuarios
INSERT INTO usuarios (nombre, correo, telefono, fecha_nacimiento) VALUES
('Juan Pérez', 'juan.perez@example.com', '777-111-2233', '1990-03-15'),
('María López', 'maria.lopez@example.com', '777-444-5566', '1992-08-21'),
('Carlos Ruiz', 'carlos.ruiz@example.com', '777-777-8899', '1988-12-05');

-- Credenciales (para demo usamos "password_hash" en claro; en un sistema real usarías hash)
INSERT INTO credenciales (id_usuario, username, password_hash) VALUES
(1, 'juan.perez1', 'hash_juan_perez'),
(2, 'maria.lopez2', 'hash_maria_lopez'),
(3, 'carlos.ruiz3', 'hash_carlos_ruiz');
