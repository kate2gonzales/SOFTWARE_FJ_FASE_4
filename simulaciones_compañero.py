"""
Archivo: simulaciones_companero.py
Autor: Julio Cesar Martinez - Grupo 213023_432
Descripción: Diez simulaciones para validar el funcionamiento
del sistema de reservas de servicios.
"""

from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reservas import Reserva


class ClientePrueba:
    def __init__(self, nombre):
        self.nombre = nombre


def main():
    with open("registro_eventos.log", "w", encoding="utf-8") as archivo:
        archivo.write("--- Inicio simulaciones - Julio Cesar Martinez ---\n")

    print("=== SOFTWARE FJ - 10 SIMULACIONES - Julio Cesar Martinez ===\n")

    print("1. Sala válida")
    try:
        s1 = ReservaSala("S001", "Sala Juntas A", 80000, 30, 3)
        print("Sala creada:", s1.describir())
        print("Con IVA:", f"${s1.calcular_costo_con_impuesto():,.0f}")
    except Exception as e:
        print("Error:", e)

    print("\n2. Equipo válido")
    try:
        s2 = AlquilerEquipo("S002", "Video Beam", 60000, 2, 3)
        print("Equipo creado:", s2.describir())
    except Exception as e:
        print("Error:", e)

    print("\n3. Asesoría válida")
    try:
        s3 = AsesoriaEspecializada(
            "S003", "Asesoría Python", 120000, 4, "Avanzado"
        )
        print("Asesoría creada:", s3.describir())
    except Exception as e:
        print("Error:", e)

    print("\n4. Sala inválida (capacidad 0) - DEBE FALLAR")
    try:
        s_malo = ReservaSala("S004", "Sala Mala", 50000, 0, 2)
        print(s_malo.describir())
    except Exception as e:
        print("Error capturado correctamente:", e)

    print("\n5. Asesoría inválida (nivel Experto) - DEBE FALLAR")
    try:
        s_malo2 = AsesoriaEspecializada(
            "S005", "Asesoría", 50000, 2, "Experto"
        )
        print(s_malo2.describir())
    except Exception as e:
        print("Error capturado:", e)

    print("\n6. Reserva exitosa - confirmar y procesar")
    c1 = ClientePrueba("Julio Cesar Martinez")

    try:
        r1 = Reserva("R001", c1, s1, 3)
        r1.confirmar()
        r1.procesar()
        print(r1.describir())
    except Exception as e:
        print("Error:", e)

    print("\n7. Reserva con servicio NO disponible - DEBE FALLAR")
    try:
        s2.disponible = False
        r2 = Reserva("R002", c1, s2, 2)
        r2.confirmar()
    except Exception as e:
        print("Error capturado:", e)
    finally:
        print("Sistema sigue activo (finally)")

    print("\n8. Procesar sin confirmar - DEBE FALLAR")
    try:
        r3 = Reserva("R003", c1, s3, 2)
        r3.procesar()
    except Exception as e:
        print("Error capturado:", e, "| Causa:", e.__cause__)

    print("\n9. Cancelar reserva y volver a cancelar")
    try:
        r4 = Reserva("R004", c1, s3, 2)
        r4.confirmar()
        r4.cancelar()
        r4.cancelar()
    except Exception as e:
        print("Error capturado (doble cancelación):", e)

    print("\n10. Polimorfismo y descuento inválido 80%")
    for servicio in [s1, s2, s3]:
        print("-", servicio.describir())

    try:
        print(s1.calcular_costo_con_descuento(0.80))
    except Exception as e:
        print("Error capturado (descuento inválido):", e)

    print("\n10 SIMULACIONES COMPLETADAS")
    print("Revisa el archivo registro_eventos.log")


if __name__ == "__main__":
    main()