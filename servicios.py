"""
Archivo: servicios.py
Autor: Julio Cesar Martinez - Grupo 213023_432
Curso: Programación 213023 - UNAD - Fase 4
Descripción: Clase abstracta Servicio y los tres servicios
especializados: ReservaSala, AlquilerEquipo y AsesoriaEspecializada.
Aplica: Abstracción, Herencia, Polimorfismo, Encapsulación y
métodos sobrecargados.
"""

from abc import ABC, abstractmethod

try:
    from excepciones import DatosInvalidosError, ServicioNoDisponibleError, CalculoInconsistenteError
    from utils_log import registrar_log
except ImportError:
    class DatosInvalidosError(Exception): pass
    class ServicioNoDisponibleError(Exception): pass
    class CalculoInconsistenteError(Exception): pass
    def registrar_log(tipo, mensaje):
        with open("registro_eventos.log", "a", encoding="utf-8") as f:
            f.write(f"[{tipo}] {mensaje}\n")

class Servicio(ABC):
    """Clase abstracta que representa un servicio general de Software FJ."""
    def __init__(self, id_servicio, nombre, precio_base, disponible=True):
        if not id_servicio:
            raise DatosInvalidosError("El ID del servicio no puede estar vacío")
        if precio_base is None or precio_base < 0:
            raise DatosInvalidosError("El precio base no puede ser negativo o nulo")
        self._id = id_servicio
        self._nombre = nombre
        self._precio_base = float(precio_base)
        self._disponible = disponible

    @property
    def id(self): return self._id
    @property
    def nombre(self): return self._nombre
    @property
    def precio_base(self): return self._precio_base
    @property
    def disponible(self): return self._disponible

    @disponible.setter
    def disponible(self, valor):
        self._disponible = bool(valor)

    @abstractmethod
    def calcular_costo(self, *args, **kwargs):
        """Cada hija lo implementa diferente = POLIMORFISMO"""
        pass

    @abstractmethod
    def validar_parametros(self):
        pass

    @abstractmethod
    def describir(self):
        pass

    def calcular_costo_con_impuesto(self, impuesto=0.19):
        """Variante 1: costo + impuesto (19% IVA Colombia)"""
        try:
            if impuesto < 0:
                raise CalculoInconsistenteError("El impuesto no puede ser negativo")
            return self.calcular_costo() * (1 + impuesto)
        except Exception as e:
            registrar_log("ERROR", f"Error en calcular_costo_con_impuesto: {e}")
            raise CalculoInconsistenteError("Fallo cálculo con impuesto") from e

    def calcular_costo_con_descuento(self, descuento=0.0):
        """Variante 2: costo con descuento (0 a 0.5)"""
        if descuento < 0 or descuento > 0.5:
            raise CalculoInconsistenteError("Descuento debe estar entre 0 y 0.5")
        return self.calcular_costo() * (1 - descuento)

    def calcular_costo_total(self, impuesto=0.19, descuento=0.0):
        """Variante 3: costo con impuesto Y descuento"""
        costo = self.calcular_costo() * (1 - descuento)
        return costo * (1 + impuesto)

class ReservaSala(Servicio):
    """Servicio de reserva de salas de reuniones"""
    def __init__(self, id_servicio, nombre, precio_base, capacidad, horas, disponible=True):
        super().__init__(id_servicio, nombre, precio_base, disponible)
        self.capacidad = capacidad
        self.horas = horas
        self.validar_parametros()

    def validar_parametros(self):
        if self.capacidad <= 0:
            raise DatosInvalidosError("La capacidad de la sala debe ser mayor a 0")
        if self.horas <= 0 or self.horas > 12:
            raise DatosInvalidosError("Las horas deben estar entre 1 y 12")

    def calcular_costo(self, *args, **kwargs):
        descuento = kwargs.get("descuento", 0)
        costo = self._precio_base * self.horas
        if self.capacidad > 50:
            costo += 50000
        return costo * (1 - descuento)

    def describir(self):
        return f"🏢 SALA: {self._nombre} | Capacidad: {self.capacidad} | {self.horas}h | ${self.calcular_costo():,.0f}"

class AlquilerEquipo(Servicio):
    """Servicio de alquiler de equipos"""
    def __init__(self, id_servicio, nombre, precio_base, cantidad, dias, disponible=True):
        super().__init__(id_servicio, nombre, precio_base, disponible)
        self.cantidad = cantidad
        self.dias = dias
        self.validar_parametros()

    def validar_parametros(self):
        if self.cantidad <= 0:
            raise DatosInvalidosError("La cantidad de equipos debe ser mayor a 0")
        if self.dias <= 0 or self.dias > 30:
            raise DatosInvalidosError("Los días deben estar entre 1 y 30")

    def calcular_costo(self, *args, **kwargs):
        descuento = kwargs.get("descuento", 0)
        costo = self._precio_base * self.cantidad * self.dias
        if self.dias >= 7:
            costo *= 0.9
        return costo * (1 - descuento)

    def describir(self):
        return f"💻 EQUIPO: {self._nombre} | Cant: {self.cantidad} | {self.dias} días | ${self.calcular_costo():,.0f}"

class AsesoriaEspecializada(Servicio):
    """Servicio de asesoría especializada"""
    def __init__(self, id_servicio, nombre, precio_base, horas_asesoria, nivel, disponible=True):
        super().__init__(id_servicio, nombre, precio_base, disponible)
        self.horas_asesoria = horas_asesoria
        self.nivel = nivel
        self.validar_parametros()

    def validar_parametros(self):
        if self.horas_asesoria <= 0:
            raise DatosInvalidosError("Las horas de asesoría deben ser > 0")
        if self.nivel not in ["Básico", "Intermedio", "Avanzado"]:
            raise DatosInvalidosError("Nivel debe ser Básico, Intermedio o Avanzado")

    def calcular_costo(self, *args, **kwargs):
        descuento = kwargs.get("descuento", 0)
        multiplicador = {"Básico": 1.0, "Intermedio": 1.3, "Avanzado": 1.6}[self.nivel]
        return self._precio_base * self.horas_asesoria * multiplicador * (1 - descuento)

    def describir(self):
        return f"🎓 ASESORÍA: {self._nombre} | Nivel: {self.nivel} | {self.horas_asesoria}h | ${self.calcular_costo():,.0f}"