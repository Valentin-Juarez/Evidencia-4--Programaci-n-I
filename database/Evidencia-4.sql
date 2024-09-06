drop database if exists soldador_vidral;

create database Soldador_Vidral;

USE Soldador_Vidral;

create table Producto(
	Codigo_Fabrica int not null primary key,
    Marca varchar (20) not null,
    Modelo Varchar (20) not null
);
create table Temperatura(
	Temperatura_Max int not null,
    TiempodeUso int,
    Codigo_Fabrica int not null,
    foreign key (Codigo_Fabrica) references Producto (Codigo_Fabrica)
);
select * from Producto;

INSERT INTO Producto (Codigo_Fabrica, Marca, Modelo)

VALUES(24362874, 'Black&Decker', 'YX-8034'),(48291736,'Kushiro','ESK-878D'),(75938421,'Vaxun','5200'),
(19384756,'Ja','SEP100'),(62849573,'Cimurat','SOLD004');

SELECT * FROM temperatura;

INSERT INTO temperatura (Temperatura_Max,TiempodeUso,Codigo_Fabrica)

VALUES(430,2,24362874),(440,3,48291736),(450,6,75938421),(220,4,19384756),(350,8,62849573);

SELECT TiempodeUso FROM temperatura;
SELECT Temperatura_Max FROM  temperatura;
SELECT Codigo_Fabrica FROM Producto;
 
