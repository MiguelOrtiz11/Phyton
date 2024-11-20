# Algoritmo de inserción usando búsqueda binaria para ordenar una lista. 

def leerlista():
    # Leer una lista de números del usuario
    lista = []
    cant = int(input("Digite la cantidad de números a ingresar: "))
    for i in range(cant):
        lista.append(int(input("Ingrese un número: ")))
    return lista

def inserccionbinaria(lista, tam):
    # Ordenar la lista usando el algoritmo de inserción con búsqueda binaria
    for i in range(1, tam):
        aux = lista[i]  # Elemento a insertar
        izq = 0
        der = i - 1
        
        # Búsqueda binaria para encontrar la posición de inserción
        while izq <= der:
            m = (izq + der) // 2
            if aux < lista[m]:
                der = m - 1
            else:
                izq = m + 1
        
        # Desplazar elementos para hacer espacio para 'aux'
        j = i
        while j > izq:
            lista[j] = lista[j - 1]
            j -= 1
        
        # Insertar el elemento en la posición encontrada
        lista[izq] = aux

def imprimirlista(lista, tam):
    # Imprimir los elementos de la lista
    for i in range(tam):
        print(lista[i], end=" ")
    print()

# Cuerpo del programa
a = leerlista()  # Leer lista del usuario
print("Lista original:", a)
inserccionbinaria(a, len(a))  # Ordenar la lista
print("Lista ordenada:", a)
imprimirlista(a, len(a))  # Imprimir lista ordenada
