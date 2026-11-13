# Software-FJ - Sistema de Reservas de Servicios

**Autor:** Julio Cesar Martinez
**Grupo:** 213023_432
**Curso:** Programación 213023 - UNAD
**Fase:** Fase 4 - Programación Orientada a Objetos

## Descripción del Proyecto
Sistema para gestionar reservas de servicios de una empresa.
Permite reservar salas, alquilar equipos y contratar asesorías especializadas,
calculando el costo total de cada servicio de forma automática.

## Estructura del Proyecto
- `servicios.py` - Clase abstracta `Servicio` y los 3 servicios: `ReservaSala`, `AlquilerEquipo` y `AsesoriaEspecializada`
- `reservas.py` - Clase `Reserva` que une un cliente con un servicio
- `main.py` - 10 simulaciones exigidas por la guía

## Conceptos de POO Aplicados
- **Abstracción:** Clase abstracta `Servicio` con método `calcular_costo()`
- **Herencia:** Los 3 servicios heredan de `Servicio`
- **Polimorfismo:** Cada servicio calcula su costo a su manera
- **Encapsulación:** Atributos privados con `_` y métodos para manejarlos

## Cómo Ejecutar
1. Abrir la carpeta en Visual Studio Code
2. En la terminal escribir:
```bash
python main.py