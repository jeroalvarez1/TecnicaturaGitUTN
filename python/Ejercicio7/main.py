#Ejercicio 7 sumañar n valores

def calcular(cantidad):
    suma = 0
    for i in range(cantidad):
        suma = suma + i
    return suma

print("Ejercicio 7 calcular la suma de 'n' primeros numeros")
cant = calcular(int(input("Ingrese la cantidad de numeros que desea que se calculen: ")))
print(f"La suma es: {cant}")