# recuperatorio_primer_parcial
Recuperatorio primer parcial de Programación

---

## Descripción del Proyecto
Este programa es un menú interactivo que permite gestionar y analizar un nombre de usuario mediante diferentes herramientas lógicas y estadísticas. El sistema está diseñado de forma totalmente modular.

---

## Funcionalidades Implementadas
* **Opción 5 - Espejar Usuario:** Invierte el texto ingresado y lo concatena con el original.
* **Opción 6 - Reporte Estadístico:** Calcula la longitud, porcentajes de tipos de caracteres (letras, números, símbolos) y muestra los caracteres repetidos consecutivos en forma de bloques.
* **Opción 7 - Verificar Simetría:** Determina si la primera mitad del usuario es exactamente igual a la segunda mitad.
* **Opción 8 - Ordenar Caracteres:** Permite ordenar el nombre de usuario de manera ascendente o descendente según el código ASCII, utilizando un algoritmo de ordenamiento manual (Selection Sort).

---

## Estructura del Código (Modularización)
El proyecto está dividido en los siguientes módulos para un buen funcionamiento:

* **`main.py`:** Contiene la funcion que ejecuta el programa 
* **`menu.py`:** Contiene el bucle principal del menú interactivo y redirige las opciones.
* **`analisis.py`:** Aloja la lógica pura de los algoritmos (búsqueda de consecutivos, ordenamiento manual, verificación de simetría y funciones de inversión).
* **`validaciones.py`:** Se encarga de las funciones de control de ingreso de datos (como la validación del criterio de orden).
* **`utilidades.py`:** Concentra las funciones visuales y reportes unificados que se muestran por pantalla.