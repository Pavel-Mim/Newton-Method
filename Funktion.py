# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 01:46:18 2022

@author: Lenovo
"""


class Funktion:
    Grad=0
    Koeffizienten=[]
    
    def __init__(self,übergebenerGrad, übergebeneKoeffizienten):
        self.Grad=übergebenerGrad   
        self.Koeffizienten=übergebeneKoeffizienten
        
    def Ableitung (self):
        help=[]
        for i in range (len(self.Koeffizienten)-1):
            help.append(self.Koeffizienten[i+1]*(i+1))
        Rückgabefunktion=Funktion(self.Grad-1,help)
        return(Rückgabefunktion)

    
    def Wert(self,x):
        Ausgabe=0
        for i in range (len(self.Koeffizienten)):
            Ausgabe=Ausgabe+(self.Koeffizienten[i]*x**i)
        return Ausgabe

    def printMe(self):
        Ausgabe=""
        for i in range (len(self.Koeffizienten)):
            if (self.Koeffizienten[i]!=0):
                Ausgabe=Ausgabe+ str(self.Koeffizienten[i])
                Ausgabe=Ausgabe+"x^"+str(i)+"+"
        Ausgabe=Ausgabe[:-1]
        return Ausgabe  
        