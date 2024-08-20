import os 

#menu principal
respuesta = -1
while (respuesta != 0):
    print("Elija una opción")
    print("1. Calculadora")
    print("2. Ver mi IP")
    print("3. Administrador de Tareas")
    print("4. Apagar equipo en 5 minutos")
    print("5. Cancelar apagado")
    print("0. Salir ")
    respuesta = int(input(" "))
    if (respuesta == 1):
        os.system('calc')
    elif (respuesta == 2):
        os.system('ipconfig')
    elif (respuesta == 3):
        os.system('taskmgr')
    elif (respuesta == 4):
        os.system('shutdowm -s -t 300')
    elif (respuesta == 5):
        os.system(' ')
    else:
        "No se ha seleccionado nada"