#CALCULAR FACTORIAL DE UN NUMERO
def calcularFactorial(number):
    factorial = 1
    if number >= 0:
        for i in range(number+1):
            if i == 0:
                continue
            factorial = factorial * i
    else:
        factorial = "ERROR - El numero ingresado debe ser mayor o igual a 0"
    return factorial

def ingresarDatos():
    number = int(input("Ingrese un numero: "))
    return number



print(calcularFactorial(ingresarDatos()))