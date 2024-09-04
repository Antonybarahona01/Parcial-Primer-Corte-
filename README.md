# Parcial Primer Corte

---

# Informe del Proyecto

## 1. Implementación de Expresiones Lambda en Python

### Descripción

Para demostrar el uso de funciones lambda en Python, se desarrolló un programa en Python que evalúa expresiones lambda que definen funciones matemáticas básicas. En particular, se implementaron funciones para calcular seno, coseno y tangente de ángulos dados en radianes.

### Proceso

1. **Definición de Gramática Regular**: Se definió una gramática regular para analizar expresiones que contienen funciones trigonométricas.
2. **Implementación en LEX**: Se escribió un archivo `.l` para analizar las expresiones trigonométricas.
3. **Generación y Pruebas**: Se generó el archivo de análisis y se realizaron pruebas utilizando un archivo de texto con varias expresiones trigonométricas.

### Resultados

Se comprobaron varias expresiones trigonométricas y se validó el análisis correcto y el resultado esperado para cada caso.

## 2. Comparación de Rendimiento entre C y Python

### Descripción

Se comparó el rendimiento de dos programas: uno en C y otro en Python, ambos implementando el cálculo de secuencias de Collatz. La comparación se basó en el tiempo de ejecución para diferentes entradas.

### Proceso

1. **Implementación en C**: Se desarrolló un programa en C para calcular la secuencia de Collatz.
2. **Implementación en Python**: Se desarrolló un programa equivalente en Python.
3. **Ejecución y Medición**: Se ejecutaron ambos programas con varias entradas utilizando el comando `time` para medir el tiempo de ejecución en la terminal.

### Resultados

Se observó que el programa en C generalmente tiene un tiempo de ejecución menor en comparación con el programa en Python, lo que refleja la eficiencia de los lenguajes compilados sobre los interpretados en este contexto.

## 3. Búsqueda de Palabras Repetidas en C

### Descripción

Se desarrolló un programa en C que busca y cuenta palabras repetidas en un archivo de texto. El programa lee el archivo, identifica palabras repetidas y muestra el resultado.

### Proceso

1. **Desarrollo del Programa en C**: Se escribió un programa en C para abrir un archivo de texto, leer su contenido, y contar las repeticiones de palabras.
2. **Pruebas y Resultados**: Se probaron diferentes archivos de texto para verificar la precisión del conteo de palabras repetidas y asegurar el funcionamiento correcto del programa.

### Resultados

El programa identificó y contó con éxito las palabras repetidas en los archivos de texto proporcionados, mostrando resultados precisos y confiables.

## 4. Implementación de Calculador de Funciones Trigonométricas con ANTLR y Python

### Descripción

Este proyecto utiliza ANTLR y Python para crear un calculador de funciones trigonométricas que evalúa las expresiones `Sin`, `Cos` y `Tan` en radianes.

### Requisitos

- **Java**: Necesario para ejecutar ANTLR.
- **ANTLR**: Se utiliza ANTLR 4.9.2 para la generación de los archivos de análisis.
- **Python**: Se utiliza Python 3.x para el procesamiento.
- **ANTLR Python Runtime**: Debe ser compatible con ANTLR 4.9.2.

### Instalación y Configuración

1. **Instalar Java**

   Asegúrate de que Java esté instalado en tu sistema. Puedes verificar la instalación ejecutando el comando `java -version`. Si Java no está instalado, descárgalo e instálalo desde la [página oficial de Java](https://www.java.com/download/).

2. **Descargar ANTLR**

   Descarga ANTLR 4.9.2 desde la [página oficial de ANTLR](https://www.antlr.org/download.html). Guarda el archivo `antlr-4.9.2-complete.jar` en un directorio de tu elección.

3. **Configurar ANTLR**

   Configura el `CLASSPATH` y crea un alias para ANTLR. Ajusta la ruta según donde guardaste el archivo JAR. Puedes establecer el CLASSPATH con el comando `export CLASSPATH="~/path/to/antlr-4.9.2-complete.jar:$CLASSPATH"` y crear un alias con `alias antlr4='java -jar ~/path/to/antlr-4.9.2-complete.jar'`.

4. **Instalar el Runtime de ANTLR para Python**

   Desinstala cualquier versión anterior del runtime de ANTLR para Python e instala la versión correcta. Utiliza el comando `pip3 uninstall antlr4-python3-runtime` para desinstalar y `pip3 install antlr4-python3-runtime==4.9.2` para instalar la versión correcta.

5. **Crear la Gramática ANTLR**

   Crea un archivo con la gramática ANTLR para las funciones trigonométricas. Esta gramática define cómo se deben interpretar las expresiones `Sin`, `Cos` y `Tan`.

6. **Generar Archivos de Código con ANTLR**

   Utiliza ANTLR para generar los archivos de código necesarios basados en la gramática que has definido.

7. **Crear el Script Python**

   Desarrolla un script en Python que utilice los archivos generados por ANTLR para leer las expresiones desde un archivo de texto y calcular los resultados.

8. **Crear el Archivo de Entrada**

   Crea un archivo de entrada con las expresiones trigonométricas que deseas calcular. Este archivo será procesado por el script Python.

9. **Ejecutar el Programa**

   Ejecuta el script Python con el archivo de entrada para obtener los resultados de las funciones trigonométricas.

### Notas

- **Compatibilidad de Versiones**: Asegúrate de que la versión del runtime de ANTLR para Python (4.9.2) sea compatible con la versión de ANTLR utilizada (4.9.2).
- **Errores Comunes**: Verifica que no haya desajustes entre la gramática y el código generado. La desinstalación y reinstalación del runtime puede resolver problemas de compatibilidad.

### Archivos en el Repositorio

Todos los archivos necesarios para la implementación, incluyendo la gramática ANTLR, el script Python y el archivo de entrada, se encuentran en este repositorio.

