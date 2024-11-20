# Función para leer una lista desde la entrada del usuario
def leerlista():
    lista = []
    cant = int(input("Digite la cantidad de números a ingresar: "))
    for i in range(cant):
        lista.append(int(input("Ingrese un número: ")))
    return lista

# Función que implementa el algoritmo de ordenamiento de burbuja
def burbuja(lista, tam):
    for i in range(1, tam):
        for j in range(0, tam - i):
            if lista[j] > lista[j + 1]:
                # Intercambio de elementos si no están en orden
                k = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = k

# Función para imprimir los elementos de una lista
def imprimirlista(lista, tam):
    for i in range(tam):
        print(lista[i])

# Cuerpo principal del programa
a = leerlista()  # Leer lista del usuario
print(a)  # Imprimir lista original
burbuja(a, len(a))  # Ordenar la lista con el método de burbuja
print(a)  # Imprimir lista ordenada
imprimirlista(a, len(a))  # Imprimir elementos de la lista ordenada
