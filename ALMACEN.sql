CREATE DATABASE almacen;

USE almacen;

CREATE TABLE categoria (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre_categoria VARCHAR(255) NOT NULL
);

CREATE TABLE marca (
    id_marca INT AUTO_INCREMENT PRIMARY KEY,
    nombre_marca VARCHAR(255) NOT NULL
);

CREATE TABLE producto (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre_producto VARCHAR(255) NOT NULL,
    id_categoria INT,
    id_marca INT,
    FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria),
    FOREIGN KEY (id_marca) REFERENCES marca(id_marca)
);

CREATE TABLE precio (
    id_precio INT AUTO_INCREMENT PRIMARY KEY,
    id_producto INT,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_producto) REFERENCES producto(id_producto)
);

CREATE TABLE stock (
    id_stock INT AUTO_INCREMENT PRIMARY KEY,
    id_producto INT,
    cantidad_disponible INT NOT NULL,
    FOREIGN KEY (id_producto) REFERENCES producto(id_producto)
);

INSERT INTO categoria (nombre_categoria) VALUES
    ('Electrónica'),
    ('Ropa'),
    ('Hogar');
    
INSERT INTO marca (nombre_marca) VALUES
    ('Sony'),
    ('Samsung'),
    ('Nike'),
    ('Adidas'),
    ('Drean');
    
INSERT INTO producto (nombre_producto, id_categoria, id_marca) VALUES
    ('Televisor LED 55"', 1, 1),
    ('Smartphone Galaxy S21', 1, 2),
    ('Zapatillas Air Max', 2, 3),
    ('Remera Adidas',2,4),
    ('Lavadora de carga frontal', 3, 5);
    
INSERT INTO precio (id_producto, precio_unitario) VALUES
    (1, 799.99),
    (2, 899.99),
    (3, 129.99),
    (4, 499.99),
    (5,599.99);
    
INSERT INTO stock (id_producto, cantidad_disponible) VALUES
    (1, 10),
    (2, 15),
    (3, 25),
    (4, 30),
    (5,5);
    
    

