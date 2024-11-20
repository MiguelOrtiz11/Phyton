import sys

try:
    4 + saludo * 3  # 'saludo' no está definido, esto genera un NameError
except NameError:
    print("El nombre de la variable no existe.")
    # sys.exc_info() devuelve una tupla con detalles del error (tipo, valor, traza)
    print("El error fue:", sys.exc_info()[1])  # [1] contiene el mensaje de error
