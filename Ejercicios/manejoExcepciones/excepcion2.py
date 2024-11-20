try:
    a = float(input("Introduce el numerador: "))
    b = float(input("Introduce el denominador: "))
    resultado = a / b
    print(f"El resultado de {a} / {b} es {resultado}")
except ZeroDivisionError:
    print("No puedes dividir por 0. Por favor, ingresa un denominador diferente.")
except ValueError:
    print("Por favor, introduce números válidos.")
finally:
    print("Programa finalizado.")
