suma = 0
contador = 0
# Es un while que nunca va a terminar siempre y cuando no se rompa on break
while (True):
    print ("Ingrese un numero")
    numero = int(input())
    if (numero < 0):
        break
    # Forma resumida "suma = suma + numero   
    suma += numero
    contador += 1
    promedio = suma/contador
if (contador != 0):
    print ("El promedio es:" + str (promedio))
 
    