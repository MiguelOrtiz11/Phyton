#hacer una nota que lea una nota definitiva y clasifique al alumno asi: su la nota esta entre 4.5 y 5 
# es excelente si esta entre 4 y 4.4 es spbresaliente si esta entre 3.0 y 3.9 es aceptable si esta 
#menos a 2.9 es deficiente

nota = float(input("Digite su nota definitiva: "))

if 4.5 <= nota <= 5.0:
    print("Su nota es excelente")
elif 4.0 <= nota < 4.5:
    print("Su nota es sobresaliente")
elif 3.0 <= nota < 4.0:
    print("Su nota es aceptable")
elif 0 <= nota < 3.0:
    print("Su nota es deficiente")
else:
    print("Nota no válida. Debe estar entre 0 y 5.")
