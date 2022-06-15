# Euivalentes de notas

nota = int(input("Ingrese su nota numerica: "))
calificacion = None
mensaje = None

if 9 <= nota <= 10:
    calificacion = "A"
    mensaje = 'Exelente trabajo'
elif 8 <= nota < 9:
    calificacion = "B"
    mensaje = 'Exelente trabajo'
elif 7 <= nota < 8:
    calificacion = "C"
    mensaje = 'Aprobaste, pero deberias esforzarte mas'
elif 6 <= nota < 7:
    calificacion = "D"
    mensaje = 'Aprobaste, pero deberias esforzarte mas'
elif 0 <= nota < 6:
    calificacion = "F"
    mensaje = 'Debes estudiar :( '
else:
    mensaje = "ERROR - La nota que usted ingreso no esta contemplada por el sistema"

print(f"{mensaje}. Su calificacion es de: {calificacion}")
