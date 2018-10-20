import tkinter as tk
import tkinter as ttk
import numpy as np
import math
from tkinter import messagebox as msg 

#create GUI
win = tk.Tk()
win.title("SIMULASI BUFFON-NEDDLE")

ttk.Label(win, text="SIMULASI BUFFON-NEDDLE").grid(column=1, row=0)

def _msgBox():
    """Menghitung peluang jarum terkena garis"""
    n1=0
    nt=0
    dr1 = int(d1.get())
    dr2 = int(d2.get())
    dr3 = int(d3.get())
    dr4 = int(d4.get())
    dr5 = int(d5.get())
    total_d= dr1+dr2+dr3+dr4+dr5

    while nt<=int(N.get()):
        r1=np.random.uniform()
        r2=np.random.uniform()
        tetha=r2*math.pi
        
        if r1 <= dr1/total_d:
            a=0.5*r1*dr1
        elif r1>dr1/total_d and r1<=dr2/total_d:
            a=0.5*r1*(dr1+dr2)    
        elif r1>dr2/total_d and r1<=dr3/total_d:
            a=0.5*r1*(dr1+dr2+dr3)
        elif r1>dr3/total_d and r1<=dr4/total_d:
            a=0.5*r1*(dr1+dr2+dr3+dr4)
        elif r1>dr4/total_d and r1<=dr5/total_d:
            a=0.5*r1*(dr1+dr2+dr3+dr4+dr5)

        if a<= int(l.get())*0.5*math.sin(tetha):
            n1 +=1
        nt +=1
    p=n1/int(N.get())
    msg.showinfo('Peluangnya adalah',str(p))
            
ttk.Label(win, text="Masukkan jarak garis 1 dan 2 : ").grid(column=0, row=1)
d1=tk.StringVar()
d1_entered= ttk.Entry(win, width=12, textvariable=d1)
d1_entered.grid(column=2, row=1)

ttk.Label(win, text="Masukkan jarak garis 2 dan 3 : ").grid(column=0, row=2)
d2=tk.StringVar()
d2_entered= ttk.Entry(win, width=12, textvariable=d2)
d2_entered.grid(column=2, row=2)

ttk.Label(win, text="Masukkan jarak garis 3 dan 4 : ").grid(column=0, row=3)
d3=tk.StringVar()
d3_entered= ttk.Entry(win, width=12, textvariable=d3)
d3_entered.grid(column=2, row=3)

ttk.Label(win, text="Masukkan jarak garis 4 dan 5 : ").grid(column=0, row=4)
d4=tk.StringVar()
d4_entered= ttk.Entry(win, width=12, textvariable=d4)
d4_entered.grid(column=2, row=4)

ttk.Label(win, text="Masukkan jarak garis 5 dan 6 : ").grid(column=0, row=5)
d5=tk.StringVar()
d5_entered= ttk.Entry(win, width=12, textvariable=d5)
d5_entered.grid(column=2, row=5)

ttk.Label(win, text="Masukkan panjang jarum : ").grid(column=0, row=6)
l=tk.StringVar()
l_entered= ttk.Entry(win, width=12, textvariable=l)
l_entered.grid(column=2, row=6)

ttk.Label(win, text="Masukkan banyak jarum : ").grid(column=0, row=7)
N=tk.StringVar()
N_entered= ttk.Entry(win, width=12, textvariable=N)
N_entered.grid(column=2, row=7)

actio=ttk.Button(win, text="Proses", command = _msgBox)
actio.grid(column=2, row=8)

d1_entered.focus()
d2_entered.focus()
d3_entered.focus()
d4_entered.focus()
d5_entered.focus()
l_entered.focus()
N_entered.focus()
#start GUI
win.mainloop()
