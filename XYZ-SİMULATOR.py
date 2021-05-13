
from tkinter.filedialog import *

import tkinter as tk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import time
import threading

from matplotlib.figure import Figure
yaza = ""

def dosyasec():
    dosyaal=askopenfilename()
    global yaza
    yaza = dosyaal
    btdosyayaz.invoke()
    if dosyaal:
        yazi2.config(text=dosyaal)

    else:
        yazi2.config(text="File Not Selected")

def dosyayaz():
    satirsayisi = 0
    gcode = open(yaza, "r", encoding="utf-8")

    for i in gcode:
        satirsayisi += 1

    gcode = open(yaza, "r", encoding="utf-8")
    k = 0
    i = 0
    s = 0
    sayac1 = 0

    global corx
    corx =[]
    global cory
    cory = []
    global corz
    corz = []

    while k < satirsayisi:

        k += 1
        print(str(k) + ". satıra girdi-----------")
        global z
        z = gcode.readline()

        # print(z, end="")
        while i < len(z) + 1:

            print(str(k) + ".satırda")
            print(str(i) + ".indexe baktı")

            if z[i] == ";" or i == len(z) - 1:

                i = 0
                break

            elif z[i] == "Z":
                sayac2 = 0
                s = i

                while z[s] != " " and i < len(z) - 1:

                    i += 1
                    sayac2 += 1
                    s += 1
                i = i - sayac2

                corz.append(z[i + 1:i + sayac2])
            elif z[i] == "X":
                sayac2 = 0

                s = i

                while z[s] != " ":
                    sayac2 += 1
                    s = s + 1

                corx.append(z[i + 1:i + sayac2])

            elif z[i] == "Y":
                sayac2 = 0
                s = i


                while z[s] != " " and i < len(z) - 2:
                    i += 1
                    sayac2 += 1
                    s += 1
                i = i - sayac2

                cory.append(z[i + 1:i + sayac2])

            i += 1



    for ii in range(0, len(corx)):
        corx[ii] = float(corx[ii])
    for ii in range(0, len(cory)):
        try :
            cory[ii] = float(cory[ii])
        except ValueError:
            cory[ii] = cory[ii-1]

    for ii in range(0, len(corz)):
        corz[ii] = float(corz[ii])

    global corx_iter
    corx_iter = iter(corx)
    global cory_iter
    cory_iter = iter(cory)

    global corz_iter
    corz_iter = iter(corz)
    print("VAR OLAN TÜM X KORDİNATLARI :", end="")
    print(corx)
    print("VAR OLAN TÜM Y KORDİNATLARI :", end="")
    print(cory)
    print("VAR OLAN TÜM Z KODLARI :", end="")
    print(corz)


# --------------------------------------------------------------------------------------------------------------
form = tk.Tk()
form.state("zoomed")
fig = Figure()
canvas = FigureCanvasTkAgg(fig, master=form)
canvas.get_tk_widget().place(x=600, y=10)
a = fig.add_subplot(projection='3d')
form.title("XYZ CARTESIAN COORDINATE SIMULATOR")
t = 1
a.plot(5, 5)

a.set_xlabel("x koordinatı")
a.set_ylabel("y koordinatı")
a.set_zlabel("z koordinatı")

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

a.plot3D(x, y, z, c="b")
a.plot3D(x1, y1, z1, c="b")
a.plot3D(x2, y2, z2, c="g")
a.plot3D(x3, y3, z3, c="g")
a.plot3D(x4, y4, z4)

a.scatter(0, 0, 0, c="r", s=250)
a.scatter(0, -235, -235, c="b")
a.scatter(0, 235, -235, c="b")
a.scatter(0, -235, 0, c="g")
a.scatter(0, 235, 0, c="g")


def calistir():
    tt = threading.Thread(target=calisartik)
    tt.start()
def calisartik ():
    sayac4 = 0

    global g
    global speed2,speed3
    speed2 = giris1z.get()
    speed3 = float(speed2)
    global gcode1
    gcode1 = open(yaza, "r", encoding="utf-8")
    while sayac4 < len(corx) and sayac4 < len(cory) and sayac4 < len(corz):
        # print(type(speed3))
        time.sleep(speed3)
        g=gcode1.readline()
        listbox.insert(END,g)
        listbox.selection_clear(0, END)
        listbox.selection_set(listbox.size() - 1, listbox.size() - 1)
        listbox.see(END)
        sayac4 += 1
        goster1.invoke()

