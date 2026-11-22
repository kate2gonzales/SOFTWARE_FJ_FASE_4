
from entidades import EntidadBase
from excepciones import ErrorValidacion


class Cliente(EntidadBase):
    """
    Representa un cliente del sistema Software FJ.
    """

    def __init__(self, identificador, nombre, documento, correo, telefono):
        super().__init__(identificador)

        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo
        self.__telefono = telefono

        self.validar()

    @property
    def nombre(self):
        return self.__nombre

    @property
    def documento(self):
        return self.__documento

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def validar(self):
        if not isinstance(self.__nombre, str) or not self.__nombre.strip():
            raise ErrorValidacion("El nombre del cliente es obligatorio.")

        if not isinstance(self.__documento, str) or not self.__documento.strip():
            raise ErrorValidacion("El documento del cliente es obligatorio.")

        if not isinstance(self.__correo, str):
            raise ErrorValidacion("El correo electrónico no es válido.")

        correo = self.__correo.strip()

        if (
            correo.count("@") != 1
            or " " in correo
            or correo.startswith("@")
            or correo.endswith("@")
            or "." not in correo.split("@")[1]
            or correo.split("@")[1].startswith(".")
            or correo.split("@")[1].endswith(".")
        ):
            raise ErrorValidacion("El correo electrónico no es válido.")

        if not isinstance(self.__telefono, str) or not self.__telefono.strip():
            raise ErrorValidacion("El teléfono del cliente es obligatorio.")

        return True
