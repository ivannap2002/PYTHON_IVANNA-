#Desarrollar un programa que encuentre números primos.
#While 
numero = 10
while True:
    numero += 1 
    bandera = 0 
    for x in range(2,numero):
        if (numero % x == 0):
            bandera = 1

    if(bandera == 0):
        print(f" | {numero}")
        #break 