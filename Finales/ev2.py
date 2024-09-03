# Leer dos números del usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Imprimir los números ingresados
print("Los números ingresados fueron: num1 =", num1, "y num2 =", num2)

# Comparar los dos números e imprimir el mayor o si son iguales
if num1 > num2:
    print("El número mayor es:", num1)
elif num2 > num1:
    print("El número mayor es:", num2)
else:
    print("Ambos números son iguales")
