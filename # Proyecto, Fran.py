# Proyecto, Fran

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import customtkinter as ctk


#----DEFINIMOS LA VENTANA PRINCIPAL Y SUS TAMAÑOS-------------------------------------------------------#
main_window = ctk.CTk()                                                                                #   Asignamos las propiedades de ctk.Ctk a main_window
main_window.title("Tiro Parabolico")                                                                            #   Ponemos nombre a la ventanita creada
main_window.geometry("900x600")                                                                         #   Definimos la resolucion de la ventana
main_window_width, main_window_height = main_window.winfo_geometry()[0], main_window.winfo_geometry()[1] #   Obtenemos el alto y ancho
main_window.resizable(False, False)
num_parts = 5



#-----------------DEFINIMOS FUNCIONES--------------------------------------------------------------#
def selected(choice):
    print(choice)

def calcular_Trayectoria(velocidad, angulo):
    # Convierto el angulo a radians
    #los pasamos aradians por que asi es mas facil
    #trabajar con los angulos de mas adelante
    angle_rad = np.deg2rad(angulo)

    # Calculo el tiempo de vuelo
    tiempo_de_vuelo = (2 * velocidad * np.sin(angle_rad)) / 9.8 #Ecuación Tiempo de vuelo

    # Calculo el timpo en intervalos
    t = np.linspace(0, tiempo_de_vuelo, num=100)

    # Calculo el "x" y "y" posiciones en cada  intervalo del tiempo
    x = velocidad * np.cos(angle_rad) * t #Ecuación para la Posición
    y = velocidad * np.sin(angle_rad) * t - 0.5 * 9.8 * t ** 2 #Ecuación de Itinerario

    # Encuentra la altura maxima y el tiempo correspondiente
    Altura_maxima = np.max(y)
    Altura_maximo_tiempo = t[np.argmax(y)]

    return x, y, Altura_maxima, Altura_maximo_tiempo

#--CALCULAMOS EL GRAFICO CON MATPLOTLIB------------------------------#
def mostrar_Trayectoria(x, y, Altura_Maxima, Altura_maximo_tiempo, ):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.plot(Altura_maximo_tiempo, Altura_Maxima)
    ax.axhline(y=Altura_Maxima, xmin=0.0, xmax=1.0, color='r')
    ax.set_xlabel('Distancia (Metros)')
    ax.set_ylabel('Altura (Metros)')
    ax.set_title('Simulación del proyectil')

    ax.text(Altura_maximo_tiempo, Altura_Maxima, f'Altura: {Altura_Maxima:.2f} metros',
        verticalalignment='bottom', horizontalalignment='right', color='b', fontsize=10)
    
    return fig


#-----PARTE "SIGUIENTE" EM LA DEMOSTRACION DEL TIRO------------#
def next_part():
    current_part = int(btn_next["text"].split('/')[0]) - 1
    if current_part < num_parts:
        current_part += 1
        btn_prev["state"] = ctk.NORMAL
        if current_part == num_parts:
            btn_next["state"] = ctk.DISABLED
        btn_next["text"] = f"{current_part+1}/{num_parts+1}"
        update_plot(current_part)
    return


#-----PARTE "PREVIA" DE LA DEMOSTRACION DEL TIRO(atras)------#
def prev_part():
    current_part = int(btn_next["text"].split('/')[0]) - 1
    if current_part > 0:
        current_part -= 1
        btn_next["state"] = ctk.NORMAL
        if current_part == 0:
            btn_prev["state"] = ctk.DISABLED
        btn_next["text"] = f"{current_part+1}/{num_parts+1}"
        update_plot(current_part)
    return


#------REALIZAMOS LOS CALCULOS PARA EL BOTON "GRAFICAR"--------------#
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
    lienzo.draw()
    return 


#------ACTUALIZAMOS LOS LIENZOS--------------#
def update_plot(part):
    global lienzo, ax, x, y
    line, = ax.plot([], [], 'o-')
    line.set_data(x[:part+1], y[:part+1])
    lienzo.draw()
    return


