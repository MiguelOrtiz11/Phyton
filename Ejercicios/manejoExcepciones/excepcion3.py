try:
    num1 = int(input("Ingrese el número divisor: "))
    num2 = int(input("Ingrese el número dividendo: "))
    resultado = num1 / num2
except ValueError:
    print("Por favor, ingrese solo números enteros.")
except ZeroDivisionError:
    print("No se puede dividir entre cero!!!")
else:
    print(f"El resultado de {num1} / {num2} es {resultado:.2f}")
finally:
    print("Fin del programa.")
