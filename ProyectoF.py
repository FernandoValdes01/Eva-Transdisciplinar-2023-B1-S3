#----------------IMPORTAMOS LIBRERIAS---------------------------#
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import webbrowser
import math

#-------------------------------VENTANA PRINCIPAL---------------#
main_window = ctk.CTk()                                                                                #   Asignamos las propiedades de ctk.Ctk a main_window
main_window.title("Tiro Parabolico")                                                                   #   Ponemos nombre a la ventanita creada
main_window.geometry("900x600")                                                                         #   Definimos la resolucion de la ventana
main_window_width, main_window_height = main_window.winfo_geometry()[0], main_window.winfo_geometry()[1] #   Obtenemos el alto y ancho
main_window.resizable(False, False)


#-----------------------------FUNCIONES Y CALCULOS----------------#

num_parts = 35


#--------CALCULAMOS NUESTRA TRAYECTORIA PRINCIPA--------------------------------------#
def calcular_Trayectoria(velocidad, angulo):
    # Convierto el angulo a radians
    #los pasamos aradians por que asi es mas facil
    #trabajar con los angulos de mas adelante
    global x_entry, y_entry,g_entry
    g = float(g_entry.get())
    posicion_x = float(x_entry.get())
    posicion_y = float(y_entry.get())
    
    angle_rad = np.deg2rad(angulo)

    # Calculo el tiempo de vuelo
    #ax**2 + bx+ c, defino a,b y c para utilizar la formula
    a = 0.5 * g #Defino a
    b = -velocidad * np.sin(angle_rad) #Defino b
    c = -posicion_y #Defino c
    
    discriminante = b**2 - 4 *a * c #Discriminante utilizado para saber si existe solucion
    if posicion_y < 0:
        print("Error de entrada en posicion y, debe ser mayor o igual a 0")
        exit()
    if g<=0:
        print("Error de entrada en Gravedad, debe ser positivo")
        exit()

    #Raices posibles
    raiz_1 = float( (-b + math.sqrt(discriminante)) / (2 * a))
    raiz_2 = float( (-b - math.sqrt(discriminante)) / (2 * a))
    if raiz_1 >= raiz_2:
        tiempo_de_vuelo = raiz_1 
    elif raiz_2 >= raiz_1:
        tiempo_de_vuelo = raiz_2
    # Calculo el timpo en intervalos
    t = np.linspace(0, tiempo_de_vuelo, num=35)

    # Calculo el "x" y "y" posiciones en cada  intervalo del tiempo
    x = posicion_x + velocidad * np.cos(angle_rad) * t #Ecuación para la Posición en eje X
    y = posicion_y + velocidad * np.sin(angle_rad) * t - 0.5 * g * t ** 2 #Ecuación de Itinerario

    # Encuentra la altura maxima y el tiempo correspondiente
    Altura_maxima = np.max(y)
    Altura_maximo_tiempo = t[np.argmax(y)]
    return x, y, Altura_maxima, Altura_maximo_tiempo


#--------------------MOSTRAMOS GRAFICO CON MATPLOTLIB-------------------------------#
def mostrar_plot(x, y, Altura_Maxima, Altura_maximo_tiempo,part):
    fig, ax= plt.subplots()
    #ax.plot(x, y)
    ax.plot(Altura_maximo_tiempo, Altura_Maxima)
    ax.axhline(y=Altura_Maxima, xmin=0.0, xmax=1.0, color='r')
    ax.set_xlabel('Distancia (Metros(MRUA))')
    ax.set_ylabel('Altura (Metros(MRU))')
    ax.set_title(f"Simulación tiro parabólico")
    ax.text(Altura_maximo_tiempo, Altura_Maxima, f'Altura: {Altura_Maxima:.2f} metros',
    verticalalignment='bottom', horizontalalignment='left', color='r', fontsize=9)
    global line
    line, = ax.plot(x, y, 'b')
    line.set_data(x[:part+1], y[:part+1])

    return fig 

#-------DIBUJAR PARTES DEL GRAFICO------------------#
current_part = 0

#----CALCULA LA SIGUIENTE PARTE DEL GRAFICO------#
def next_part():
    
    global current_part, angle_entry, velocity_entry, line, canvas
    angle = float(angle_entry.get())
    velocity = float(velocity_entry.get())
    
    temp1 = calcular_Trayectoria(angle, velocity)
    x = temp1[0]
    y = temp1[1]

    if current_part < num_parts:
        current_part += 3
    
    #Actualizamos la linea del grafico
    line.set_xdata(x[:current_part+1])
    line.set_ydata(y[:current_part+1])
    plt.draw()
    canvas.draw()  
        
    return


#------CALCULA LA PARTE PREVIA DEL GRAFICO---------------#
def prev_part():
    global current_part, angle_entry, velocity_entry, line, canvas
    angle = float(angle_entry.get())
    velocity = float(velocity_entry.get())
    
    temp1 = calcular_Trayectoria(angle, velocity)
    x = temp1[0]
    y = temp1[1]

    if current_part > 0:
        current_part -= 3
    #Actualizamos la linea del grafico
    line.set_xdata(x[:current_part+1])
    line.set_ydata(y[:current_part+1])
    plt.draw()
    canvas.draw()  
    return 

