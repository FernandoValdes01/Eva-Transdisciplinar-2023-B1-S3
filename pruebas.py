import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

def calcular_tiro_parabolico(velocidad_inicial, angulo, gravedad):
    # Convertir el ángulo a radianes
    angulo_rad = np.deg2rad(angulo)
    
    # Calcular las componentes horizontal y vertical de la velocidad inicial
    velocidad_inicial_x = velocidad_inicial * np.cos(angulo_rad)
    velocidad_inicial_y = velocidad_inicial * np.sin(angulo_rad)
    
    # Calcular el tiempo de vuelo
    tiempo_vuelo = (2 * velocidad_inicial_y) / gravedad
    
    # Calcular los intervalos de tiempo
    t = np.linspace(0, tiempo_vuelo, num=100)
    
    # Calcular las posiciones horizontal y vertical en cada intervalo de tiempo
    x = velocidad_inicial_x * t
    y = velocidad_inicial_y * t - 0.5 * gravedad * t**2
    
    # Devolver los resultados
    return x, y

def mostrar_grafico():
    # Obtener los datos ingresados por el usuario
    velocidad_inicial = float(entry_velocidad.get())
    angulo = float(entry_angulo.get())
    gravedad = float(entry_gravedad.get())
    
    # Calcular el tiro parabólico
    x, y = calcular_tiro_parabolico(velocidad_inicial, angulo, gravedad)
    
    # Mostrar el gráfico
    plt.plot(x, y)
    plt.xlabel('Distancia (m)')
    plt.ylabel('Altura (m)')
    plt.title('Tiro Parabólico')
    plt.grid(True)
    plt.show()
    
    # Habilitar el botón "Continuar"
    btn_continuar.config(state=tk.NORMAL)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Tiro Parabólico')

# Crear y posicionar los elementos en la ventana
lbl_velocidad = tk.Label(ventana, text='Velocidad inicial (m/s):')
lbl_velocidad.pack()
entry_velocidad = tk.Entry(ventana)
entry_velocidad.pack()

lbl_angulo = tk.Label(ventana, text='Ángulo de lanzamiento (grados):')
lbl_angulo.pack()
entry_angulo = tk.Entry(ventana)
entry_angulo.pack()

lbl_gravedad = tk.Label(ventana, text='Gravedad (m/s²):')
lbl_gravedad.pack()
entry_gravedad = tk.Entry(ventana)
entry_gravedad.pack()

btn_calcular = tk.Button(ventana, text='Calcular', command=mostrar_grafico)
btn_calcular.pack()

btn_continuar = tk.Button(ventana, text='Continuar', state=tk.DISABLED)
btn_continuar.pack()

# Iniciar la ventana principal
ventana.mainloop()
