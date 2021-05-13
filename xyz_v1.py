# 09.05.2021

import tkinter as tk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)

from matplotlib.figure import Figure

root = tk.Tk()
root.title("XYZ CARTESIAN COORDINATE SIMULATOR")

fig = Figure()
canvas = FigureCanvasTkAgg(fig, master=root)
plt = fig.add_subplot(projection='3d')

pos_x = 0
pos_y = 0
pos_z = 0

def aa():
    print("aa")

def ciz(xx, yy, zz):
    plt.cla()

    plt.set_xlabel("X")
    plt.set_ylabel("Y")
    plt.set_zlabel("Z")

    x = [235, -235]
    y = [-235, -235]
    z = [-235, -235]

    x1 = [-235, 235]
    y1 = [235, 235]
    z1 = [-235, -235]

    x2 = [0, 0]
    y2 = [235, 235]
    z2 = [-235, 235]

    x3 = [0, 0]
    y3 = [-235, -235]
    z3 = [-235, 235]

    x4 = [0, 0]
    y4 = [235, -235]
    z4 = [0, 0]

    plt.plot3D(x, y, z, c="b")
    plt.plot3D(x1, y1, z1, c="b")
    plt.plot3D(x2, y2, z2, c="g")
    plt.plot3D(x3, y3, z3, c="g")
    plt.plot3D(x4, y4, z4)

    plt.plot(xx, yy, zz, 'ro')
    # i+=10
    canvas.draw()

x_label = tk.Label(text="X", font="times 15")
x_width = tk.Entry(root)
x_label.pack()
x_width.pack()

y_label = tk.Label(text="Y", font="times 15")
y_width = tk.Entry(root)
y_label.pack()
y_width.pack()

z_label = tk.Label(text="Z", font="times 15")
z_width = tk.Entry(root)
z_label.pack()
z_width.pack()

x_width.insert(0, 20)
y_width.insert(0, 20)
z_width.insert(0, 20)

button = tk.Button(text="Click me!", command=lambda: ciz(int(x_width.get()), int(y_width.get()), int(z_width.get())))
button.pack()

canvas.get_tk_widget().pack()

# ciz(pos_x, pos_y, pos_z)

root.mainloop()
