import matplotlib.pyplot as plt
from calc import *
from file_reader import *
from pie import * 
from tkinter import *   #library for an easy GUI
from tkinter import ttk #add on of the previous Lib

window = Tk()
window.geometry("400x400")
window.title("Comparaison Types Conso. Energie 2022") #name our program window

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1)

def Clickannee():
    pie(CalcFossile(0),CalcVerte(0),"Annuelle 2022")
def Clickmois1():
    pie(CalcFossile(1),CalcVerte(1),"Janvier 2022")
def Clickmois2():
    pie(CalcFossile(2),CalcVerte(2),"Fevrier 2022")
def Clickmois3():
    pie(CalcFossile(3),CalcVerte(3),"Mars 2022")
def Clickmois4():
    pie(CalcFossile(4),CalcVerte(4),"Avril 2022")
def Clickmois5():
    pie(CalcFossile(5),CalcVerte(5),"Mai 2022")
def Clickmois6():
    pie(CalcFossile(6),CalcVerte(6),"Juin 2022")
def Clickmois7():
    pie(CalcFossile(7),CalcVerte(7),"Juillet 2022")
def Clickmois8():
    pie(CalcFossile(8),CalcVerte(8),"Août 2022")
def Clickmois9():
    pie(CalcFossile(9),CalcVerte(9),"Septembre 2022")
def Clickmois10():
    pie(CalcFossile(10),CalcVerte(10),"Octobre 2022")
def Clickmois11():
    pie(CalcFossile(11),CalcVerte(11),"Novembre 2022")
def Clickmois12():
    pie(CalcFossile(12),CalcVerte(12),"Decembre 2022")

btn1 = Button(tab1,text="Comparaison à l'année", command=Clickannee)
btn1.place(x=120,y=10)
btn2 = Button(tab1,text="Comparaison Janvier", command=Clickmois1)
btn2.place(x=10,y=60)
btn2 = Button(tab1,text="Comparaison Fevrier", command=Clickmois2)
btn2.place(x=10,y=100)
btn2 = Button(tab1,text="Comparaison Mars", command=Clickmois3)
btn2.place(x=10,y=140)
btn2 = Button(tab1,text="Comparaison Avril", command=Clickmois4)
btn2.place(x=10,y=180)
btn2 = Button(tab1,text="Comparaison Mai", command=Clickmois5)
btn2.place(x=10,y=220)
btn2 = Button(tab1,text="Comparaison Juin", command=Clickmois6)
btn2.place(x=10,y=260)
btn2 = Button(tab1,text="Comparaison Juillet", command=Clickmois7)
btn2.place(x=250,y=60)
btn2 = Button(tab1,text="Comparaison Aout", command=Clickmois8)
btn2.place(x=250,y=100)
btn2 = Button(tab1,text="Comparaison Septembre", command=Clickmois9)
btn2.place(x=250,y=140)
btn2 = Button(tab1,text="Comparaison Octobre", command=Clickmois10)
btn2.place(x=250,y=180)
btn2 = Button(tab1,text="Comparaison Novembre", command=Clickmois11)
btn2.place(x=250,y=220)
btn2 = Button(tab1,text="Comparaison Decembre", command=Clickmois12)
btn2.place(x=250,y=260)

tab_control.pack(expand=1, fill='both')

window.mainloop()