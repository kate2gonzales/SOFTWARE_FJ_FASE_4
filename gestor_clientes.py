from clientes import Cliente
from excepciones import ErrorCliente


class GestorClientes:
    """
    Administra el registro y la búsqueda de clientes
    del sistema Software FJ.
    """

    def __init__(self):
        self.clientes = []

    def registrar_cliente(self, cliente):

        if not isinstance(cliente, Cliente):
            raise ErrorCliente(
                "El objeto ingresado no corresponde a un cliente."
            )

        for cliente_existente in self.clientes:
            if cliente_existente.documento == cliente.documento:
                raise ErrorCliente(
                    "Ya existe un cliente con ese documento."
                )

        self.clientes.append(cliente)
        return True

    def buscar_cliente(self, documento):

        for cliente in self.clientes:
            if cliente.documento == documento:
                return cliente

        raise ErrorCliente(
            "No se encontró un cliente con ese documento."
        )

    def listar_clientes(self):
        return self.clientes.copy()