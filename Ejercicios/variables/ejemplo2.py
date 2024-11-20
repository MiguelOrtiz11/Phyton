# Hacer un programa donde la primera letra del nombre del tripulante
#  y los 4 ultimos digitos de la cedula"

# Datos del tripulante
N1 = "Miguel"  # Primer nombre
N2 = "Angel"   # Segundo nombre
A1 = "Ortiz"   # Primer apellido
A2 = "Escobar" # Segundo apellido
T = "1109661685"  # Número de identificación

# Extracción de caracteres
a = N1[0]  # Primera letra del primer nombre: 'M'
b = N2[0]  # Primera letra del segundo nombre: 'A'
c = A1[0]  # Primera letra del primer apellido: 'O'
d = A2[0]  # Primera letra del segundo apellido: 'E'
e = T[-4:] # Últimos 4 dígitos de la cédula: '1685'

# Generar e imprimir el identificador único
print(a + b + c + d + e)  # Salida: MAOE1685
