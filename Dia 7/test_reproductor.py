from tkinter import *
from tkinter.ttk import *
from Reproductor import *

musica = Reproductor("wefere.mp3") 

def play_musica():
    musica.volume(0.8)  # 0 a 1
    musica.play()

def pause_musica():
    musica.pause()

def salir():
    master.destroy()  # Cierra la ventana principal

master = Tk()
master.geometry("200x200")

label = Label(master, text="Reproductor de música")
label.pack(pady=10)

btn_play = Button(master, text="Reproducir", command=play_musica)
btn_play.pack(pady=10)

btn_pause = Button(master, text="Pausar", command=pause_musica)
btn_pause.pack(pady=10)

btn_exit = Button(master, text="Salir", command=salir)
btn_exit.pack(pady=10)

master.mainloop()
