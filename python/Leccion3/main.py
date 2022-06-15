'''
#Ciclo while (Mientra o durante)
contador = 0
while contador < 78:
    print("Ejecutamos nuestro ciclo while", contador)
    contador += 1
else:
    print("Fin del ciclo while")
'''

'''#Imprimir los numeros del 0 al 5 con el ciclo while

contador = 0
maximo = 5
while contador <= maximo:
    print(contador)
    contador += 1'''

'''#Imprimir los numeros del 5 al 50 con el ciclo while

contador = 5
minimo = 0
while contador >= minimo:
    print(contador)
    contador -= 1'''

'''# Ciclo for
cadena = 'Hello'
for letra in cadena:
    print(letra)
else:
    print('Fin del ciclo for')'''

'''#Palabra reservada break

for letra in 'Alemania':
    if letra == 'a':
        print(f'Letra encontrada {letra}')
        break
else:
    print('Fin del ciclo for')'''

#Palabra reservada continue
    #Imprime n° pares
for i in range(6):
    if i % 2 == 0:
        print(f'Valor = {i}')

    #Imprime n° pares
for i in range(6):
    if i % 2 != 0:
        continue # el continue sirve para saltar a la siguiente vuelta del ciclo repetitivo
    print(f'Valor = {i}')


