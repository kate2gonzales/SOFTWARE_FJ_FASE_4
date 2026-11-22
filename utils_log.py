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
    """

    if tipo.upper() == "ERROR":
        logger.error(mensaje)
    else:
        logger.info(mensaje)