
from abc import ABC, abstractmethod
from excepciones import ErrorValidacion


class EntidadBase(ABC):
    """
    Clase abstracta que representa una entidad
    general del sistema Software FJ.
    """

    def __init__(self, identificador):
        if not isinstance(identificador, str) or not identificador.strip():
            raise ErrorValidacion(
                "El identificador es obligatorio."
            )

        self._identificador = identificador

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def validar(self):
        """Método que cada clase hija debe implementar."""
        pass
