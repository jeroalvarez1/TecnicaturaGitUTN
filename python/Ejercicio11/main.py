
import numpy as np

array = []
#vistas
def vistaPedirLongitud():
    longitud = int(input("Ingrese la cantidad de datos a ingresar: "))
    return longitud

def vistaPedirDato():
    number = int(input("Ingrese un numero: "))
    return number

#funciones
def ingresarDatos(number):
    array.append(number)

def repetirEntrarDato(repts):
    cont = 0
    while repts > cont:
        cont += 1
        ingresarDatos(vistaPedirDato())

def listaPares():
    arrayPares = []
    for valor in array:
        if valor % 2 == 0:
            arrayPares.append(valor)
    return arrayPares

def listaImpares():
    arrayImpares = []
    for valor in array:
        if valor % 2 != 0:
            arrayImpares.append(valor)
    return arrayImpares

def procesoPrincipalPrint():
    repetirEntrarDato(vistaPedirLongitud())
    print(f"La suma de los numeros pares es {np.sum(listaPares())}")
    print(f"Hay {len(listaPares())} numeros pares")
    print(f"El promedio de los numeros impares es de {np.mean(listaImpares())}")

procesoPrincipalPrint()
