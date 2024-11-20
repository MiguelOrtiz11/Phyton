# Función Fibonacci recursiva
def fibonacci_recursiva(numero):
    return 0 if numero == 0 else 1 if numero == 1 else fibonacci_recursiva(numero - 1) + fibonacci_recursiva(numero - 2)

# Función Fibonacci iterativa
def fibonacci_iterativa(numero):
    if numero < 2:
        return numero
    a, b = 0, 1
    for _ in range(2, numero + 1):
        a, b = b, a + b
    return b

# Cuerpo del programa
print("0 1 1 2 3 5 8 13 21 34 55 89 144 233")

# Calcular con la función recursiva
a = fibonacci_recursiva(11)
print("El resultado de la serie Fibonacci de forma recursiva es:", a)

# Calcular con la función iterativa
b = fibonacci_iterativa(5)
print("El resultado de la serie Fibonacci de forma iterativa es:", b)

# Calcular y mostrar los números de Fibonacci hasta un número ingresado
numeros = int(input("Digite un número para calcular la serie Fibonacci hasta ese término: "))
for i in range(numeros + 1):
    print(f"Fibonacci({i}) = {fibonacci_iterativa(i)}")
