try:
    n = float(input("Introduce un número: "))  # Solicitar un número al usuario
    m = 4
    if m == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")  # Manejo de división por cero
    print("{}/{} = {}".format(n, m, n / m))  # Imprime el resultado de la división
    # También puede ser con concatenación de strings
    print(n, "/", m, " = ", n / m)

except ValueError:
    print("Ha ocurrido un error: introduce un número válido.")  # Error si no se ingresa un número
except ZeroDivisionError as e:
    print(e)  # Error si se intenta dividir por cero
else:
    print("Todo ha funcionado correctamente.")  # Si no hubo errores, muestra este mensaje
finally:
    print("Fin del programa.")  # Este mensaje se imprime siempre
