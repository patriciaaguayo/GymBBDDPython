
class Reservas:
    def __init__(self, codigo_aparato, aparato, codigo_cliente, cliente, fecha, hora):
        self.codigo_aparato = codigo_aparato
        self.codigo_cliente = codigo_cliente
        self.aparato = aparato
        self.cliente = cliente
        self.fecha = fecha
        self.hora = hora

    def listarReservas(self):
        return ("Código aparato: {} Aparato: {} Codigo cliente: {}  Cliente: {} "
                " Fecha: {} Hora: {}").format(self.codigo_aparato, self.aparato,
                                                     self.codigo_cliente,self.cliente,
                                                     self.fecha, self.hora)

