import logging


def configurar_logger():
    """
    Configura el registro de eventos y errores
    del sistema Software FJ.
    """

    logging.basicConfig(
        filename="sistema.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
    )

    return logging.getLogger("SoftwareFJ")


logger = configurar_logger()



def registrar_log(tipo, mensaje):
    """
    Registra eventos y errores del sistema.
    Acepta los argumentos en cualquiera de los dos órdenes.
    """

    if not isinstance(tipo, str) or not isinstance(mensaje, str):
        raise TypeError("El tipo y el mensaje del registro deben ser textos.")

    if tipo.upper() not in ("INFO", "ERROR") and mensaje.upper() in ("INFO", "ERROR"):
        tipo, mensaje = mensaje, tipo

    if tipo.upper() == "ERROR":
        logger.error(mensaje)
    else:
        logger.info(mensaje)
