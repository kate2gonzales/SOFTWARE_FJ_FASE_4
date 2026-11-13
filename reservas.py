"""
Archivo: reservas.py
Autor: Julio Cesar Martinez - Grupo 213023_432
Curso: Programación 213023 - UNAD - Fase 4
Descripción: Gestiona las reservas: creación, confirmación,
cancelación y procesamiento. Manejo avanzado de excepciones
con try/except/else/finally y encadenamiento.
"""
import traceback
from datetime import datetime

try:
    from excepciones import ReservaInvalidaError, ServicioNoDisponibleError, OperacionNoPermitidaError, CalculoInconsistenteError
    from utils_log import registrar_log
except ImportError:
    class ReservaInvalidaError(Exception): pass
    class ServicioNoDisponibleError(Exception): pass
    class OperacionNoPermitidaError(Exception): pass
    class CalculoInconsistenteError(Exception): pass
    def registrar_log(tipo, mensaje):
        with open("registro_eventos.log", "a", encoding="utf-8") as f:
            f.write(f"[{tipo}] {mensaje}\n")

class Reserva:
    """Reserva: integra Cliente + Servicio + duración + estado."""
    ESTADOS = ["Pendiente", "Confirmada", "Cancelada", "Procesada"]

    def __init__(self, id_reserva, cliente, servicio, duracion):
        if not id_reserva:
            raise ReservaInvalidaError("El ID de la reserva no puede estar vacío")
        if cliente is None or not hasattr(cliente, "nombre"):
            raise ReservaInvalidaError("La reserva requiere un Cliente válido")
        if servicio is None or not hasattr(servicio, "calcular_costo"):
            raise ReservaInvalidaError("La reserva requiere un Servicio válido")
        if duracion is None or duracion <= 0:
            raise ReservaInvalidaError("La duración debe ser mayor a 0")
        self._id = id_reserva
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = "Pendiente"
        self._costo_total = 0
        self._fecha = datetime.now()

    @property
    def id(self): return self._id
    @property
    def estado(self): return self._estado
    @property
    def cliente(self): return self._cliente
    @property
    def servicio(self): return self._servicio
    @property
    def costo_total(self): return self._costo_total

    def validar(self):
        if not self._servicio.disponible:
            raise ServicioNoDisponibleError(f"Servicio {self._servicio.nombre} no está disponible")

    def confirmar(self):
        try:
            self.validar()
            if self._estado != "Pendiente":
                raise OperacionNoPermitidaError(f"No se puede confirmar en estado {self._estado}")
            self._estado = "Confirmada"
            registrar_log("INFO", f"Reserva {self._id} confirmada para {self._cliente.nombre}")
            print(f"✅ Reserva {self._id} confirmada")
            return True
        except Exception as e:
            registrar_log("ERROR", f"Fallo confirmar {self._id}: {e}")
            raise

    def cancelar(self):
        try:
            if self._estado == "Cancelada":
                raise OperacionNoPermitidaError("La reserva ya está cancelada")
            if self._estado == "Procesada":
                raise OperacionNoPermitidaError("No se puede cancelar una reserva ya procesada")
            self._estado = "Cancelada"
            registrar_log("INFO", f"Reserva {self._id} cancelada")
            print(f"🚫 Reserva {self._id} cancelada")
            return True
        except Exception as e:
            registrar_log("ERROR", f"Fallo cancelar {self._id}: {e}")
            raise

    def procesar(self):
        print(f"\n🔄 Procesando reserva {self._id}...")
        try:
            if self._estado != "Confirmada":
                raise ReservaInvalidaError(f"Solo se procesa si está Confirmada. Estado: {self._estado}")
            if not self._servicio.disponible:
                raise ServicioNoDisponibleError("Servicio no disponible al procesar")
            self._costo_total = self._servicio.calcular_costo()
            if self._costo_total <= 0:
                raise CalculoInconsistenteError("Costo calculado inconsistente (<=0)")
        except (ReservaInvalidaError, ServicioNoDisponibleError, CalculoInconsistenteError) as e:
            registrar_log("ERROR", f"Error procesando {self._id}: {e}\n{traceback.format_exc()}")
            print(f"❌ Error al procesar: {e}")
            raise ReservaInvalidaError(f"No se pudo procesar {self._id}") from e
        else:
            self._estado = "Procesada"
            registrar_log("INFO", f"Reserva {self._id} procesada - ${self._costo_total:,.0f}")
            print(f"✅ Procesada. Costo: ${self._costo_total:,.0f}")
            return self._costo_total
        finally:
            print(f"ℹ️ Fin procesamiento {self._id} - Estado: {self._estado}")
            registrar_log("INFO", f"Fin procesamiento {self._id} - Estado: {self._estado}")

    def describir(self):
        return f"Reserva [{self._id}] Cliente: {self._cliente.nombre} | Servicio: {self._servicio.nombre} | Duración: {self._duracion} | Estado: {self._estado} | Costo: ${self._costo_total:,.0f}"