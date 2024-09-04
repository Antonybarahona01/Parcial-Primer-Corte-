# Solicita al usuario que introduzca un número entero positivo
n = int(input("Introduce un número entero positivo: "))

# Verifica si el número es positivo
if n <= 0:
    print("Por favor, introduce un número entero positivo.")
else:
    # Imprime el número inicial
    print(f"Secuencia de Collatz para {n}:")
    pasos = 0 # Contador de pasos en la secuencia
    while n != 1: # Mientras el número no sea 1
        print(f"{n} -> ", end="") # Imprime el número actual seguido de "->" sin salto de línea
        if n % 2 == 0: # Si el número es par
            n = n // 2 # Divide el número por 2 (entero)
        else: # Si el número es impar
            n = 3 * n + 1 # Aplica la fórmula de Collatz
        pasos += 1 # Incrementa el contador de pasos
    print("1") # Imprime el último número de la secuencia (1)
    print(f"Secuencia completada en {pasos} pasos.") # Imprime el número total de pasos
