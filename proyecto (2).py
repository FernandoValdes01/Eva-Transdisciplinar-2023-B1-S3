import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk


def calculate_trajectory(velocity, angle):
    # Convert the angle to radians
    angle_rad = np.deg2rad(angle)

    # Calculate the time of flight
    time_of_flight = (2 * velocity * np.sin(angle_rad)) / 9.8

    # Calculate the time intervals
    t = np.linspace(0, time_of_flight, num=100)

    # Calculate the x and y positions at each time interval
    x = velocity * np.cos(angle_rad) * t
    y = velocity * np.sin(angle_rad) * t - 0.5 * 9.8 * t ** 2

    # Find the maximum height and corresponding time
    max_height = np.max(y)
    max_height_time = t[np.argmax(y)]

    return x, y, max_height, max_height_time


def plot_trajectory(x, y, max_height, max_height_time):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.plot(max_height_time, max_height, 'ro')
    ax.set_xlabel('Distance (m)')
    ax.set_ylabel('Height (m)')
    ax.set_title('Projectile Motion')
    plt.show()


def on_submit():
    velocity = float(velocity_entry.get())
    angle = float(angle_entry.get())

    x, y, max_height, max_height_time = calculate_trajectory(velocity, angle)
    plot_trajectory(x, y, max_height, max_height_time)


# Create the GUI window
window = tk.Tk()
window.title("Projectile Motion")
window.configure(bg='black')

# Create the velocity input label and entry
velocity_label = tk.Label(window, text="Initial Velocity (m/s):", fg='white', bg='black')
velocity_label.pack()
velocity_entry = tk.Entry(window)
velocity_entry.pack()

# Create the angle input label and entry
angle_label = tk.Label(window, text="Launch Angle (degrees):", fg='white', bg='black')
angle_label.pack()
angle_entry = tk.Entry(window)
angle_entry.pack()

# Create the submit button
submit_button = tk.Button(window, text="Submit", command=on_submit)
submit_button.pack()

# Run the GUI event loop
window.mainloop()