#----------RECOLECTA LOS DATOS PARA HACER LOS CALCULOS----------------------------------#
def on_submit():
    global velocity_entry, angle_entry
   
    velocidad = float(velocity_entry.get())
    angulo= float(angle_entry.get())

    x, y, Altura_maxima, Altura_maxima_tiempo= calcular_Trayectoria(velocidad, angulo)
    mostrar_Trayectoria(x, y, Altura_maxima, Altura_maxima_tiempo)



#--------------------------GRAFICOS/ENTRADAS/BOTONES------------------------------------------------------#

graphic_frame = ctk.CTkFrame(main_window, width=643, height=480)    #Frame para el gráfico  "graphic_frame"
graphic_frame.grid(row=0, column=1, pady=20)                        #Posicionamiento del frame para gráficos

buttons_frame = ctk.CTkFrame(main_window, width=800, height=450)    #Frame para Botones/textboxes   "buttons_frame"
buttons_frame.grid(row=0, column=0, padx=20, pady=10)               #Posicionamiento del frame para los botones/texboxes

#-------------------------ENTRADA DE DATO=VELOCIDAD--------------------------------------------------------#
txt1label = ctk.CTkLabel(buttons_frame, width=10, height=20, text="Velocidad Inicial:", font=ctk.CTkFont(size=12, weight="normal"))    #Crear texto dentro de buttons_frame
txt1label.grid(row=0, column=0, columnspan=2, pady=15, sticky="sew")                                                               #Posicionamiento del texto dentro de buttons_frame

angle_entry = ctk.CTkEntry(buttons_frame, width=60, height=12)                                                 #Textbox para almacenar valores
angle_entry.grid(row=1, column=0, padx=2, pady=5, sticky="ne")                                                                             #Posicion de la textbox

b_1 = ctk.CTkSegmentedButton(buttons_frame,width=60, height=10 , values=["m/s"])                         #Segmented button, para 2 botones en 1
b_1.grid(row=1, column=1, padx=2, pady=8, sticky="nw")                                                                               #Posicion y config del segmented button
b_1.set("m/s")

#-------------------------ENTRADA DE DATO=ANGULÓ-----------------------------------------------------------#
txt_2_label = ctk.CTkLabel(buttons_frame, width=5, height=10, text="Angulo de Lanzamiento:", font=ctk.CTkFont(size=12, weight="normal"))
txt_2_label.grid(row=3, column=0, columnspan=2, pady=15, sticky="sew")

velocity_entry = ctk.CTkEntry(buttons_frame, width=60, height=8)
velocity_entry.grid(row=4, column=0, padx=2, pady=5, sticky="ne")

b_2 = ctk.CTkSegmentedButton(buttons_frame,width=60, height=10 , values=["β"])
b_2.grid(row=4, column=1, padx=2, pady=8, sticky="nw")
b_2.set("β") 

#-------------------------CREACION DEL BOTON=GRAFICAR-------------------------------------------------------#
b_3 = ctk.CTkButton(buttons_frame, width=60, height=8, command=calculofinal, text = 'Graficar')
b_3.grid(row=5, column=1, padx=2, pady=8, sticky="nw")

#-------------------------CREACION DEL BOTON=ANTERIOR-------------------------------------------------------#
btn_prev = ctk.CTkButton(main_window, text="Anterior", command=prev_part, state=ctk.DISABLED)
btn_prev.grid(row = 1, column = 1, padx = 50, columnspan=2, sticky='w')

#-------------------------CREACION DEL BOTON=SIGUIENTE------------------------------------------------------#
btn_next = ctk.CTkButton(main_window, text="Siguiente", command=next_part)
btn_next.grid(row = 1, column = 1, padx = 40, columnspan=2, sticky='e' )

plot_buttons = ctk.CTkFrame(main_window, width=740, height=200)
plot_buttons.grid(row=1, column=1, padx=20, pady=10)

#------------------------INGRESAMOS UN TEXTO CON LA FORMULA--------------------------------------------------#


#--------MAIN LOOP-----------------#
main_window.mainloop()