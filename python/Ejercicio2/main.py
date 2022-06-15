# Imprimir el numero como string

numero = int(input("Ingrese un mumero en el rango del 1 al 3: "))
numeroTexto = ""

if numero == 1:
    numeroTexto = "Numero uno"
elif numero == 2:
    numeroTexto = "Numero dos"
elif numero == 3:
    numeroTexto = "Numero tres"
else:
    numeroTexto = "El numero ingresado se encuentra fuera del rango indicado"
print(f"El numero ingresado es: {numero} - {numeroTexto}")