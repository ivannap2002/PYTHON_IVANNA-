#Crear una aplicación agenda para guardar el nombre y el teléfono

def agregar_contacto(agenda):
    nombre = input("Introduce el nombre: ")
    telefono = input("Introduce el teléfono: ")
    agenda[nombre] = telefono
    print(f"Contacto {nombre} agregado.")

def mostrar_agenda(agenda):
    if agenda:
        print("\nAgenda de contactos:")
        for nombre, telefono in agenda.items():
            print(f"Nombre: {nombre}, Teléfono: {telefono}")
    else:
        print("\nLa agenda está vacía.")

def main():
    agenda = {}
    while True:
        print("\nOpciones:")
        print("1. Agregar contacto")
        print("2. Mostrar agenda")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            mostrar_agenda(agenda)
        elif opcion == "3":
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
