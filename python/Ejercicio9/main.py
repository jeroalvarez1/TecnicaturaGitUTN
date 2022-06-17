import numpy as np
array = []

def enterData():
    calification = float(input("Digite una calificacion: "))
    array.append(calification)
    return array

def repetir():
    repetir = 1
    while repetir == 1:
        enterData()
        repetir = int(input("Desea ingresar otro alumno, ingrese '1' si lo desea, o '0' en caso contrario: "))

def calcularPromedio(arreglo):
    return np.mean(arreglo)


def valMin(arreglo):
    return np.amin(arreglo)


def operaciones():
    #operaciones
    repetir()
    promedio = calcularPromedio(array)
    valueMin = valMin(array)
    return f"Las notas ingresadas son: {array}, el promedio de las notas es de: {promedio}, y el valor minimo es de: {valueMin} "

print(operaciones())