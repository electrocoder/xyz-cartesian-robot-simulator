# 11.05.2021
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

x_pos = 0
y_pos = 0
z_pos = 0


def cartesian():
    plt.cla()

    plt.set_xlabel("X")
    plt.set_ylabel("Y")
    plt.set_zlabel("Z")

    x_len = 100
    y_len = 200
    z_len = 100

    global x_pos
    global y_pos
    global z_pos

    # x
    xx = [x_len, -1 * x_len]
    xy = [-1 * x_len, -1 * x_len]
    xz = [-1 * x_len, -1 * x_len]

    xx1 = [-1 * x_len, x_len]
    xy1 = [x_len, x_len]
    xz1 = [-1 * x_len, -1 * x_len]

    # y
    yx = [x_pos, x_pos]
    yy = [x_len, x_len]
    yz = [-1 * x_len, y_len * 2]

    yx1 = [x_pos, x_pos]
    yy1 = [-1 * x_len, -1 * x_len]
    yz1 = [-1 * x_len, y_len * 2]

    # z
    zx = [x_pos, x_pos]
    zy = [-1 * x_len, x_len]
    zz = [y_len, y_len]

    # x
    plt.plot3D(xx, xy, xz, c="r")
    plt.plot3D(xx1, xy1, xz1, c="r")

    # y
    plt.plot3D(yx, yy, yz, c="b")
    plt.plot3D(yx1, yy1, yz1, c="b")

    # z
    plt.plot3D(zx, zy, zz)

    # z ball
    plt.plot(x_pos, y_pos, z_pos, 'ro')

    canvas.draw()


def on_key_press(event):
    global x_pos
    global y_pos
    global z_pos

    print("you pressed {}".format(event.key))
    # key_press_handler(event, canvas, toolbar)
    if event.key == "up":
        x_pos += 10
    elif event.key == "down":
        x_pos -= 10
    elif event.key == "left":
        y_pos -= 10
    elif event.key == "right":
        y_pos += 10
    elif event.key == "+":
        z_pos += 10
    elif event.key == "-":
        z_pos -= 10

    cartesian()


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()
    root.destroy()


def _draw():
    cartesian()


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
