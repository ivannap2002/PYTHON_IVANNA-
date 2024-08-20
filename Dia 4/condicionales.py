#Dados dos números leídos por teclado, imprimir el mayor y si es par o impar.

#Escriba un programa para validar los datos de acceso ingresados por teclado por el usuario. Los datos leídos son user y password. Se
#deben imprimir “acceso correcto” si los valores ingresados son
#“admin” y 12345 respectivamente. En cualquier otro caso “acceso
#denegado”.

numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))

if(numero_1 > numero_2):
    print("{} es mayor a {}".format(numero_1,numero_2))
    if(numero_1 % 2 == 0):
        print("El numero es par")
    else:
        print("El numero es impar")
elif(numero_1 < numero_2):
    print("{} es mayor a {}".format(numero_2,numero_1))
    if(numero_2 % 2 == 0):
        print("El numero es par")
    else:
        print("El numero es impar")
else:
    print("Los numeros ingresados son iguales")

print("-------------------------------------------------")
usuario = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")
if(usuario == "admin" and password == "12345"):
    print("Acceso correcto")
else:
    print("Acceso denegado")
