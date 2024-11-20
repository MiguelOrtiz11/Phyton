# Algoritmo de ordenamiento por inserción directa para ordenar una 
# lista de números ingresados por el usuario.

# Función para leer una lista de números ingresados por el usuario
def leerLista():
    lista = []
    cant = int(input("Digite la cantidad de números a ingresar: "))
    for i in range(cant):
        lista.append(int(input("Ingrese un número: ")))
    return lista

# Función que implementa el algoritmo de inserción directa
def insercciondirecta(lista, tam):
    for i in range(1, tam):
        v = lista[i]  # Elemento a insertar
        j = i - 1
        while j >= 0 and lista[j] > v:
            lista[j + 1] = lista[j]  # Desplaza el elemento hacia la derecha
            j -= 1
        lista[j + 1] = v  # Inserta el elemento en la posición correcta

# Función para imprimir los elementos de una lista
def imprimirlista(lista, tam):
    for i in range(tam):
        print(lista[i], end=" ")
    print()

# Cuerpo principal del programa
a = leerLista()  # Leer lista del usuario
print("Lista original:", a)  # Imprimir lista original
insercciondirecta(a, len(a))  # Ordenar lista con inserción directa
print("Lista ordenada:", a)  # Imprimir lista ordenada
imprimirlista(a, len(a))  # Imprimir elementos ordenados
