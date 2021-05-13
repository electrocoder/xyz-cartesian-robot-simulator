# 09.05.2021
# python 3.9

import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


root = tkinter.Tk()
root.wm_title("XYZ Cartesian Robot")

fig = Figure(figsize=(5, 4), dpi=100)
plt = fig.add_subplot(projection='3d')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def cartesian():
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


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()
    root.destroy()


def _draw():
    plt.cla()

    cartesian()

    plt.plot(int(x_width.get()), int(y_width.get()), int(z_width.get()), 'ro')

    canvas.draw()


x_label = tkinter.Label(master=root, text="X", font="times 15")
x_width = tkinter.Entry(master=root)
x_label.pack()
x_width.pack()

y_label = tkinter.Label(master=root, text="Y", font="times 15")
y_width = tkinter.Entry(master=root)
y_label.pack()
y_width.pack()

z_label = tkinter.Label(master=root, text="Z", font="times 15")
z_width = tkinter.Entry(master=root)
z_label.pack()
z_width.pack()

x_width.insert(0, 0)
y_width.insert(0, 0)
z_width.insert(0, 0)

button = tkinter.Button(master=root, text="Draw", command=_draw)
button.pack()

button1 = tkinter.Button(master=root, text="Quit", command=_quit)
button1.pack()

cartesian()

tkinter.mainloop()

