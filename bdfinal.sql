CREATE DATABASE agendate;
use agendate;


create table usuario (
idUsuario INT PRIMARY KEY NOT NULL,
nombreUsuario VARCHAR (50) NOT NULL,
apellidoUsuario VARCHAR(50) NOT NULL,
edadUsuario INT NOT NULL,
ocupacion VARCHAR(50)  NOT NULL,
email VARCHAR(60) NULL,
contrasena VARCHAR(50)  NOT NULL);

create table eventos(
id INT(11) PRIMARY KEY NOT NULL,
descripcion VARCHAR(70) NOT NULL,
hora TIME NOT NULL,
fecha DATE NOT NULL,
lugar VARCHAR(50)  NOT NULL,
codEvento INT NOT NULL,
FOREIGN KEY(codEvento) REFERENCES usuario (idUsuario));
