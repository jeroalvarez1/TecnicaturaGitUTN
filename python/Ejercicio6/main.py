#Ejecicio 6 año bieciesto
def añoBiciesto(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def operativa():
    seguir = 1
    while seguir == 1:
        valor = añoBiciesto(int(input("Ingrese un año: ")))
        if valor == True:
            print("El año es biciesto")
        else:
            print("El año no es biciesto")
        seguir = int(input("Ingrese 1 si desea calcular otro año o 0 si desea terminar el programa: "))

print("Este ejercicio devuelve si el año ingresado es biciesto o no")
operativa()



