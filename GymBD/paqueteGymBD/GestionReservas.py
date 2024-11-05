from paqueteGymBD.Conexion import Conexion
from paqueteGymBD.Reservas import Reservas
from paqueteGymBD.Aparatos import Aparatos

class GestionReservas:
    def __init__(self):
        Conn= Conexion()
        self.conexion = Conn.conectar()
        self.reservas = []
        self.aparatos = []

    """ Métodos para listar todas las reservas """

    def listar_aparatos(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM Aparatos")
            aparatos_db = cursor.fetchall()
            self.aparatos = [Aparatos(codigo_aparato=aparato[0], aparato=aparato[1]) for aparato in
                             aparatos_db]

        except:
            print("\n Error al realizar consulta")

    def listar_reservas_fecha(self, fecha):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("select Reservas.codigo_aparato, Aparatos.nombre_maquina, "
                           "Reservas.codigo_cliente, Clientes.nombre_cliente, Reservas.fecha, "
                           "Reservas.hora from Reservas "
                           "inner join Clientes on Reservas.codigo_cliente = Clientes.codigo_cliente "
                           "inner join Aparatos on Reservas.codigo_aparato = Aparatos.codigo_aparato "
                           "where Reservas.fecha = %s", (fecha,))
            reservas_db = cursor.fetchall()
            self.reservas = [
                Reservas(codigo_aparato=reserva[0], aparato=reserva[1], codigo_cliente=reserva[2], cliente=reserva[3],
                         fecha=reserva[4], hora=reserva[5]) for
                reserva in reservas_db]

        except:
            print("\n Error al realizar consulta")

    def imprimir_reservas_fecha(self, fecha):

        info = "\n\n Lista de reservas en la fecha " + fecha + ": \n\n"

        # Listar reservas para la fecha especificada

        self.listar_reservas_fecha(fecha)
        for reserva in self.reservas:
            info += " " + reserva.listarReservas() + "\n"

        # Listar aparatos que no están reservados para la fecha especificada

        self.listar_aparatos()
        for aparato in self.aparatos:
            if aparato.codigo_aparato not in [reserva.codigo_aparato for reserva in self.reservas]:
                info += " " + aparato.listaAparatosSinReserva() + "\n"
        print(info)

        return ""

