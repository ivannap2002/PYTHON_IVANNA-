#Crear una aplicación que utilice funciones para cargar una lista y otra para imprimir el contenido.

def cargar_lista():
    lista = []
    while True:
        elemento = input("Introduce un elemento (o 'fin' para terminar): ")
        if elemento.lower() == 'fin':
            break
        lista.append(elemento)
    return lista

def imprimir_lista(lista):
    print("Contenido de la lista:")
    for elemento in lista:
        print(f"- {elemento}")

# Programa principal
lista = cargar_lista()
imprimir_lista(lista)
