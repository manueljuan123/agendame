CREATE DATABASE agendate;
use agendate;


create table usuario (
nombreUsuario VARCHAR (50) NOT NULL,
apellidoUsuario VARCHAR(50) NOT NULL,
edadUsuario INT NOT NULL,
ocupacion VARCHAR(50)  NOT NULL,
email VARCHAR(60) PRIMARY KEY NOT NULL,
contrasena VARCHAR(50)  NOT NULL);

create table eventos(
codEvento INT PRIMARY KEY NOT NULL,
descripcion VARCHAR(70) NOT NULL,
hora TIME NOT NULL,
fecha DATE NOT NULL,
lugar VARCHAR(50)  NOT NULL
);
