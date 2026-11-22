from clientes import Cliente

from excepciones import (
    ErrorValidacion,
    ErrorCliente,
    DatosInvalidosError,
    ServicioNoDisponibleError,
    ReservaInvalidaError,
    OperacionNoPermitidaError,
    CalculoInconsistenteError
)
from gestor_clientes import GestorClientes
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reservas import Reserva
from utils_log import registrar_log

try:
    cliente1 = Cliente(
        "C001",
        "María Pérez",
        "123456789",
        "maria@gmail.com",
        "3001234567"
    )

    print("Cliente registrado correctamente.")
    print("Nombre:", cliente1.nombre)
    print("Documento:", cliente1.documento)

except ErrorValidacion as error:
    print("No fue posible registrar el cliente:", error)

print("\n--- PRUEBA DE CLIENTE CON DATOS INCORRECTOS ---")

try:
    cliente2 = Cliente(
        "C002",
        "Carlos Gómez",
        "987654321",
        "correo_incorrecto",
        "3109876543"
    )

    print("Cliente registrado correctamente.")

except ErrorValidacion as error:
    print("Error al registrar el cliente:", error)
    registrar_log("ERROR", f"Error al registrar cliente: {error}")

print("\n--- PRUEBA DE CLIENTE SIN NOMBRE ---")

try:
    cliente3 = Cliente(
        "C003",
        "",
        "456789123",
        "cliente@gmail.com",
        "3201234567"
    )

    print("Cliente registrado correctamente.")

except ErrorValidacion as error:
    print("Error al registrar el cliente:", error)
    registrar_log("ERROR", f"Error de validación de cliente: {error}")

print("\n--- PRUEBA DEL GESTOR DE CLIENTES ---")

gestor = GestorClientes()

try:
    gestor.registrar_cliente(cliente1)

    print("Cliente agregado al gestor correctamente.")

    cliente_buscado = gestor.buscar_cliente("123456789")

    print("Cliente encontrado:", cliente_buscado.nombre)

except ErrorCliente as error:
    print("Error en la gestión de clientes:", error)

print("\n--- PRUEBA DE LOS TRES SERVICIOS ---")

try:
    sala = ReservaSala(
        "S001", "Sala de reuniones", 50000, 10, 2
    )

    equipo = AlquilerEquipo(
        "E001", "Computador portátil", 20000, 2, 3
    )

    asesoria = AsesoriaEspecializada(
        "A001", "Asesoría informática", 80000, 2, "Intermedio"
    )

    print(sala.describir())
    print(equipo.describir())
    print(asesoria.describir())

    print("\nLos tres servicios fueron creados correctamente.")

except DatosInvalidosError as error:
    print("Error al crear un servicio:", error)

print("\n--- PRUEBA DE CREACIÓN Y CONFIRMACIÓN DE RESERVA ---")

try:
    reserva1 = Reserva(
        "R001",
        cliente1,
        sala,
        2
    )

    print("Reserva creada correctamente.")
    print(reserva1.describir())

    reserva1.confirmar()

except (ReservaInvalidaError, ServicioNoDisponibleError) as error:
    print("Error al crear o confirmar la reserva:", error)

print("\n--- PRUEBA DE PROCESAMIENTO DE RESERVA ---")

try:
    costo = reserva1.procesar()

    print("Costo final de la reserva:", costo)
    print("Estado final:", reserva1.estado)

except ReservaInvalidaError as error:
    print("No fue posible procesar la reserva:", error)

print("\n--- PRUEBA DE CANCELACIÓN DE RESERVA ---")

try:
    reserva2 = Reserva(
        "R002",
        cliente1,
        equipo,
        3
    )

    print("Segunda reserva creada correctamente.")

    reserva2.cancelar()

    print("Estado final:", reserva2.estado)

except (ReservaInvalidaError, OperacionNoPermitidaError) as error:
    print("Error al cancelar la reserva:", error)

print("\n--- PRUEBA DE CANCELACIÓN DE RESERVA PROCESADA ---")

try:
    reserva1.cancelar()

except OperacionNoPermitidaError as error:
    print("Error controlado correctamente:", error)
    print("Estado de la reserva:", reserva1.estado)

print("\n--- PRUEBA DE SERVICIO NO DISPONIBLE ---")

sala.disponible = False

try:
    reserva3 = Reserva(
        "R003",
        cliente1,
        sala,
        2
    )

    reserva3.confirmar()

except ServicioNoDisponibleError as error:
    print("Error controlado correctamente:", error)

finally:
    sala.disponible = True
    print("Disponibilidad de la sala restaurada.")

print("\n--- PRUEBA DE SERVICIO CON DATOS INCORRECTOS ---")

try:
    sala_incorrecta = ReservaSala(
        "S002",
        "Sala inválida",
        50000,
        0,
        2
    )

except DatosInvalidosError as error:
    print("Error controlado correctamente:", error)

print("\n--- PRUEBA DE RESERVA CON DURACIÓN INVÁLIDA ---")

try:
    reserva_incorrecta = Reserva(
        "R004",
        cliente1,
        equipo,
        0
    )

except ReservaInvalidaError as error:
    print("Error controlado correctamente:", error)
    registrar_log("ERROR", f"Reserva R004 inválida: {error}")

print("\n--- PRUEBA DE ENCADENAMIENTO DE EXCEPCIONES ---")

try:
    sala.calcular_costo_con_impuesto(-0.1)

except CalculoInconsistenteError as error:
    print("Excepción controlada:", error)
    print("Causa original:", error.__cause__)

print("\n--- PRUEBA DE CÁLCULOS DE COSTOS ---")

print("Costo con IVA:", sala.calcular_costo_con_impuesto())

print("Costo con descuento:", sala.calcular_costo_con_descuento(0.10))

print("Costo total con descuento e IVA:",
      sala.calcular_costo_total(0.19, 0.10))