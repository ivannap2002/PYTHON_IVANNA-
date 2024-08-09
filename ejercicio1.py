#Escribir un programa que calcule el IMC de una persona

peso = float(input("Introduce tu peso: "))

altura = float(input("Introduce tu altura: "))

imc = peso / (altura * altura)

print("Tu IMC es:", imc)
