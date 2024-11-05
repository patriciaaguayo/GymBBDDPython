from distutils.command.install_egg_info import install_egg_info

from paqueteGymBD.Clientes import Clientes
from paqueteGymBD.Conexion import Conexion

from paqueteGymBD.Conexion import Conexion
class GestionClientes:

    def __init__(self):
        Conn= Conexion()
        self.conexion = Conn.conectar()
        self.clientes = []


    """ Métodos para imprimir todos los clientes """

    def listar_clientes(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM Clientes")
            clientes_db = cursor.fetchall()
            self.clientes = [Clientes(codigo_cliente=cliente[0], nombre=cliente[1], dni=cliente[2], mensualidad=cliente[3]) for cliente in clientes_db]

        except:
            print("\n Error al realizar consulta")

    def imprimir_clientes(self):
        info = "\n\n Lista de clientes: \n\n"
        for cliente in self.clientes:
            info += " "+ cliente.listarClientes() + "\n"
        print(info)

    """ Métodos para imprimir los clientes morosos """

    def imprimir_clientes_morosos(self):
        info = "\n\n Lista de clientes morosos: \n\n"
        for cliente in self.clientes:
            if cliente.mensualidad == "Pendiente":
                info += " "+ cliente.listarClientesMensualidad() + "\n"
        print(info)

    """ Métodos para imprimir los clientes pagados """

    def imprimir_clientes_pagados(self):
        info = "\n\n Lista de clientes pagados: \n\n"
        for cliente in self.clientes:
            if cliente.mensualidad == "Pagado":
                info += " " + cliente.listarClientesMensualidad() + "\n"
        print(info)
