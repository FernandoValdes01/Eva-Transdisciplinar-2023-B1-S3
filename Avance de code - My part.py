import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

main_window = ctk.CTk()                                                                                #   Asignamos las propiedades de ctk.Ctk a main_window
main_window.title("Tiro Parabolico")                                                                            #   Ponemos nombre a la ventanita creada
main_window.geometry("900x600")                                                                         #   Definimos la resolucion de la ventana
main_window_width, main_window_height = main_window.winfo_geometry()[0], main_window.winfo_geometry()[1] #   Obtenemos el alto y ancho
main_window.resizable(False, False)

graphic_frame = ctk.CTkFrame(main_window, width=643, height=480)    #Frame para el gráfico  "graphic_frame"
graphic_frame.grid(row=0, column=1, pady=20) 


# Parámetros del tiro parabólico
#g = 9.8  # Aceleración gravitacional
#v0 = velocity_entry  # Velocidad inicial
#angle = 45  # Ángulo de lanzamiento

buttons_frame = ctk.CTkFrame(main_window, width=800, height=450)    #Frame para Botones/textboxes   "buttons_frame"
buttons_frame.grid(row=0, column=0, padx=20, pady=10)

txt1label = ctk.CTkLabel(buttons_frame, width=10, height=20, text="Velocidad Inicial:", font=ctk.CTkFont(size=12, weight="normal"))    #Crear texto dentro de buttons_frame
txt1label.grid(row=0, column=0, columnspan=2, pady=15, sticky="sew")                                                               #Posicionamiento del texto dentro de buttons_frame

angle_entry = ctk.CTkEntry(buttons_frame, width=60, height=12)                                         #Textbox para almacenar valores
angle_entry.grid(row=1, column=0, padx=2, pady=5, sticky="ne")

txt_2_label = ctk.CTkLabel(buttons_frame, width=5, height=10, text="Angulo de Lanzamiento:", font=ctk.CTkFont(size=12, weight="normal"))
txt_2_label.grid(row=3, column=0, columnspan=2, pady=15, sticky="sew")
velocity_entry = ctk.CTkEntry(buttons_frame, width=60, height=8)
velocity_entry.grid(row=4, column=0, padx=2, pady=5, sticky="ne")

# Cálculo de las trayectorias en 5 partes
# Parámetros del tiro parabólico
g = 9.8  # Aceleración gravitacional
v0 = 2 # Velocidad inicial
angle = 90 # Ángulo de lanzamiento


num_parts = 10
dt = 2 * v0* (1 / g) / num_parts
t = 0
x = []
y = []
for _ in range(num_parts + 1):
    x.append(v0 * t * (1))
    y.append(v0 * t * (1) - 0.5 * g * t**2)
    t += dt


# Crear figura de Matplotlib
def calcular_Trayectoria(velocidad, angulo):
    # Convierto el angulo a radians
    #los pasamos aradians por que asi es mas facil
    #trabajar con los angulos de mas adelante
    angle_rad = np.deg2rad(angulo)

    # Calculo el tiempo de vuelo
    tiempo_de_vuelo = (2 * velocidad * np.sin(angle_rad)) / 9.8 #Ecuación Tiempo de vuelo

    # Calculo el timpo en intervalos
    t = np.linspace(0, tiempo_de_vuelo, num=10)

    # Calculo el "x" y "y" posiciones en cada  intervalo del tiempo
    x = velocidad * np.cos(angle_rad) * t #Ecuación para la Posición
    y = velocidad * np.sin(angle_rad) * t - 0.5 * 9.8 * t ** 2 #Ecuación de Itinerario

    # Encuentra la altura maxima y el tiempo correspondiente
    Altura_maxima = np.max(y)
    Altura_maximo_tiempo = t[np.argmax(y)]

    return x, y, Altura_maxima, Altura_maximo_tiempo





# Funciones para actualizar el gráfico
def mostrar_plot(x, y, Altura_Maxima, Altura_maximo_tiempo,part):
    fig, ax= plt.subplots()
    #ax.plot(x, y)
    ax.plot(Altura_maximo_tiempo, Altura_Maxima)
    ax.axhline(y=Altura_Maxima, xmin=0.0, xmax=1.0, color='r')
    ax.set_xlabel('Distancia (Metros)')
    ax.set_ylabel('Altura (Metros)')
    ax.set_title(f"Simulación tiro parabólico")

    line, = ax.plot(x, y, 'b')
    line.set_data(x[:part+1], y[:part+1])

    return fig 


#fig = Figure(figsize=(5, 4), dpi=100)
#ax = fig.add_subplot(1, 1, 1)
#ax.set_xlabel('Distancia (m)')
#ax.set_ylabel('Altura (m)')
#ax.set_xlim(0, max(x) * 1.1)
#ax.set_ylim(0, max(y) * 1.1)


current_part = 0
current_part_2 = 1

def next_part():
    
    global current_part, angle_entry, velocity_entry
    angle = float(angle_entry.get())
    velocity = float(velocity_entry.get())
    
    temp1 = calcular_Trayectoria(angle, velocity)

    if current_part < num_parts:
        current_part += 1
    
    fig = mostrar_plot(temp1[0], temp1[1], temp1[2], temp1[3], current_part)
    
    canvas = FigureCanvasTkAgg(fig, master=graphic_frame)
    canvas.get_tk_widget().place(x = 2, y = 2)
    canvas.draw()   
        
    return

def prev_part():
    global current_part, angle_entry, velocity_entry
    angle = float(angle_entry.get())
    velocity = float(velocity_entry.get())
    
    temp1 = calcular_Trayectoria(angle, velocity)

    if current_part > 0:
        current_part -= 1

    fig = mostrar_plot(temp1[0], temp1[1], temp1[2], temp1[3], current_part)
    
    canvas = FigureCanvasTkAgg(fig, master=graphic_frame)
    canvas.get_tk_widget().place(x = 2, y = 2)
    canvas.draw()    
    return 

# Agregar el gráfico a la ventana Tkinter

def calculofinal():
    global angle_entry, velocity_entry, current_part

    angle = float(angle_entry.get())
    velocity = float(velocity_entry.get())
    
    temp1 = calcular_Trayectoria(angle, velocity)
    print(temp1)
    fig = mostrar_plot(temp1[0], temp1[1], temp1[2], temp1[3], current_part)
    
    canvas = FigureCanvasTkAgg(fig, master=graphic_frame)
    canvas.get_tk_widget().place(x = 2, y = 2)
    canvas.draw()
    return



b_3 = ctk.CTkButton(buttons_frame, width=60, height=8, command=calculofinal, text = 'Graficar')
b_3.grid(row=5, column=1, padx=2, pady=8, sticky="nw")

# Agregar los botones
btn_prev = ctk.CTkButton(main_window, text="Anterior", command=prev_part)
btn_prev.grid(row = 1, column = 1, padx = 50, columnspan=2, sticky='w')
btn_next = ctk.CTkButton(main_window, text="Siguiente", command=next_part)
btn_next.grid(row = 1, column = 1, padx = 40, columnspan=2, sticky='e' )

# Mostrar el primer tiro parabólico
#update_plot(0)

# Ejecutar la interfaz
main_window.mainloop()
