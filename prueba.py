import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Parámetros del tiro parabólico
g = 9.8  # Aceleración gravitacional
v0 = 20  # Velocidad inicial
angle = 90  # Ángulo de lanzamiento

# Cálculo de las trayectorias en 5 partes
num_parts = 5
dt = 2 * v0 * (1 / g) / num_parts
t = 0
x = []
y = []
for _ in range(num_parts + 1):
    x.append(v0 * t * (1))
    y.append(v0 * t * (1) - 0.5 * g * t**2)
    t += dt

# Crear ventana Tkinter
root = tk.Tk()
root.title("Tiro parabólico")

# Crear figura de Matplotlib
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Distancia (m)')
ax.set_ylabel('Altura (m)')
ax.set_xlim(0, max(x) * 1.1)
ax.set_ylim(0, max(y) * 1.1)
line, = ax.plot([], [], 'o-')

# Funciones para actualizar el gráfico
def update_plot(part):
    line.set_data(x[:part+1], y[:part+1])
    ax.set_title(f"Tiro parabólico - Parte {part+1}/{num_parts+1}")
    canvas.draw()

def next_part():
    current_part = int(btn_next["text"].split('/')[0]) - 1
    if current_part < num_parts:
        current_part += 1
        btn_prev["state"] = tk.NORMAL
        if current_part == num_parts:
            btn_next["state"] = tk.DISABLED
        btn_next["text"] = f"{current_part+1}/{num_parts+1}"
        update_plot(current_part)

def prev_part():
    current_part = int(btn_next["text"].split('/')[0]) - 1
    if current_part > 0:
        current_part -= 1
        btn_next["state"] = tk.NORMAL
        if current_part == 0:
            btn_prev["state"] = tk.DISABLED
        btn_next["text"] = f"{current_part+1}/{num_parts+1}"
        update_plot(current_part)

# Agregar el gráfico a la ventana Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Agregar los botones
btn_prev = tk.Button(root, text="Anterior", command=prev_part, state=tk.DISABLED)
btn_prev.pack(side=tk.LEFT)
btn_next = tk.Button(root, text="1/6", command=next_part)
btn_next.pack(side=tk.LEFT)

# Mostrar el primer tiro parabólico
update_plot(0)

# Ejecutar la interfaz
tk.mainloop()
