# Hacer un programa para una fruteria que ofrece manzanas a 4200 el kilo 
# con descuento asi: 0 a 2 kilos no tiene descuento hasta 5 kilos 10% de 
# descuento hasta 10 kilos 15% de descuento y si es mayor a 10 kilos 20% 
# de descuento

# Programa para calcular el valor de una compra en una frutería
kilos = float(input("Digite la cantidad de kilos a comprar: "))
valor_compra = kilos * 4200  # Precio base sin descuento

# Determinar el descuento según la cantidad de kilos
if kilos <= 2:
    descuento = 0
elif kilos <= 5:
    descuento = valor_compra * 0.10
elif kilos <= 10:
    descuento = valor_compra * 0.15
else:
    descuento = valor_compra * 0.20

# Calcular el valor final a pagar
valor_pagar = valor_compra - descuento

# Mostrar resultados
print(f"La compra de {kilos} kilos tiene un valor base de: {valor_compra:.2f}")
print(f"Usted tiene un descuento de: {descuento:.2f}")
print(f"Por lo tanto, el valor a pagar es: {valor_pagar:.2f}")
