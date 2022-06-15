# Sentencia if/else
condicion = True
if condicion:
    print("Condicion Verdadera")
else:
    print("Condición Falsa")

condicion1 = 10
if condicion1:
    print("Condicion Verdadera")
else:
    print("Condición Falsa")

condicion2 = 9
if condicion2 == True:
    print("Condicion Verdadera")
elif condicion2 == False:
    print("Condicion Falsa")
else:
    print("Condición sin especificar")

num = int(input("Digite un número en el rango del 1 al 3: "))
numTexto = ""
if num == 1:
    numTexto = "Numero uno"
elif num ==2:
    numTexto = "Numero dos"
elif num == 3:
    numTexto = "Numero tres"
else:
    numTexto = "Has ingresado un número fuera de rango"
print(f"El numero ingrasado es: {num} - {numTexto}")

condicion5 = True
if condicion5:
    print("Condicon verdadera")
else:
    print("Condicon Falsa")

print("Condición Verdadera") if condicion5 else print("Condicion Falsa")
