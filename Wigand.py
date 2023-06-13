import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.widgets import Button
from functools import partial
import customtkinter as ctk

#Variables globales
d=[0,25,50,75,99]
cont=0
pelota_x= 0.0
pelota_y= 0.0

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
    print(np.argmax(y))
    
    Altura_maxima_tiempo = t[np.argmax(y)]
    X_en_altura_maxima = x[np.argmax(y)]

    return x, y, Altura_maxima, Altura_maxima_tiempo,X_en_altura_maxima,t

def previo(event,pelota,x,y):
    global d,pelota_x,pelota_y,cont
    cont-=1
    if cont < 0:
        cont=4
    pelota_x= float(x[d[cont]])
    pelota_y= float(y[d[cont]])
    pelota.set_offsets([pelota_x, pelota_y])
    plt.draw()
    return

def next(event,pelota,x,y):
    global d,pelota_x,pelota_y,cont
    cont+=1
    if cont > 4:
        cont=0
    pelota_x= float(x[d[cont]])
    pelota_y= float(y[d[cont]])
    pelota.set_offsets([pelota_x, pelota_y])
    plt.draw()
    return

def mostrar_Trayectoria(x, y, Altura_Maxima, Altura_maxima_tiempo, X_en_altura_maxima,t):
    fig, ax = plt.subplots(dpi = 150)
    ax.plot(x, y)
    plt.subplots_adjust(bottom=0.2)
    
    global pelota_x,pelota_y
    pelota_x=X_en_altura_maxima
    pelota_y=Altura_Maxima
    
    ax_prev = plt.axes([0.58, 0.05, 0.15, 0.07])
    ax_next = plt.axes([0.75, 0.05, 0.15, 0.07])
    
    Button_prev = Button(ax_prev, 'Previo', color='green', hovercolor= 'blue')
    Button_next = Button(ax_next, 'Siguiente', color='orange', hovercolor= 'red')
    pelota = ax.scatter(pelota_x, pelota_y)
    
    partial_button_clicked = partial(previo, pelota=pelota,x=x,y=y)
    partial_button_clicked1 = partial(next, pelota=pelota,x=x,y=y)
    
    Button_prev.on_clicked(partial_button_clicked)
    Button_next.on_clicked(partial_button_clicked1)
    ax.plot(X_en_altura_maxima, Altura_Maxima, 'ro')
    ax.set_xlabel('Distancia (Metros)')
    ax.set_ylabel('Altura (Metros)')
    ax.set_title('Demostración del proyectil')
    plt.show()
    
def on_submit():
    velocidad = float(velocity_entry.get())
    angulo= float(angle_entry.get())

    x, y, Altura_maxima, Altura_maxima_tiempo,X_en_altura_maxima,t= calcular_Trayectoria(velocidad, angulo)
    mostrar_Trayectoria(x, y, Altura_maxima, Altura_maxima_tiempo,X_en_altura_maxima,t)

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

