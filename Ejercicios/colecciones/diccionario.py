ciudades = {'santander': 'Bucaramanga', 'boyaca': 'tunja', 'casanare': 'yopal'}

print(ciudades)  # Muestra el diccionario
print(ciudades['boyaca'])  # Accede al valor de una clave
print(len(ciudades))  # Cantidad de elementos
print(ciudades.keys())  # Claves
print(ciudades.values())  # Valores

print(ciudades.get('casanare'))  # Obtener valor de una clave

del ciudades['santander']  # Eliminar una clave
print(ciudades)

ciudades['casanare'] = 'aguazul'  # Reemplazar un valor
print(ciudades)
