import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
import webbrowser

#-------------------------------VENTANA PRINCIPAL---------------#
main_window = ctk.CTk()
main_window.title("Tiro Parabolico")
main_window.geometry("900x600")
main_window_width, main_window_height = main_window.winfo_geometry()[0], main_window.winfo_geometry()[1]
main_window.resizable(False, False)


#-----------------------------FUNCIONES Y CALCULOS----------------#

num_parts = 35
current_part = 0
toolbar = None

def Reset():
    toolbar.home()

def Zoom():
    toolbar.zoom()

def Guardar():
    global current_part, angle_entry, velocity_entry, toolbar
    angle = float(angle_entry.get())
    velocity = float(velocity_entry.get())
    temp1 = calcular_Trayectoria(angle, velocity)
    current_part = (num_parts - 1) if num_parts > 0 else 0  # Guardar la última parte generada
    fig = mostrar_plot(temp1[0], temp1[1], temp1[2], temp1[3], current_part)
    canvas = FigureCanvasTkAgg(fig, master=graphic_frame)
    canvas.get_tk_widget().place(x=2, y=2)
    canvas.draw()
    toolbar.update()  # Actualizar la barra de herramientas
    toolbar.save_figure() 
# Luego, en algún lugar de tu código, puedes llamar a esta función cuando se presione el botón de guardar.

    

def calcular_Trayectoria(velocidad, angulo):
    angle_rad = np.deg2rad(angulo)
    tiempo_de_vuelo = (2 * velocidad * np.sin(angle_rad)) / 9.8
    t = np.linspace(0, tiempo_de_vuelo, num=35)
    x = velocidad * np.cos(angle_rad) * t
    y = velocidad * np.sin(angle_rad) * t - 0.5 * 9.8 * t ** 2
    Altura_maxima = np.max(y)
    Altura_maximo_tiempo = t[np.argmax(y)]
    return x, y, Altura_maxima, Altura_maximo_tiempo

def mostrar_plot(x, y, Altura_Maxima, Altura_maximo_tiempo, part):
    fig, ax = plt.subplots()
    ax.plot(Altura_maximo_tiempo, Altura_Maxima)
    ax.axhline(y=Altura_Maxima, xmin=0.0, xmax=1.0, color='r')
    ax.set_xlabel('Distancia (Metros(MRUA))')
    ax.set_ylabel('Altura (Metros(MRU))')
    ax.set_title(f"Simulación tiro parabólico")
    ax.text(
        Altura_maximo_tiempo, Altura_Maxima, f'Altura: {Altura_Maxima:.2f} metros',
        verticalalignment='bottom', horizontalalignment='left', color='r', fontsize=9
    )
    line, = ax.plot(x, y, 'b')
    line.set_data(x[:part + 1], y[:part + 1])
    return fig


def next_part():
    global current_part, angle_entry, velocity_entry
    angle = float(angle_entry.get())
    velocity = float(velocity_entry.get())
    temp1 = calcular_Trayectoria(angle, velocity)
    if current_part < num_parts:
        current_part += 3
    fig = mostrar_plot(temp1[0], temp1[1], temp1[2], temp1[3], current_part)
    canvas = FigureCanvasTkAgg(fig, master=graphic_frame)
    canvas.get_tk_widget().place(x=2, y=2)
    canvas.draw()
    return


def prev_part():
    global current_part, angle_entry, velocity_entry
    angle = float(angle_entry.get())
    velocity = float(velocity_entry.get())
    temp1 = calcular_Trayectoria(angle, velocity)
    if current_part > 0:
        current_part -= 3
    fig = mostrar_plot(temp1[0], temp1[1], temp1[2], temp1[3], current_part)
    canvas = FigureCanvasTkAgg(fig, master=graphic_frame)
    canvas.get_tk_widget().place(x=2, y=2)
    canvas.draw()
    return canvas