#-----SE REALIZA CALCULO FINAL PARA EL GRAFICO-----------#
def calculofinal():
    global angle_entry, velocity_entry, current_part, canvas

    angle = float(angle_entry.get())
    velocity = float(velocity_entry.get())
    
    temp1 = calcular_Trayectoria(angle, velocity)
    fig = mostrar_plot(temp1[0], temp1[1], temp1[2], temp1[3], current_part)
    
    canvas = FigureCanvasTkAgg(fig, master=graphic_frame)
    canvas.get_tk_widget().place(x = 2, y = 2)
    canvas.draw()
    return

#---------FUNCION DEL VIDEO DE YOUTUBE--------------------------------------------------#
def reproducir_video():
    url = "https://www.youtube.com/watch?v=2DJDTtIazgA"  
    webbrowser.open(url)

#---------------------------------GRAFICOS;BOTONES;ENTRADAS------------------------------------------------#
#------------------------------------LUGAR DEL GRAFICO-----------------------------------------------------#
graphic_frame = ctk.CTkFrame(main_window, width=643, height=480)    #Frame para el gráfico  "graphic_frame"
graphic_frame.grid(row=0, column=1, pady=20)


#---------------------------------LUGAR DE ENTRADA DE DATOS------------------------------------------------#
buttons_frame = ctk.CTkFrame(main_window, width=800, height=450)    #Frame para Botones/textboxes   "buttons_frame"
buttons_frame.grid(row=0, column=0, padx=20, pady=10)


#---------------------------------ENTRADA DE DATO=VELOCIDAD------------------------------------------------#
txt1label = ctk.CTkLabel(buttons_frame, width=50, height=20, text="Velocidad Inicial:", font=ctk.CTkFont(size=12, weight="normal"))    #Crear texto dentro de buttons_frame
txt1label.grid(row=0, column=0, columnspan=2, pady=15, sticky="we")                                                               #Posicionamiento del texto dentro de buttons_frame
velocity_entry = ctk.CTkEntry(buttons_frame, width=50, height=20)
velocity_entry.grid(row=3, column=0,columnspan=2, padx=5, pady=5, sticky="ew")


#---------------------------------ENTRADA DE DATO=ANGULO---------------------------------------------------#
angle_entry = ctk.CTkEntry(buttons_frame, width=50, height=20)                                         #Textbox para almacenar valores
angle_entry.grid(row=1, column=0,columnspan=2, padx = 5, pady=5, sticky="we")
txt_2_label = ctk.CTkLabel(buttons_frame, width=50, height=10, text="Angulo:", font=ctk.CTkFont(size=12, weight="normal"))
txt_2_label.grid(row=2, column=0, columnspan=2, pady=15, sticky="we")

#---------------------------------ENTRADA DE DATO=POSICION_X-----------------------------------------------#
x_label = ctk.CTkLabel(buttons_frame, width=50, height=20, text="Posicion x:", font=ctk.CTkFont(size=12, weight="normal"))    #Crear texto dentro de buttons_frame
x_label.grid(row=4, column=0, columnspan=2, pady=15, sticky="we")                                                               #Posicionamiento del texto dentro de buttons_frame
x_entry = ctk.CTkEntry(buttons_frame, width=50, height=20)
x_entry.grid(row=5, column=0,columnspan=2, padx=5, pady=5, sticky="ew")

#---------------------------------ENTRADA DE DATO=POSICION_Y-----------------------------------------------#
y_label = ctk.CTkLabel(buttons_frame, width=50, height=20, text="Posicion y:", font=ctk.CTkFont(size=12, weight="normal"))    #Crear texto dentro de buttons_frame
y_label.grid(row=6, column=0, columnspan=2, pady=15, sticky="we")                                                              #Posicionamiento del texto dentro de buttons_frame
y_entry = ctk.CTkEntry(buttons_frame, width=50, height=20)
y_entry.grid(row=7, column=0,columnspan=2, padx=5, pady=5, sticky="ew")

#---------------------------------ENTRADA DE DATO=GRAVEDAD-----------------------------------------------#
g_label = ctk.CTkLabel(buttons_frame, width=50, height=20, text="Gravedad:", font=ctk.CTkFont(size=12, weight="normal"))    #Crear texto dentro de buttons_frame
g_label.grid(row=8, column=0, columnspan=2, pady=15, sticky="we")                                                              #Posicionamiento del texto dentro de buttons_frame
g_entry = ctk.CTkEntry(buttons_frame, width=50, height=20)
g_entry.grid(row=9, column=0,columnspan=2, padx=5, pady=5, sticky="ew")

#---------------------------------CREACION DEL BOTON=GRAFICAR----------------------------------------------#
b_3 = ctk.CTkButton(buttons_frame, width=60, height=8, command=calculofinal, text = 'Graficar')
b_3.grid(row=10, column=0,columnspan=2,padx=0, pady=0, sticky="we")


#---------------------------------CREACION DE LOS BOTONES A/S----------------------------------------------#
btn_prev = ctk.CTkButton(main_window, text="Anterior", command=prev_part)
btn_prev.grid(row = 1, column = 1, padx = 50, columnspan=2, sticky='w')
btn_next = ctk.CTkButton(main_window, text="Siguiente", command=next_part)
btn_next.grid(row = 1, column = 1, padx = 40, columnspan=2, sticky='e' )


#---------------------------------CREACION DEL BOTON "EJEMPLO"----------------------------------------------#
yt = ctk.CTkButton(main_window, text="Ejemplo", command=reproducir_video)
yt.grid(row = 1, column = 1, padx = 25, columnspan=2, sticky='s')

# Ejecutar la interfaz
main_window.mainloop()