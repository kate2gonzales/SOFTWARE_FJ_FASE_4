# Software-FJ – Sistema de Reservas de Servicios

**Autor:** Julio Cesar Martinez  y Wendy tatiana coquinche gonzales
**Grupo:** 213023_432  
**Curso:** Programación 213023 – UNAD  
**Fase:** Fase 4 – Programación Orientada a Objetos

## 1. Descripción del proyecto

Software-FJ es un sistema desarrollado en Python para gestionar reservas de servicios de una empresa. Permite administrar clientes, realizar reservas de diferentes servicios y calcular automáticamente sus costos.

El sistema contempla servicios como reserva de salas, alquiler de equipos y asesorías especializadas. Además, incorpora validaciones, manejo de excepciones y registro de eventos para contribuir al correcto funcionamiento del programa.

## 2. Objetivos del proyecto

- Aplicar los principios de la Programación Orientada a Objetos (POO).
- Gestionar clientes y reservas de servicios.
- Implementar validaciones para controlar datos incorrectos.
- Calcular los costos de los servicios mediante métodos específicos.
- Realizar pruebas para verificar el funcionamiento y la estabilidad del sistema.

## 3. Estructura del proyecto

El proyecto está organizado en los siguientes archivos:

| Archivo | Descripción |
|---|---|
| `main.py` | Programa principal y pruebas de funcionamiento del sistema. |
| `servicios.py` | Clase abstracta `Servicio` y sus servicios derivados. |
| `reservas.py` | Clase `Reserva` y operaciones relacionadas con las reservas. |
| `clientes.py` | Definición de la clase `Cliente`. |
| `entidades.py` | Definición de entidades utilizadas en el sistema. |
| `gestor_clientes.py` | Gestión de los clientes registrados. |
| `excepciones.py` | Excepciones personalizadas para el manejo de errores. |
| `utils_log.py` | Funciones de apoyo para el registro de eventos. |
| `simulaciones_compañero.py` | Archivo complementario con diez simulaciones de validación. |

## 4. Conceptos de Programación Orientada a Objetos aplicados

- **Abstracción:** implementación de la clase abstracta `Servicio`, que define el método para calcular los costos.
- **Herencia:** las clases de los diferentes servicios heredan de la clase base `Servicio`.
- **Polimorfismo:** cada tipo de servicio implementa su propio comportamiento para calcular el costo.
- **Encapsulamiento:** utilización de atributos y métodos para controlar el acceso y la modificación de la información.

## 5. Ejecución del proyecto

Para ejecutar el sistema se deben seguir estos pasos:

1. Descargar o clonar el repositorio de GitHub.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Abrir una terminal dentro de la carpeta del proyecto.
4. Ejecutar el programa principal con el siguiente comando:

```bash
python main.py
```

Para ejecutar las diez simulaciones complementarias:

```bash
python simulaciones_compañero.py
```

## 6. Pruebas y validaciones

El proyecto incluye pruebas orientadas a comprobar el funcionamiento de los servicios, la gestión de clientes y las operaciones de reserva.

También contempla situaciones de error, validaciones de datos y manejo de excepciones, con el propósito de verificar la respuesta del sistema ante diferentes escenarios.

## 7. Repositorio del proyecto

El código fuente y los archivos del proyecto se encuentran disponibles en GitHub:

https://github.com/kate2gonzales/SOFTWARE_FJ_FASE_4

---

**Proyecto académico – Universidad Nacional Abierta y a Distancia (UNAD)**  
**Curso: Programación – Fase 4**
