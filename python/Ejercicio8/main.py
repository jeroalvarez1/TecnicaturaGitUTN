#Leer 10 numero e imprima cuantos son primitivos, negativo y neutros
def calculate(num):
    if num == 0:
        return 0
    elif num % 2 == 0:
        return 1
    elif num % 2 != 0:
        return 2


def proceso():
    cont = 0
    while cont < 10:
        cont += 1
        numberEnter = int(input("Ingrese un numero: "))
        numberType = calculate(numberEnter)
        if numberType == 0:
            mensaje = f"El numero {numberEnter} es NEUTRO"
        elif numberType == 1:
            mensaje = f"El numero {numberEnter} es PAR"
        elif numberType == 2:
            mensaje = f"El numero {numberEnter} es IMPAR"
        print(mensaje)

proceso()