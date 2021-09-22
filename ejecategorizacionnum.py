print ("¿Cuantos números se van a categorizar?")
n = int(input())
contador = {
    "mayores": 0,
    "iguales": 0,
    "menores": 0,
}
#Toma de Datos
for i in range (n):
    print ("Escriba un número")
    numero = float (input())
    if (numero > 0):
        contador ["mayores"] += 1
    elif (numero < 0):
        contador ["menores"] += 1
    else:
        contador ["iguales"] += 1

# generación de informe
for llave in contador:
    print ("la cantidad de numeros " + llave)
    print (contador [llave])
