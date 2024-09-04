#include <stdio.h>  // Incluye la biblioteca estándar de entrada/salida en C

#define MAX_LINE_LENGTH 1000  // Define una constante para la longitud máxima de una línea en el archivo

// Función que cuenta las coincidencias de la palabra clave en el archivo
int contarCoincidencias(FILE *archivo, const char *clave) {
    char linea[MAX_LINE_LENGTH];  // Arreglo para almacenar cada línea del archivo
    int cuenta = 0;  // Inicializa el contador de coincidencias en 0
    int i, j, clave_len = 0;

    // Calcula la longitud de la palabra clave manualmente
    while (clave[clave_len] != '\0') {
        clave_len++;
    }

    // Lee cada línea del archivo hasta que se llegue al final
    while (fgets(linea, MAX_LINE_LENGTH, archivo) != NULL) {
        // Recorre la línea para buscar coincidencias con la palabra clave
        for (i = 0; linea[i] != '\0'; i++) {
            for (j = 0; j < clave_len && linea[i + j] == clave[j]; j++);

            // Si se encuentra una coincidencia completa, incrementa el contador
            if (j == clave_len) {
                cuenta++;
            }
        }
    }

    return cuenta;  // Retorna el número total de coincidencias encontradas
}

int main(int argc, char *argv[]) {
    // Verifica si el programa fue llamado con el número correcto de argumentos
    if (argc != 3) {
        printf("Uso: %s archivo clave\n", argv[0]);  // Muestra un mensaje de uso correcto si no se proporcionaron 2 argumentos
        return 1;  // Termina el programa con un código de error
    }

    // Intenta abrir el archivo proporcionado en modo de lectura
    FILE *archivo = fopen(argv[1], "r");
    if (archivo == NULL) {
        printf("No se pudo abrir el archivo %s\n", argv[1]);  // Muestra un mensaje de error si no se puede abrir el archivo
        return 1;  // Termina el programa con un código de error
    }

    const char *clave = argv[2];  // Almacena el segundo argumento (la palabra clave) en la variable 'clave'
    int coincidencias = contarCoincidencias(archivo, clave);  // Llama a la función para contar coincidencias
    fclose(archivo);  // Cierra el archivo

    // Muestra el número de veces que la palabra clave se repite en el texto
    printf("La palabra '%s' se repite %d veces en el texto.\n", clave, coincidencias);
    return 0;  // Termina el programa exitosamente
}
