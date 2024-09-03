# Definir el monto límite para el IRP
MONTO_IRP = 80000000

# Solicitar al usuario que ingrese su sueldo mensual
sueldo = int(input("Ingrese cuál es su sueldo mensual: "))

# Calcular el sueldo anual multiplicando el sueldo mensual por 12
sueldoAnual = sueldo * 12

# Verificar si el sueldo anual supera el monto para pagar impuestos
if sueldoAnual > MONTO_IRP:
    print("Esta persona debe pagar impuestos")
else:
    print("Esta persona no debe abonar impuestos")
