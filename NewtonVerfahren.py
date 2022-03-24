# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 11:37:04 2022

@author: Lenovo
"""
import Funktion

def NewtonVerfahren(f, x0):
    x=x0
    i=0
    xvorher=x
    xvorvorher=xvorher
    fAbleitung=f.Ableitung()
    while not ((f.Wert(x)==0 or 
                abs(f.Wert(x))<(10**(-15))) or 
               (i>20 and ((abs(f.Wert(xvorher))<abs(f.Wert(x)) ) or
                        abs(x-xvorher)>abs(xvorher-xvorvorher) or 
                        x==xvorher or x==xvorvorher)) or
               i>50
               ):
        
        xvorvorher=xvorher
        xvorher=x
        try: x=x-f.Wert(x)/fAbleitung.Wert(x)
        except  ZeroDivisionError:
            return x
        i+=1
    return x


def NewtonVerfahrenPolynom(f, x0, NSTListe):
    
    x=x0
    i=0
    xvorher=x
    xvorvorher=xvorher
    fAbleitung=f.Ableitung()
    
    while not ((f.Wert(x)==0 or 
                abs(f.Wert(x))<(10**(-15))) or 
               (i>20 and ((abs(f.Wert(xvorher))<abs(f.Wert(x)) ) or
                        abs(x-xvorher)>abs(xvorher-xvorvorher) or 
                        x==xvorher or x==xvorvorher)) or
               i>50
               ):
        
        xvorvorher=xvorher
        xvorher=x
        Divisionsabzug=0
        for j in range (len(NSTListe)):
           Divisionsabzug=Divisionsabzug+ (f.Wert(x)/(x-NSTListe[j]))
           
        try: x=x-f.Wert(x)/(fAbleitung.Wert(x)-Divisionsabzug)
        except  ZeroDivisionError:
            return x
        i+=1
    return x









# Koeff=[-2,0,1]
# test=Funktion.Funktion(1,Koeff)
# test2=test.Ableitung()
#print(test.Wert(1.4142135623730951))
#print(test2.printMe())
# Gefundeneliste=[1.4142135623730951]
# print(NewtonVerfahrenPolynom(test, 100,Gefundeneliste))
