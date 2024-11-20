# Definimos unas variables con una cadena de texto
a = "perro"  # Puede representar cualquier palabra o concepto
carro = "renault"  # Nombre de una marca de automóvil
animal = "caballo_23"  # Puede ser un identificador o etiqueta para un objeto
aviso = "vivimos en una sociedad profundamente dependiente de la ciencia y la tecnología"

# Mostramos el aviso dividido en palabras usando split(), que separa por espacios por defecto
print(aviso.split())  # Salida: ['vivimos', 'en', 'una', ..., 'ciencia', 'y', 'la', 'tecnología']

# Concatenamos las variables a, carro y animal en una sola cadena
union = a + carro + animal  # Junta las cadenas sin espacios
print(union)  # Salida: "perrorenaultcaballo_23"

# Definimos otra variable con el nombre de un país
pais = "colombia"

# Multiplicamos la cadena 'pais' por 3, lo que repite su contenido 3 veces
multi = 3 * pais  # Salida: "colombiacolombiacolombia"
print(multi)

# Convertimos todo el texto de 'pais' a mayúsculas
print(pais.upper())  # Salida: "COLOMBIA"

# Convertimos el texto de 'pais' a formato de título (primera letra en mayúscula)
print(pais.title())  # Salida: "Colombia"

# Contamos cuántas veces aparece la letra "o" en 'pais'
print(pais.count("o"))  # Salida: 2, ya que hay dos "o" en "colombia"
