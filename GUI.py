# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 19:46:18 2022

@author: Lenovo
"""

from tkinter import *
import Funktion
import InitialisierungNewtonVerfahren

window=Tk()
window.geometry("375x300")
window.title("Newton-Verfahren")
#grid=grid(window)


def SubmitGrad():
    global Grad
    global KoeffEntryList
    KoeffEntryList=[]
    try:
        Grad=int(GradEntry.get())
    except ValueError:
        messagebox.showerror(title="Value Error",message="Sie müssen eine natürliche Zahl eingeben (z.B: 5)")
        return
    
    for i in range (Grad+1):
        KoeffLabel=Label(window, text="Koeffizient a"+str(i)).grid(row=4,column=i)
        
        KoeffEntry=Entry(window)
        KoeffEntry.grid(row=5,column=i)
        KoeffEntryList.append(KoeffEntry)
        
        KoeffButton=Button(window,text="Koeffizienten bestätigen",command=SubmitKoeff)
        KoeffButton.grid(row=6,column=0,columnspan=3)
        
    if (Grad>=2):
        window.geometry(f"{(Grad+1)*125}x300")  
    elif(Grad==1 or Grad==0):
        window.geometry("375x300")
        
    
def SubmitKoeff():
    cleanlabel=Label(window)
    cleanlabel.grid(row=8)
    global Koeff
    Koeff=[]
    global Nullstellen
    Nullstellen=[]
    global lenNullstellenAlt
    for i in range (Grad+1):
        Hilfe=KoeffEntryList[i]
        try:
           Koeff.append(float(Hilfe.get()))#grid(row=5,column=i).get()))
        except ValueError:
            messagebox.showerror(title="Value Error",message="Sie müssen eine Gleitkommazahl eingeben (z.B: 3.75)")  
            return
    BearbeiteteFunktion=Funktion.Funktion(Grad,Koeff)
    #print(BearbeiteteFunktion.printMe())
    Nullstellen=InitialisierungNewtonVerfahren.InitialisierungNewtonVerfahren(BearbeiteteFunktion)    
    ErgebnisLabel=Label(window, text="Alle gefundenen Nullstellen:").grid(row=8,column=0,columnspan=4)
    try:
        for i in range (lenNullstellenAlt):
            KoeffLabel=Label(window, text="                                       ").grid(row=9,column=i,columnspan=1)   
    except:
        pass
    if (len(Nullstellen)!=0):
        for i in range (len(Nullstellen)):
            KoeffLabel=Label(window, text=Nullstellen[i]).grid(row=9,column=i)
        lenNullstellenAlt=len(Nullstellen)
    else:
       KoeffLabel=Label(window, text="Es wurde keine Nullstelle gefunden").grid(row=9,column=0, columnspan=3) 
       lenNullstellenAlt=3
       
       
       
GradLabel=Label(window, text="Geben Sie den Grad des Polynoms als natürliche Zahl ein:").grid(row=0,column=0,columnspan=3)
GradEntry=Entry(window)
GradEntry.grid(row=1,column=0,columnspan=3)
GradButton=Button(window,text="Grad bestätigen",command=SubmitGrad)
GradButton.grid(row=2,column=0,columnspan=3)
window.resizable(False, False)
window.mainloop()