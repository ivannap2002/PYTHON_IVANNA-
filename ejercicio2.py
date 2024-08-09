#Escribí un programa que solicite al usuario ingresar la cantidad de
#kilómetros recorridos por una motocicleta y la cantidad de litros de
#combustible que consumió durante ese recorrido. Mostrar el
#consumo de combustible por kilómetro

kilometros = float(input("Introduce los kilómetros recorridos: "))

litros = float(input("Introduce los litros de combustible consumidos: "))


consumo_por_km = litros / kilometros

print("Consumo de combustible por kilómetro:", consumo_por_km)
