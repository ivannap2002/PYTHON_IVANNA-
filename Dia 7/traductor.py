# Diccionario de traducción
traductor = {
    "hola": "hello",
    "mundo": "world",
    "perro": "dog",
    "gato": "cat",
   
}

while True:
    palabra = input("Introduce una palabra en español (o 0 para salir): ").lower()

    if palabra == "0":
        break

    if palabra in traductor:
        print(f"La traducción de '{palabra}' es '{traductor[palabra]}'")
    else:
        print(f"La palabra '{palabra}' no está en el diccionario.")
        agregar = input("¿Deseas agregarla al diccionario? (s/n): ").lower()
        
        if agregar == "s":
            traduccion = input(f"Introduce la traducción de '{palabra}' en inglés: ").lower()
            traductor[palabra] = traduccion
            print(f"'{palabra}' ha sido añadida al diccionario con la traducción '{traduccion}'.")

print("Programa terminado.")
