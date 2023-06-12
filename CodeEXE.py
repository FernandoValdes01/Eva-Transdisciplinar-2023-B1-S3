import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import customtkinter as ctk
import seaborn as sns

main_window = ctk.CTk()                                                                                #   Asignamos las propiedades de ctk.Ctk a main_window
main_window.title("Tiro Parabolico")                                                                            #   Ponemos nombre a la ventanita creada
main_window.geometry("900x600")                                                                         #   Definimos la resolucion de la ventana
main_window_width, main_window_height = main_window.winfo_geometry()[0], main_window.winfo_geometry()[1] #   Obtenemos el alto y ancho
main_window.resizable(False, False)

def selected(choice):
    print(choice)


def calcular_Trayectoria(velocidad, angulo):
    # Convierto el angulo a radians
    #los pasamos aradians por que asi es mas facil
    #trabajar con los angulos de mas adelante
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
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.plot(Altura_maximo_tiempo, Altura_Maxima)
    ax.axhline(y=Altura_Maxima, xmin=0.0, xmax=1.0, color='r')
    ax.set_xlabel('Distancia (Metros)')
    ax.set_ylabel('Altura (Metros)')
    ax.set_title('Simulación del proyectil')
    return fig

#________________________________________________________________________________________________________

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



# https://customtkinter.tomschimansky.com/documentation/widgets/entry
# https://customtkinter.tomschimansky.com/documentation/widgets/textbox



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
    fig = mostrar_Trayectoria(temp1[0], temp1[1], temp1[2], temp1[3])



    # Crear un lienzo de Matplotlib para Tkinter
    lienzo = FigureCanvasTkAgg(fig, master=graphic_frame)
    lienzo.get_tk_widget().place(x = 2, y = 2)
    return

b_3 = ctk.CTkButton(buttons_frame, width=60, height=8, command=calculofinal, text = 'Aceptar')
b_3.grid(row=5, column=1, padx=2, pady=8, sticky="nw")


def on_submit():
    global velocity_entry, angle_entry
   
    velocidad = float(velocity_entry.get())
    angulo= float(angle_entry.get())

    x, y, Altura_maxima, Altura_maxima_tiempo= calcular_Trayectoria(velocidad, angulo)
    mostrar_Trayectoria(x, y, Altura_maxima, Altura_maxima_tiempo)

    
# Generar el gráfico utilizando la función generate_plot()


#   temp1 = calcular_Trayectoria(angle_entry.get(), velocity_entry.get())

#   Loop principal de la Ventana    #
main_window.mainloop()