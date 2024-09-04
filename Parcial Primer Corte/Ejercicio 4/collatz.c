#include <stdio.h>  // Incluye la biblioteca estándar de entrada/salida
#include <stdlib.h> // Incluye la biblioteca estándar para funciones de utilidad

// Función principal
int main() {
    int n; // Variable para almacenar el número introducido por el usuario
    printf("Introduce un número entero positivo: ");
    scanf("%d", &n); // Lee el número entero desde la entrada estándar

    // Verifica si el número es positivo
    if (n <= 0) {
        printf("Por favor, introduce un número entero positivo.\n");
        return 1; // Sale del programa con código de error
    }

    // Imprime el número inicial
    printf("Secuencia de Collatz para %d:\n", n);
    int pasos = 0; // Contador de pasos en la secuencia
    while (n != 1) { // Mientras el número no sea 1
        printf("%d -> ", n); // Imprime el número actual seguido de "->"
        if (n % 2 == 0) { // Si el número es par
            n = n / 2; // Divide el número por 2
        } else { // Si el número es impar
            n = 3 * n + 1; // Aplica la fórmula de Collatz
        }
        pasos++; // Incrementa el contador de pasos
    }
    printf("1\n"); // Imprime el último número de la secuencia (1)
    printf("Secuencia completada en %d pasos.\n", pasos); // Imprime el número total de pasos

    return 0; // Sale del programa con éxito
}
