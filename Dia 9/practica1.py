notas = []

# Leer datos
for x in range(3):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {x + 1}: "))
            if 1 <= nota <= 5:
                notas.append(nota)
                break
            else:
                print("La nota debe estar en el rango de 1 a 5.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Calcular el promedio
promedio = sum(notas) / len(notas)

# Determinar si está aprobado o reprobado
if promedio > 1.7:
    print(f"Promedio: {promedio:.2f} - Aprobado")
else:
    print(f"Promedio: {promedio:.2f} - Reprobado")

