"""
Archivo: main.py - 10 Simulaciones exigidas por la guía
Autor: Julio Cesar Martinez - Grupo 213023_432
Ejecuta: python main.py
"""
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reservas import Reserva

class ClientePrueba:
    def __init__(self, nombre): self.nombre = nombre

def main():
    open("registro_eventos.log","w",encoding="utf-8").write("--- Inicio simulaciones - Julio Cesar Martinez ---\n")
    print("=== SOFTWARE FJ - 10 SIMULACIONES - Julio Cesar Martinez ===\n")
    print("1. Sala válida")
    try:
        s1 = ReservaSala("S001","Sala Juntas A",80000,30,3)
        print("✅", s1.describir(), "| Con IVA:", f"${s1.calcular_costo_con_impuesto():,.0f}")
    except Exception as e: print("❌",e)
    print("\n2. Equipo válido")
    try:
        s2 = AlquilerEquipo("S002","Video Beam",60000,2,3)
        print("✅", s2.describir())
    except Exception as e: print("❌",e)
    print("\n3. Asesoría válida")
    try:
        s3 = AsesoriaEspecializada("S003","Asesoría Python",120000,4,"Avanzado")
        print("✅", s3.describir())
    except Exception as e: print("❌",e)
    print("\n4. Sala inválida (capacidad 0) - DEBE FALLAR")
    try:
        s_malo = ReservaSala("S004","Sala Mala",50000,0,2)
        print(s_malo.describir())
    except Exception as e: print("❌ Capturado correctamente:",e)
    print("\n5. Asesoría inválida (nivel Experto) - DEBE FALLAR")
    try:
        s_malo2 = AsesoriaEspecializada("S005","Asesoría",50000,2,"Experto")
        print(s_malo2.describir())
    except Exception as e: print("❌ Capturado:",e)
    print("\n6. Reserva exitosa - confirmar y procesar")
    c1 = ClientePrueba("Julio Cesar Martinez")
    try:
        r1 = Reserva("R001", c1, s1, 3)
        r1.confirmar()
        r1.procesar()
        print("✅", r1.describir())
    except Exception as e: print("❌",e)
    print("\n7. Reserva con servicio NO disponible - DEBE FALLAR")
    try:
        s2.disponible = False
        r2 = Reserva("R002", c1, s2, 2)
        r2.confirmar()
    except Exception as e: print("❌ Capturado:",e)
    finally: print("ℹ️ Sistema sigue activo (finally)")
    print("\n8. Procesar sin confirmar - DEBE FALLAR")
    try:
        r3 = Reserva("R003", c1, s3, 2)
        r3.procesar()
    except Exception as e:
        print("❌ Capturado:",e,"| Causa:",e.__cause__)
    print("\n9. Cancelar reserva y volver a cancelar")
    try:
        r4 = Reserva("R004", c1, s3, 2)
        r4.confirmar()
        r4.cancelar()
        r4.cancelar()
    except Exception as e: print("❌ Capturado (doble cancelación):",e)
    print("\n10. Polimorfismo y descuento inválido 80%")
    for s in [s1, s2, s3]:
        print("  -", s.describir())
    try:
        print(s1.calcular_costo_con_descuento(0.80))
    except Exception as e: print("❌ Capturado descuento inválido:",e)
    print("\n✅ 10 SIMULACIONES COMPLETADAS SIN QUE EL PROGRAMA SE CAIGA")
    print("📄 Revisa registro_eventos.log - Autor: Julio Cesar Martinez")

if __name__ == "__main__":
    main()