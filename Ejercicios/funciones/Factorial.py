from math import factorial

# Función para calcular el factorial de forma recursiva
def factorialrecursivo(n):
    return 1 if n == 0 else n * factorialrecursivo(n - 1)

# Función para calcular el factorial de forma iterativa
def facto(n):
    facto_resp = 1
    while n > 1:
        facto_resp *= n  # Forma compacta de escribir facto_resp = facto_resp * n
        n -= 1  # Decrementamos n
    return facto_resp

# Cuerpo del programa
a = factorialrecursivo(3)
print("El factorial de forma recursiva de 3 es:", a)

b = facto(5)
print("El factorial de forma iterativa de 5 es:", b)

c = factorial(5)
print("El factorial de la función de Python de 5 es:", c)
