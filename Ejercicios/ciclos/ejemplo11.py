#hacer un programa que sume la cantidad de numeros

# Inicializamos la variable para almacenar la suma
suma = 0

# Solicitamos al usuario el número total de la sumatoria
n = int(input("Digite el número hasta donde desea calcular la sumatoria: "))

# Iteramos desde 1 hasta n (incluido)
for i in range(1, n + 1):
    suma += i  # Sumamos cada número al total

# Mostramos el resultado
print(f"La sumatoria desde 1 hasta {n} es: {suma}")

