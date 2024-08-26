from pygame import mixer

class Reproductor:
    # Constructor
    def __init__(self, archivo):
        self.archivo = archivo
        mixer.init()
        self.cargar_archivo()

    def cargar_archivo(self):
        try:
            mixer.music.load(self.archivo)
        except pygame.error as e:
            return f"Error al cargar el archivo: {e}"

    def play(self):
        mixer.music.play()
        return "Reproduciendo música"

    def pause(self):
        mixer.music.pause()
        return "La música se ha pausado"

    def stop(self):
        mixer.music.stop()
        return "La música se detuvo"

    def volume(self, v):
        mixer.music.set_volume(v)
        return "Definiendo volumen a {}".format(v)
