import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.widgets import Button
from functools import partial
import customtkinter as ctk
import seaborn as sns

main_window = ctk.CTk()                                                                                #   Asignamos las propiedades de ctk.Ctk a main_window
main_window.title("Tiro Parabolico")                                                                            #   Ponemos nombre a la ventanita creada
main_window.geometry("900x600")                                                                         #   Definimos la resolucion de la ventana
main_window_width, main_window_height = main_window.winfo_geometry()[0], main_window.winfo_geometry()[1] #   Obtenemos el alto y ancho
main_window.resizable(False, False)

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
 
    fig, ax = plt.subplots(dpi=150)
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
    


# Crea las ventanas GUI
graphic_frame = ctk.CTkFrame(main_window, width=643, height=480)    #Frame para el gráfico  "graphic_frame"
graphic_frame.grid(row=0, column=1, pady=20)                        #Posicionamiento del frame para gráficos

buttons_frame = ctk.CTkFrame(main_window, width=800, height=450)    #Frame para Botones/textboxes   "buttons_frame"
buttons_frame.grid(row=0, column=0, padx=20, pady=10)               #Posicionamiento del frame para los botones/texboxes

# plot_buttons = ctk.CTkFrame(main_window, width=740, height=200)
# plot_buttons.grid(row=1, column=1, padx=20, pady=10)

#______________________________________________________________________________________________________________
txt1label = ctk.CTkLabel(buttons_frame, width=10, height=20, text="Velocidad Inicial:", font=ctk.CTkFont(size=12, weight="normal"))    #Crear texto dentro de buttons_frame
txt1label.grid(row=0, column=0, columnspan=2, pady=15, sticky="sew")                                                               #Posicionamiento del texto dentro de buttons_frame

angle_entry = ctk.CTkEntry(buttons_frame, width=60, height=12)                                                 #Textbox para almacenar valores
angle_entry.grid(row=1, column=0, padx=2, pady=5, sticky="ne")                                                                             #Posicion de la textbox


b_1 = ctk.CTkSegmentedButton(buttons_frame,width=60, height=10 , values=["m/s"])                         #Segmented button, para 2 botones en 1
b_1.grid(row=1, column=1, padx=2, pady=8, sticky="nw")                                                                               #Posicion y config del segmented button
b_1.set("m/s")

txt_2_label = ctk.CTkLabel(buttons_frame, width=5, height=10, text="Angulo de Lanzamiento:", font=ctk.CTkFont(size=12, weight="normal"))
txt_2_label.grid(row=3, column=0, columnspan=2, pady=15, sticky="sew")
velocity_entry = ctk.CTkEntry(buttons_frame, width=60, height=8)
velocity_entry.grid(row=4, column=0, padx=2, pady=5, sticky="ne")
b_2 = ctk.CTkSegmentedButton(buttons_frame,width=60, height=10 , values=["β"])
b_2.grid(row=4, column=1, padx=2, pady=8, sticky="nw")
b_2.set("β") 


def calculofinal():
    global angle_entry, velocity_entry

    angle = float(angle_entry.get())
    velocity = float(velocity_entry.get())
    
    temp1 = calcular_Trayectoria(angle, velocity)
    print(temp1)
    fig = mostrar_Trayectoria(temp1[0], temp1[1], temp1[2], temp1[3],temp1[4],temp1[5])
    #complete los "temp1" hasta el 5 para que funcionara



    # Crear un lienzo de Matplotlib para Tkinter
    lienzo = FigureCanvasTkAgg(fig, master=graphic_frame)
    lienzo.get_tk_widget().place(x = 2, y = 2)
    return

b_3 = ctk.CTkButton(buttons_frame, width=60, height=8, command=calculofinal, text = 'Aceptar')
b_3.grid(row=5, column=1, padx=2, pady=8, sticky="nw")

def on_submit():
    velocidad = float(velocity_entry.get())
    angulo= float(angle_entry.get())

    x, y, Altura_maxima, Altura_maxima_tiempo,X_en_altura_maxima,t= calcular_Trayectoria(velocidad, angulo)
    mostrar_Trayectoria(x, y, Altura_maxima, Altura_maxima_tiempo,X_en_altura_maxima,t)
# Inicia el GUI en un bucle de eventos
main_window.mainloop()