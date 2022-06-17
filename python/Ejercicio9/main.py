import numpy as np
array = []

def enterData():
    calification = float(input("Digite una calificacion: "))
    array.append(calification)
    return array

def repetir():
    repetir = int(input("Desea ingresar otro alumno, precione '1' si lo desea o '0' en caso contrario: "))
    return repetir

def calcularPromedio(arreglo):
    return np.mean(arreglo)


def valMin(arreglo):
    return np.amin(arreglo)


def operaciones():
    #Entrar data
    rep = 1
    while rep == 1:
        enterData()
        rep = repetir()
    #Se calucla el promedio
    promedio = calcularPromedio(array)
    valueMin = valMin(array)
    return f"Las notas ingresadas son: {array}, el promedio de las notas es de: {promedio}, y el valor minimo es de: {valueMin} "

print(operaciones())