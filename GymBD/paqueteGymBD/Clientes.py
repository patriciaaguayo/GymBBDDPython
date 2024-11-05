
class Clientes:
    def __init__(self, codigo_cliente, nombre, dni, mensualidad=None):
        self.nombre = nombre
        self.dni = dni
        self.mensualidad = mensualidad
        self.codigo_cliente = codigo_cliente

    def listarClientes(self):
        return "Código cliente: {} Nombre: {} DNI: {}".format(self.codigo_cliente,
                                                              self.nombre, self.dni)

    def listarClientesMensualidad(self):
        return "Código cliente: {} Nombre: {} DNI: {} Mensualidad {}".format(self.codigo_cliente,
                                                              self.nombre, self.dni, self.mensualidad)