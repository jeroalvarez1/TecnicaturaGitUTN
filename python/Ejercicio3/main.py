#Estacion del año
numEstacion = int(input("Ingrese el numero del mes en el cual usted esta: "))
estacionAño = None
if numEstacion == 1 or numEstacion == 2 or numEstacion == 3:
    estacionAño = "Verano"
elif numEstacion == 4 or numEstacion == 5 or numEstacion == 6:
    estacionAño = "Otoño"
elif numEstacion == 7 or numEstacion == 8 or numEstacion == 9:
    estacionAño = "Invierno"
elif numEstacion == 10 or numEstacion == 11 or numEstacion == 12:
    estacionAño = "Primavera"
else:
     estacionAño = "(ERROR, no hay numero para este mes)"

print(f"La estación del mes {numEstacion} corresponde a {estacionAño}")