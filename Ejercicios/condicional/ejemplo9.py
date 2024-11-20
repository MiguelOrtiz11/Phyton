# Hacer un programa que lea el nombre, seco y la edad de una persona. 
# determine si es mayor de edad y de que sexo es .

# Leer datos de la persona
nombre = input("Digite su nombre: ")
sexo = input("Digite '1' para hombre o '2' para mujer: ")
edad = int(input("Digite su edad: "))

# Verificar si la persona es mayor de edad
if edad >= 18:
    if sexo == '1':
        print(f"{nombre} es un hombre y es mayor de edad.")
    elif sexo == '2':
        print(f"{nombre} es una mujer y es mayor de edad.")
    else:
        print("Opción de sexo no válida.")
else:
    if sexo == '1':
        print(f"{nombre} es un hombre y es menor de edad.")
    elif sexo == '2':
        print(f"{nombre} es una mujer y es menor de edad.")
    else:
        print("Opción de sexo no válida.")
      