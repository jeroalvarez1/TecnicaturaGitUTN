
def ingresarPersonas():
    arrayPersonas = []
    for i in range(5):
        x=[]
        x.append(input("Ingrese el nombre del empleado: "))
        x.append(float(input("ingrese el sueldo por hora del empleado: ")))
        x.append(float(input("ingrese las horas trabajadas del empleado: ")))
        arrayPersonas.append(x)
        x=[]
    return arrayPersonas
def operacionResultado(arrayPersonas):
    sumaSalarios = 0
    for i in arrayPersonas:
        print(f"El salario de {i[0]} es de {(i[1]*i[2])}")
        sumaSalarios += (i[1]*i[2])
    return sumaSalarios
print(operacionResultado(ingresarPersonas()))