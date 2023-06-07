import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter as ctk

def calcular_Trayectoria(velocidad, angulo):
    # Convierto el angulo a radians
    angle_rad = np.deg2rad(angulo)

    # Calculo el tiempo de vuelo
    tiempo_de_vuelo = (2 * velocidad * np.sin(angle_rad)) / 9.8

    # Calculo el timpo en intervalos
    t = np.linspace(0, tiempo_de_vuelo, num=100)

    # Calculo el "x" y "y" posiciones en cada  intervalo del tiempo
    x = velocidad * np.cos(angle_rad) * t
    y = velocidad * np.sin(angle_rad) * t - 0.5 * 9.8 * t ** 2

    # Encuentra la altura maxima y el tiempo correspondiente
    Altura_maxima = np.max(y)
    Altura_maximo_tiempo = t[np.argmax(y)]

    return x, y, Altura_maxima, Altura_maximo_tiempo


def mostrar_Trayectoria(x, y, Altura_Maxima, Altura_maximo_tiempo):
    fig, ax = plt.subplots(dpi = 150)
    ax.plot(x, y)
    ax.plot(Altura_maximo_tiempo, Altura_Maxima, 'ro')
    ax.set_xlabel('Distancia (Metros)')
    ax.set_ylabel('Altura (Metros)')
    ax.set_title('Demostración del proyectil')
    plt.show()
    
    def on_submit():
    velocidad = float(velocity_entry.get())
    angulo= float(angle_entry.get())

    x, y, Altura_maxima, Altura_maxima_tiempo= calcular_Trayectoria(velocidad, angulo)
    mostrar_Trayectoria(x, y, Altura_maxima, Altura_maxima_tiempo)
    
    
    
def on_submit():
    velocidad = float(velocity_entry.get())
    angulo= float(angle_entry.get())

    x, y, Altura_maxima, Altura_maxima_tiempo= calcular_Trayectoria(velocidad, angulo)
    mostrar_Trayectoria(x, y, Altura_maxima, Altura_maxima_tiempo)

# Crea las ventanas GUI
window = ctk.CTk()
window.title("Proyección de lanzamiento")
window.configure(bg_color ='transparent')
window.geometry("300x250")

# Crear la entrada y la etiqueta de entrada de velocidad
velocity_label =ctk.CTkLabel(window, text="Velocidad Inicial(m/s):", fg_color='transparent', bg_color ='transparent')
velocity_label.pack(padx = 10 , pady = 10)
velocity_entry = ctk.CTkEntry(window)
velocity_entry.pack()

# Crear la entrada y la entrada y la etiqueta de entrada de ángulo
angle_label = ctk.CTkLabel(window, text="Angulo de Lanzamiento:", fg_color='transparent', bg_color ='transparent')
angle_label.pack(padx = 10 , pady = 10)
angle_entry = ctk.CTkEntry(window)
angle_entry.pack()

# Crear el boton de enviar
submit_button = ctk.CTkButton(window, text="Aceptar", command=on_submit)
submit_button.pack(padx = 20 , pady = 20)

# Inicia el GUI en un bucle de eventos
window.mainloop()
