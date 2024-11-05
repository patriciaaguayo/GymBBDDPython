from paqueteGymBD.GestionAparatos import GestionAparatos
from paqueteGymBD.GestionClientes import GestionClientes
import datetime

from paqueteGymBD.GestionReservas import GestionReservas

""" Función para comprobar si una fecha es día entre semana """

def es_dia_laboral(fecha):
    dia_semana = datetime.datetime.strptime(fecha, "%Y-%m-%d").weekday()
    return dia_semana < 5  # 0-4 representan los días laborales (de lunes a viernes)

class Main:
    def __init__(self):

        self.gestionC = GestionClientes()
        self.gestionM = GestionAparatos()
        self.gestionR = GestionReservas()

    """ Funciones clientes """

    def imprimir_clientes(self):
        self.gestionC.imprimir_clientes()

    def lista_clientes_morosos(self):
        self.gestionC.imprimir_clientes_morosos()

    def lista_clientes_pagados(self):
        self.gestionC.imprimir_clientes_pagados()

    """ Funciones aparatos """

    def imprimir_aparatos(self):
        self.gestionM.imprimir_aparatos()

    """ Funciones reservas """

    def imprimir_reservas_fecha(self):
        while True:
            print("\n Introduce fecha (YYYY-MM-DD): ")
            fecha = input()

            try:
                fecha_obj = datetime.datetime.strptime(fecha, "%Y-%m-%d")

                if es_dia_laboral(fecha):
                    print(self.gestionR.imprimir_reservas_fecha(fecha))
                    break  # Salir del bucle si la fecha es válida y es día laboral
                else:
                    print("\n El gimnasio no abre los fines de semana. Por favor, elige otra fecha.")
            except ValueError:
                print("\n Fecha mal introducida. Por favor, introduce la fecha en formato YYYY-MM-DD.")


    """ Función para imprimir el menu principal """

    def menu(self):
        print("\n MENU PRINCIPAL GymForTheMoment")
        print("\n 1. Lista de todos los clientes")
        print(" 2. Lista de clientes pendientes")
        print(" 3. Lista de clientes pagados")
        print(" 4. Lista de todos los aparatos")
        print(" 5. Listar aparatos por fecha")
        print(" 6. Salir")
        return input("\n Opcion: ")

main = Main()

op = ""
while op != "6":
    op = main.menu()
    if op == "1":
        main.gestionC.listar_clientes()
        main.imprimir_clientes()

    elif op == "2":
        main.gestionC.listar_clientes()
        main.lista_clientes_morosos()

    elif op == "3":
        main.gestionC.listar_clientes()
        main.lista_clientes_pagados()

    elif op == "4":
        main.gestionM.listar_aparatos()
        main.imprimir_aparatos()

    elif op == "5":
        main.imprimir_reservas_fecha()

    elif op == "6":
        print("\n Gracias por usar nuestros servicios")
        break
    else:
        print("\n Opcion incorrecta")