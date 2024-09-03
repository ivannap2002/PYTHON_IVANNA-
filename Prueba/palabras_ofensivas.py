from urllib import request
from urllib.error import URLError

palabras_ofensivas = ['payaso','maldicion','loco', 'puto','idiota']
print(palabras_ofensivas)

# Cargar palabras ofensivas desde un archivo de texto
def cargar_palabras_ofensivas(nombre_archivo):
    with open(nombre_archivo, 'r') as f:
        return [linea.strip() for linea in f]

def ver_contenido(url):
    try:
        f = request.urlopen(url)
    except URLError:
        return '¡La URL ' + url + ' no existe!'
    else:
        contenido = f.read().decode('utf-8')
        return contenido

def buscar_palabras_ofensivas(contenido):
    contenido = contenido.lower()
    encontrado = False
    for palabra in palabras_ofensivas:
        if palabra.lower() in contenido:
            encontrado = True
            enviar_notificacion(palabra)
    if not encontrado:
        print("No se encontraron palabras ofensivas.")

def enviar_notificacion(palabra_ofensiva):
    print(f"¡Alerta! Se ha encontrado la palabra ofensiva: {palabra_ofensiva}")

def contar_palabras(url):
    contenido = ver_contenido(url)
    if '¡La URL' in contenido:
        print(contenido)
        return
    print(f"Número de palabras en el contenido: {len(contenido.split())}")


#palabras_ofensivas = cargar_palabras_ofensivas('palabras_ofensivas.txt')



url =  'https://es.wiktionary.org/wiki/Wikcionario:Insultos_regionales'
contenido = ver_contenido(url)

print("Contenido de la URL:")
#print(contenido)
print("\n---------------------------------\n")

buscar_palabras_ofensivas(contenido)
#contar_palabras(url)