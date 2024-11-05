
class Aparatos:
    def __init__(self, codigo_aparato, aparato):
        self.aparato = aparato
        self.codigo_aparato = codigo_aparato

    def listarAparato(self):
        return "Código aparato: {} Aparato: {}".format(self.codigo_aparato,
                                                          self.aparato)

    def listaAparatosSinReserva(self):
        return ("Código aparato: {} Aparato: {} Estado: Libre").format(self.codigo_aparato, self.aparato)