def calculofinal():
    global angle_entry, velocity_entry, current_part, toolbar
    angle = float(angle_entry.get())
    velocity = float(velocity_entry.get())
    temp1 = calcular_Trayectoria(angle, velocity)
    fig = mostrar_plot(temp1[0], temp1[1], temp1[2], temp1[3], current_part)
    canvas = FigureCanvasTkAgg(fig, master=graphic_frame)
    canvas.get_tk_widget().place(x=2, y=2)
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, graphic_frame)
    toolbar.update()
    toolbar.pack_forget()
    return toolbar


def reproducir_video():
    url = "https://www.youtube.com/watch?v=2DJDTtIazgA"
    webbrowser.open(url)

#---------------------------------GRAFICOS;BOTONES;ENTRADAS------------------------------------------------#
#------------------------------------LUGAR DEL GRAFICO-----------------------------------------------------#
graphic_frame = ctk.CTkFrame(main_window, width=643, height=480)
graphic_frame.grid(row=0, column=1, pady=20)


#---------------------------------LUGAR DE ENTRADA DE DATOS------------------------------------------------#
buttons_frame = ctk.CTkFrame(main_window, width=800, height=450)
buttons_frame.grid(row=0, column=0, padx=20, pady=10)

#---------------------------------LUGAR DE BOTONES DE FUNCIONES---------------------------------------------#
Botonesfuncionales = ctk.CTkFrame(main_window, width=740, height=200)
Botonesfuncionales.grid(row=1, column=1, padx=20, pady=10)

#---------------------------------ENTRADA DE DATO=VELOCIDAD------------------------------------------------#
txt1label = ctk.CTkLabel(buttons_frame, width=50, height=20, text="Velocidad Inicial:",
                         font=ctk.CTkFont(size=12, weight="normal"))
txt1label.grid(row=0, column=0, columnspan=2, pady=15, sticky="we")
velocity_entry = ctk.CTkEntry(buttons_frame, width=50, height=20)
velocity_entry.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")


#---------------------------------ENTRADA DE DATO=ANGULO---------------------------------------------------#
angle_entry = ctk.CTkEntry(buttons_frame, width=50, height=20)
angle_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="we")
txt_2_label = ctk.CTkLabel(buttons_frame, width=50, height=10, text="Angulo:",
                           font=ctk.CTkFont(size=12, weight="normal"))
txt_2_label.grid(row=2, column=0, columnspan=2, pady=15, sticky="we")


#---------------------------------CREACION DEL BOTON=GRAFICAR----------------------------------------------#
b_3 = ctk.CTkButton(buttons_frame, width=60, height=8, command=calculofinal, text='Graficar')
b_3.grid(row=5, column=0, columnspan=2, padx=0, pady=0, sticky="we")


#---------------------------------CREACION DE LOS BOTONES A/S----------------------------------------------#
btn_prev = ctk.CTkButton(main_window, text="Anterior", command=prev_part)
btn_prev.grid(row=1, column=1, padx=50, columnspan=2, sticky='w')
btn_next = ctk.CTkButton(main_window, text="Siguiente", command=next_part)
btn_next.grid(row=1, column=1, padx=40, columnspan=2, sticky='e')


#---------------------------------CREACION DEL BOTON "EJEMPLO"----------------------------------------------#
yt = ctk.CTkButton(main_window, text="Ejemplo", command=reproducir_video)
yt.grid(row=1, column=1, padx=25, columnspan=2, sticky='s')


#---------------------------------CREACION DE BOTONES DE NAVEGACION-----------------------------------------#

buttonreset = ctk.CTkButton(Botonesfuncionales, text="Reset Pos.", command=Reset)
buttonreset.grid(column=0, row=0, padx=5)

buttonzoom = ctk.CTkButton(Botonesfuncionales, text="Zoom", command=Zoom)
buttonzoom.grid(column=1, row=0, padx=5)

buttonsave = ctk.CTkButton(Botonesfuncionales, text="Guardar", command=Guardar)
buttonsave.grid(column=3, row=0, padx=5)

# Ejecutar la interfaz
main_window.mainloop()
