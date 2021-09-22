lista = []
while (True):
    print ("Ingrese un Número")
    numero = int(input())
    if (numero < 0):
        break
    lista.append (numero)
suma = 0
for numerico in lista:
    suma += numerico

# len (nombre_lista) me da el dato de numero de datos dentro de la lista
print (suma/len(lista))

