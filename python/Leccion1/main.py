variable = 3
print(variable)
variable = "a"
print(variable)
variable = 3.5
print(variable)
x = 10
y = 2
z = x + y
print(id(x))
# literales
print(id(y))
print(id(z))

# Tipos int, float, String, Bool
a = True
print(type(a))
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola Alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Strings
miGrupoFavorito = "AC DC:"
caracteristicas = "The Best Rock Band"
print("Mi grupo favorito es:", miGrupoFavorito, caracteristicas)
numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))

# Bool - Boleanos
miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es: verdadero")
else:
    print("El resultado es falso")
# Procesar la entrada del usuario
# función input
resultado = input("Ingrese un numero: ")
print(resultado)

titulo = input("Proporciona el titulo del libro: ")
autor = input("Proporciona el autor del libro: ")
print(titulo, "fue escrito por", autor)
'''
'''
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
# print("Resultado de la suma:", suma)
print(f"El resultado de la suma es: {suma}")

resta = operandoA - operandoB
print(f"El resultado de al resta es: {resta}")

multiplicación = operandoA * operandoB
print(f"El resultado de la multiplicación es: {multiplicación}")

division = operandoA / operandoB
print(f"El resultado de la división es: {division}")

division = operandoA // operandoB
print(f"El resultado de la division (int) es: {division}")

modulo = operandoA % operandoB
print(f"El resultado de la divison o residuo (modulo) es: {modulo}")

exponente = operandoA ** operandoB
print(f"El resultado del exponente es: {exponente}")

alto = int(input("Proporciona el alto del rectángulo: "))
ancho = int(input("Proporciona el ancho del rectángulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print(f"El alto del rectangulo es: {area}")
print(f"El ancho del rectangulo es: {perimetro}")
'''
'''
miVariable3 = 10
print(miVariable3)

# operadores de reasignación
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# miVariable3 = miVariable3 - 2
miVariable3 -= 2
print(miVariable3)

# miVariable3 = miVariable3 * 3
miVariable3 *= 3
print(miVariable3)
# miVariable3 = miVariable3 / 2
miVariable3 /= 2
print(miVariable3)

# Operadoresde comparación

d = 4
b = 2
resultado = d == b  # comprobamos si son iguales
print(resultado)

# Operador diferente
resultado = d != b
print(resultado)

# Operador mayor que
resultado = d > b
print(resultado)

# Operador menor que
resultado = d < b
print(resultado)

# Operador menor o igual que
resultado = d <= b
print(resultado)
'''
'''
num = int(input("Ingrese un numero: "))
if num % 2 == 0:
    print(f"El numero: {num} es par")
else:
    print(f"El numero: {num} es impar")

num = input
'''
'''
# Operadores Lógicos
a = True
b = True
resultado = a and b
print(resultado)

# Operador or
resultado = a or b
print(resultado)

# Operador not
resultado = not a
print(resultado)
'''
'''
num = int(input("Ingrese un número: "))

if num >= 0 and num <= 5:
    print(f"El numero {num} se encuentra dentro del rango 0 y 5")
else:
    print(f"El numero {num} no se encuentra dentro del rango 0 y 5")
'''
'''
# Ejercicio con operador or
vacaciones = False
diaDescanso = True
if not (vacaciones or diaDescanso):
    print("Puede asistir al juego")
else:
    print("Tiene trabajo que hacer")
'''
'''
# Ejercicio: Rango entre 20 y 30 años
edad = int(input("Ingrese su edad: "))
veinte = edad >= 20 and edad < 30
print(veinte)
treinta = edad >= 30 and edad < 40
print(treinta)

if veinte or treinta:
    print("La edad está dentro del rango")
else:
    print("La edad está fuera de rango")
'''
'''
edad = int(input("Ingrese su edad: "))
veinte = edad >= 20 and edad < 30
print(veinte)
treinta = edad >= 30 and edad < 40
print(treinta)

if veinte or treinta:
    if veinte:
        print("La edad está dentro del rango de los 20")
    elif treinta:
        print("La edad está dentro del rango de los 30")
else:
    print("La edad está fuera de rango")

# Metodo simple

if (20 <= edad < 30) or (30 <= edad < 40):
    print("Estas dentro del rango de los 20 a 30 años")
else:
    print("No estás dentro del rango")
'''
'''
# Ejercicio mayor de dos números
num1 = int(input("Ingrese un numero entero para el valor 1: "))
num2 = int(input("Ingrese un numero entero para el valor 2: "))

if num1 > num2:
    print("El numero 1 es mayor")
else:
    print("El numero 2 es mayor")

# Ejercicio: Tienda de libros

print("Ingrese los siguientes datos del libro")
nombreLibro = (input("Ingrese el nombre del libro: "))
idLibro = int(input("Ingrese el id del libro: "))
precioLibro = float(input("Ingrese el precio del libro: "))
envíoGratuito = (input("Indicar si el envío es gratuito o no (True/False: "))

if envíoGratuito == "True":
    envíoGratuito = True
elif envíoGratuito == "False":
    envíoGratuito = False
else:
    envíoGratuito = "El valor es incorrecto, debe escribir True/False"
print(f'''
    Nombre: {nombreLibro}
    ID: {idLibro}
    Precio: {precioLibro}
    ¿Envío gratuito?: {envíoGratuito}
''')





