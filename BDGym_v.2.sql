create database BDGym;

use BDGym;

drop table Aparatos;

create table Aparatos(
codigo_aparato varchar(9) primary key, 
nombre_maquina varchar (50) not null
);

INSERT INTO Aparatos (codigo_aparato, nombre_maquina) 
VALUES 
('M12345678', 'Cinta de correr'),
('M23456789', 'Bicicleta estatica'),
('M80989365', 'Cinta de correr'),
('M45678901', 'Cinta de correr'),
('M56789012', 'Bicicleta estatica');

drop table Clientes;

create table Clientes(
codigo_cliente varchar(9) primary key,
nombre_cliente varchar (100) not null,
dni varchar(9) not null,
mensualidad varchar(15) not null
);

INSERT INTO Clientes (codigo_cliente, nombre_cliente, dni, mensualidad) 
VALUES 
('C12345678', 'Marco Polo Lopez', '12345678Z', 'Pendiente'),
('C23456789', 'Paco Porros Maria', '56789012P', 'Pendiente'),
('C34567890', 'Dora Exploradora India', '45678901J', 'Pendiente'),
('C45678901', 'Jose Garcia Sopa', '23456789S', 'Pagado'),
('C56789012', 'Ana Lopez Serrano', '34567890N', 'Pagado');

drop table Reservas;

create table Reservas(
codigo_aparato varchar(9), 
codigo_cliente varchar(9),
fecha date not null,
hora varchar(5) not null,
primary key (codigo_aparato, codigo_cliente),
foreign key (codigo_aparato) references Aparatos (codigo_aparato),
foreign key (codigo_cliente) references Clientes (codigo_cliente)
);

INSERT INTO Reservas (codigo_aparato, codigo_cliente, fecha, hora)
VALUES 
('M12345678', 'C12345678', '2024-10-10', '10:00'),
('M23456789', 'C23456789', '2024-10-14', '12:00'),
('M80989365', 'C23456789', '2024-10-31', '20:00'),
('M80989365', 'C34567890', '2024-10-31', '20:30'),
('M56789012', 'C56789012', '2024-10-25', '18:30');

select Reservas.codigo_aparato, Aparatos.nombre_maquina, Reservas.codigo_cliente, Clientes.nombre_cliente, Reservas.fecha, Reservas.hora from Reservas
inner join Clientes on Reservas.codigo_cliente = Clientes.codigo_cliente
inner join Aparatos on Reservas.codigo_aparato = Aparatos.codigo_aparato;