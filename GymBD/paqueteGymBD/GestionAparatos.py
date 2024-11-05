from paqueteGymBD.Conexion import Conexion, conexion
from paqueteGymBD.Aparatos import Aparatos

class GestionAparatos:
    def __init__(self):
        Conn= Conexion()
        self.conexion = Conn.conectar()
        self.aparatos = []

    """ Métodos para imprimir todos los aparatos """

    def listar_aparatos(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM Aparatos")
            aparatos_db = cursor.fetchall()
            self.aparatos = [Aparatos(codigo_aparato = aparato[0], aparato=aparato[1]) for aparato in
                             aparatos_db]

        except:
            print("\n Error al realizar consulta")

    def imprimir_aparatos(self):
        info = "\n\n Lista de aparatos: \n\n"
        for aparato in self.aparatos:
            info += " " + aparato.listarAparato() + "\n"
        print(info)