def noktabirgoster():

    kordinatx=int(axisentryx.get())
    kordinaty=int(axisentryy.get())
    kordinatz=int(axisentryz.get())
    kordinatxeksi=-(kordinatx)
    kordinatyeksi = -(kordinaty)
    kordinatzeksi = -(kordinatz)

    x = [kordinatx, kordinatxeksi]
    y = [kordinatxeksi, kordinatxeksi]
    z = [kordinatxeksi, kordinatxeksi]

    x1 = [kordinatxeksi, kordinatx]
    y1 = [kordinatx, kordinatx]
    z1 = [kordinatxeksi, kordinatxeksi]

    x2 = [0, 0]
    y2 = [kordinatx, kordinatx]
    z2 = [kordinatxeksi,kordinatx]

    x3 = [0, 0]
    y3 = [kordinatxeksi, kordinatxeksi]
    z3 = [kordinatxeksi, kordinatx]

    x4 = [0, 0]
    y4 = [kordinatx, kordinatxeksi]
    z4 = [0, 0]

    bas1 = next(corx_iter)
    bas2 = next(cory_iter)
    bas3 = next(corz_iter)

    fig = Figure()
    canvas = FigureCanvasTkAgg(fig, master=form)
    canvas.get_tk_widget().place(x=600, y=10)
    a = fig.add_subplot(projection='3d')
    t = 1
    a.plot(5, 5)
    a.set_xlabel("x koordinatı")
    a.set_ylabel("y koordinatı")
    a.set_zlabel("z koordinatı")

    x2 = []
    x2.append(bas1)
    x2.append(bas1)
    x3 = []
    x3.append(bas1)
    x3.append(bas1)
    x4 = []
    x4.append(bas1)
    x4.append(bas1)
    z4 = []
    z4.append(bas3)
    z4.append(bas3)

    a.plot3D(x, y, z, c="b")
    a.plot3D(x1, y1, z1, c="b")
    a.plot3D(x2, y2, z2, c="g")
    a.plot3D(x3, y3, z3, c="g")
    a.plot3D(x4, y4, z4)

    a.scatter(bas1, bas2, bas3, c="r", s=250)
    a.scatter(bas1, kordinatxeksi, kordinatxeksi, c="b")
    a.scatter(bas1, kordinatx, kordinatxeksi, c="b")
    a.scatter(bas1, kordinatxeksi, bas3, c="g")
    a.scatter(bas1, kordinatx, bas3, c="g")

speed = 0.3
label4 = tk.Label(text="SPEED:",
                  font="times 15"
                  )
label4.place(x=100, y=345)
giris1z = tk.Entry(form)
giris1z.insert(0,0.3)
giris1z.place(x=175, y=350)
axisentryx=tk.Entry(form)
axisentryx.place(x=150,y=375)
axisentryy=tk.Entry(form)
axisentryy.place(x=300,y=375)
axisentryz=tk.Entry(form)
axisentryz.place(x=450,y=375)
axislabel=tk.Label(text="AXİS WİDTH:",
                   font="times 15")
axislabel.place(x=25,y=370)
axislabel2=tk.Label(text="x",
                   font="times 15")

axislabel2.place(x=280,y=370)
axislabel3=tk.Label(text="x",
                   font="times 15")
axislabel3.place(x=430,y=370)
yazi = tk.Label(text="Plase Select Process File")
yazi.place(x=175, y=250)
yazi2 = tk.Label(text="File Not Selected")
yazi2.place(x=175, y=275)
goster1 = tk.Button(text="göster", command=noktabirgoster)
btcalistir = tk.Button(text="RUN",command = calistir)
btcalistir.place(x=175, y=450)
btdosyaal = tk.Button(text="Click to select a file",command = dosyasec)
btdosyaal.place(x=175, y=300)
btdosyayaz = tk.Button(text="dosya yaz",command = dosyayaz)
korx=tk.Label(text="COORDİNATE X",
                   font="times 10")
korx.place(x=160,y=400)
kory=tk.Label(text="COORDİNATE Y",
                   font="times 10")
kory.place(x=315,y=400)
korz=tk.Label(text="COORDİNATE Z",
                   font="times 10")
korz.place(x=460,y=400)
listbox = tk.Listbox(form,width=50, height=10)
listbox.place(x=1300,y=160)
scrollbar = Scrollbar(form)
scrollbar.place(x=1605,y=160,height=320)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)




form.mainloop()



