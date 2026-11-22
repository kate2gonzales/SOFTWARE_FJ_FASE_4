
class ErrorSoftwareFJ(Exception):
    """Excepción base del sistema Software FJ."""
    pass


class ErrorValidacion(ErrorSoftwareFJ):
    """Se produce cuando los datos ingresados no son válidos."""
    pass


class ErrorCliente(ErrorSoftwareFJ):
    """Se produce cuando ocurre un problema con un cliente."""
    pass


class ErrorServicio(ErrorSoftwareFJ):
    """Se produce cuando ocurre un problema con un servicio."""
    pass


class ServicioNoDisponible(ErrorServicio):
    """Se produce cuando un servicio no está disponible."""
    pass


class ErrorReserva(ErrorSoftwareFJ):
    """Se produce cuando una reserva no puede realizarse."""
    pass

class DatosInvalidosError(ErrorValidacion):
    """Error cuando los datos ingresados no son válidos."""
    pass


class ServicioNoDisponibleError(ServicioNoDisponible):
    """Error cuando un servicio no está disponible."""
    pass


class CalculoInconsistenteError(ErrorSoftwareFJ):
    """Error cuando un cálculo presenta inconsistencias."""
    pass


class ReservaInvalidaError(ErrorReserva):
    """Error cuando una reserva no cumple las condiciones."""
    pass


class OperacionNoPermitidaError(ErrorSoftwareFJ):
    """Error cuando una operación no está permitida."""
    pass