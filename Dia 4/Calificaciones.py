#Escriba un programa que recibe las calificaciones de los alumnos de
#la materia de Programación Python e imprime el promedio general.
#El programa se detiene cuando lee el número cero. Tenga en cuenta
#que se desconoce cuantas calificaciones serán introducidas.

#Modifique el programa anterior para que las calificaciones
#permitidas solo sean 1 al 5.

def calcular_promedio():
    calificaciones = []
    
    while True:
        calificacion = int(input("Introduce la calificación (1-5) o 0 para terminar: "))
        
        if calificacion == 0:
            break
        elif 1 <= calificacion <= 5:
            calificaciones.append(calificacion)
        else:
            print("Calificación no válida.")
    
    if calificaciones:
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"El promedio general es: {promedio:.2f}")
    else:
        print("No se introdujeron calificaciones.")

calcular_promedio()
