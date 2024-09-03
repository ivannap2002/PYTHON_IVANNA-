# Cargar una oración por teclado y contar la cantidad de vocales

# Solicitar al usuario que ingrese una oración
cadena = input("Ingrese una oración: ")

# Definir las vocales en minúsculas y mayúsculas
vocales = "aeiouAEIOU"
contador_vocales = 0

# Recorrer cada carácter de la cadena
for caracter in cadena:
    # Verificar si el carácter es una vocal
    if caracter in vocales:
        contador_vocales += 1

# Imprimir la oración ingresada y la cantidad de vocales
print("La oración ingresada es:", cadena)
print("La cantidad de vocales es:", contador_vocales)
