# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
num=int(input("digite numero: "))
for i in range(1, 11):
    print(f'{i} x {num} = {i * num}')
