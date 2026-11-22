
"""
Archivo: simulaciones_companero.py
Autor: Julio Cesar Martinez - Grupo 213023_432
Descripción: Diez simulaciones para validar el funcionamiento
del sistema de reservas de servicios.
"""

from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reservas import Reserva
from utils_log import registrar_log
from clientes import Cliente
from gestor_clientes import GestorClientes





def main():
        # PRUEBAS DE CLIENTES
    print("=== PRUEBAS DE REGISTRO DE CLIENTES ===")

    gestor = GestorClientes()

    # PRUEBA 1: Cliente válido
    try:
        cliente_valido = Cliente(
            "C001",
            "Julio Cesar Martinez",
            "123456789",
            "julio@gmail.com",
            "3001234567"
        )

        gestor.registrar_cliente(cliente_valido)

        print("Cliente válido registrado correctamente.")
        registrar_log(
            "Cliente válido registrado correctamente.",
            "INFO"
        )

    except Exception as e:
        print("Error al registrar cliente válido:", e)
        registrar_log(
            f"Error al registrar cliente válido: {e}",
            "ERROR"
        )

    # PRUEBA 2: Cliente con correo inválido
    try:
        cliente_invalido = Cliente(
            "C002",
            "Cliente de prueba",
            "987654321",
            "correo_invalido",
            "3009876543"
        )

        gestor.registrar_cliente(cliente_invalido)

        print("ERROR: Se aceptó un cliente con correo inválido.")

    except Exception as e:
        print("Cliente inválido rechazado correctamente:", e)
        registrar_log(
            f"Cliente inválido rechazado correctamente: {e}",
            "INFO"
        )

    # PRUEBA 3: Documento duplicado
    try:
        cliente_duplicado = Cliente(
            "C003",
            "Otro cliente",
            "123456789",
            "otro@gmail.com",
            "3005555555"
        )

        gestor.registrar_cliente(cliente_duplicado)

        print("ERROR: Se aceptó un documento duplicado.")

    except Exception as e:
        print("Documento duplicado rechazado correctamente:", e)
        registrar_log(
            f"Documento duplicado rechazado correctamente: {e}",
            "INFO"
        )

    print("=== FIN DE PRUEBAS DE CLIENTES ===\\n")

    registrar_log("=== Inicio de las diez simulaciones ===", "INFO")

    print("=== SOFTWARE FJ - 10 SIMULACIONES - Julio Cesar Martinez ===\n")

    # SIMULACIÓN 1: Sala válida
    print("1. Sala válida")
    try:
        s1 = ReservaSala("S001", "Sala Juntas A", 80000, 30, 3)
        print("Sala creada:", s1.describir())
        print("Con IVA:", f"${s1.calcular_costo_con_impuesto():,.0f}")
        registrar_log("Simulación 1: Sala creada y costo con IVA calculado correctamente.", "INFO")
    except Exception as e:
        print("Error:", e)
        registrar_log(f"Simulación 1: Error al crear la sala: {e}", "ERROR")

    # SIMULACIÓN 2: Equipo válido
    print("\n2. Equipo válido")
    try:
        s2 = AlquilerEquipo("S002", "Video Beam", 60000, 2, 3)
        print("Equipo creado:", s2.describir())
        registrar_log("Simulación 2: Equipo creado correctamente.", "INFO")
    except Exception as e:
        print("Error:", e)
        registrar_log(f"Simulación 2: Error al crear el equipo: {e}", "ERROR")

    # SIMULACIÓN 3: Asesoría válida
    print("\n3. Asesoría válida")
    try:
        s3 = AsesoriaEspecializada("S003", "Asesoría Python", 120000, 4, "Avanzado")
        print("Asesoría creada:", s3.describir())
        registrar_log("Simulación 3: Asesoría especializada creada correctamente.", "INFO")
    except Exception as e:
        print("Error:", e)
        registrar_log(f"Simulación 3: Error al crear la asesoría: {e}", "ERROR")

    # SIMULACIÓN 4: Sala inválida
    print("\n4. Sala inválida (capacidad 0) - DEBE FALLAR")
    try:
        s_malo = ReservaSala("S004", "Sala Mala", 50000, 0, 2)
        print(s_malo.describir())
        registrar_log("Simulación 4: No se detectó la capacidad inválida de la sala.", "ERROR")
    except Exception as e:
        print("Error capturado correctamente:", e)
        registrar_log(f"Simulación 4: Capacidad inválida detectada correctamente: {e}", "INFO")

    # SIMULACIÓN 5: Asesoría inválida
    print("\n5. Asesoría inválida (nivel Experto) - DEBE FALLAR")
    try:
        s_malo2 = AsesoriaEspecializada("S005", "Asesoría", 50000, 2, "Experto")
        print(s_malo2.describir())
        registrar_log("Simulación 5: No se detectó el nivel de asesoría inválido.", "ERROR")
    except Exception as e:
        print("Error capturado:", e)
        registrar_log(f"Simulación 5: Nivel de asesoría inválido detectado correctamente: {e}", "INFO")

    # SIMULACIÓN 6: Reserva exitosa
    print("\n6. Reserva exitosa - confirmar y procesar")
    c1 = Cliente(
    "C010",
    "Julio Cesar Martinez",
    "123456789",
    "julio@gmail.com",
    "3001234567"
)
    try:
        r1 = Reserva("R001", c1, s1, 3)
        r1.confirmar()
        r1.procesar()
        print(r1.describir())
        registrar_log("Simulación 6: Reserva confirmada y procesada correctamente.", "INFO")
    except Exception as e:
        print("Error:", e)
        registrar_log(f"Simulación 6: Error al confirmar o procesar la reserva: {e}", "ERROR")

    # SIMULACIÓN 7: Servicio no disponible
    print("\n7. Reserva con servicio NO disponible - DEBE FALLAR")
    try:
        s2.disponible = False
        r2 = Reserva("R002", c1, s2, 2)
        r2.confirmar()
        registrar_log("Simulación 7: No se detectó el servicio no disponible.", "ERROR")
    except Exception as e:
        print("Error capturado:", e)
        registrar_log(f"Simulación 7: Servicio no disponible detectado correctamente: {e}", "INFO")
    finally:
        print("Sistema sigue activo (finally)")
        registrar_log("Simulación 7: Bloque finally ejecutado; sistema continúa activo.", "INFO")

    # SIMULACIÓN 8: Procesar sin confirmar
    print("\n8. Procesar sin confirmar - DEBE FALLAR")
    try:
        r3 = Reserva("R003", c1, s3, 2)
        r3.procesar()
        registrar_log("Simulación 8: No se detectó el intento de procesar una reserva pendiente.", "ERROR")
    except Exception as e:
        print("Error capturado:", e, "| Causa:", e.__cause__)
        registrar_log(f"Simulación 8: Intento de procesar reserva pendiente detectado correctamente: {e}", "INFO")

    # SIMULACIÓN 9: Doble cancelación
    print("\n9. Cancelar reserva y volver a cancelar")
    try:
        r4 = Reserva("R004", c1, s3, 2)
        r4.confirmar()
        r4.cancelar()
        r4.cancelar()
        registrar_log("Simulación 9: No se detectó la doble cancelación.", "ERROR")
    except Exception as e:
        print("Error capturado (doble cancelación):", e)
        registrar_log(f"Simulación 9: Doble cancelación detectada correctamente: {e}", "INFO")

    # SIMULACIÓN 10: Polimorfismo y descuento inválido
    print("\n10. Polimorfismo y descuento inválido 80%")
    try:
        for servicio in [s1, s2, s3]:
            print("-", servicio.describir())
        registrar_log("Simulación 10: Polimorfismo comprobado en los tres servicios.", "INFO")
    except Exception as e:
        print("Error en polimorfismo:", e)
        registrar_log(f"Simulación 10: Error en polimorfismo: {e}", "ERROR")

    try:
        print(s1.calcular_costo_con_descuento(0.80))
        registrar_log("Simulación 10: No se detectó el descuento inválido.", "ERROR")
    except Exception as e:
        print("Error capturado (descuento inválido):", e)
        registrar_log(f"Simulación 10: Descuento inválido detectado correctamente: {e}", "INFO")

    registrar_log("=== Finalizaron las diez simulaciones ===", "INFO")

    print("\n10 SIMULACIONES COMPLETADAS")
    print("Revisa el archivo sistema.log")


if __name__ == "__main__":
    main()
