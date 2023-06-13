# Proyecto, Fran

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter as ctk

def calcular_Trayectoria(velocidad, angulo):
    # Convierto el angulo a radianes
    angle_rad = np.deg2rad(angulo)

    # Calculo el tiempo de vuelo
    tiempo_de_vuelo = (2 * velocidad * np.sin(angle_rad)) / 9.8

    # Calculo el timpo de intervalos
    t = np.linspace(0, tiempo_de_vuelo, num=100)

    # Calculo las posiciones X y Y en cada intervalo de tiempo
    x = velocidad * np.cos(angle_rad) * t
    y = velocidad * np.sin(angle_rad) * t - 0.5 * 9.8 * t ** 2

    # Encontrar la altura maxima y tiempo correspondiente
    Altura_maxima = np.max(y)
    Altura_maximo_tiempo = t[np.argmax(y)]

    return x, y, Altura_maxima, Altura_maximo_tiempo


# Muestra la trayectoria al ingresar los datos
def mostrar_Trayectoria(x, y, Altura_Maxima, Altura_maximo_tiempo):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.plot(Altura_maximo_tiempo, Altura_Maxima, 'r-')
    ax.set_xlabel('Distancia (Metros)')
    ax.set_ylabel('Altura (Metros)')
    ax.set_title('Demostración del proyectil')
    plt.show()


def on_submit():
    velocidad = float(velocity_entry.get())
    angulo= float(angle_entry.get())

    x, y, Altura_maxima, Altura_maxima_tiempo= calcular_Trayectoria(velocidad, angulo)
    mostrar_Trayectoria(x, y, Altura_maxima, Altura_maxima_tiempo)


# Crear el GUI como ventana
window = ctk.CTk()
window.title("Proyección de lanzamiento")
window.configure(bg_color ='transparent')
window.geometry("300x250")

# Crear la entrada y la etiqueta de entradad de velocidad
velocity_label =ctk.CTkLabel(window, text="Velocidad Inicial(m/s):", fg_color='transparent', bg_color ='transparent')
velocity_label.pack(padx = 10 , pady = 10)
velocity_entry = ctk.CTkEntry(window)
velocity_entry.pack()

# Crear la entrada y la etiqueta de entrada del ángulo
angle_label = ctk.CTkLabel(window, text="Angulo de Lanzamiento:", fg_color='transparent', bg_color ='transparent')
angle_label.pack(padx = 10 , pady = 10)
angle_entry = ctk.CTkEntry(window)
angle_entry.pack()

# Crear el boton de enviar
submit_button = ctk.CTkButton(window, text="Aceptar", command=on_submit)
submit_button.pack(padx = 20 , pady = 20)

# Ejecuta el bucle de eventos del GUI
window.mainloop()