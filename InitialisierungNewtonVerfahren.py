# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 17:05:44 2022

@author: Lenovo
"""
import Funktion
import NewtonVerfahren

def InitialisierungNewtonVerfahren(f):
    
    NSTList=[]
    AnzahlNST=f.Grad
    Genauigkeit=GenauigkeitBerechnen(f)
    
    SchrittweiteStart=10
    Min=StartwertFindung(f,-SchrittweiteStart)
    Max=StartwertFindung(f,SchrittweiteStart)
    #Gerade=Bisektion2(f)#, Min, Max)
    
    NSTDoppelt=False      #testet ob es eine NST gibt, die doppelt, 4fach etc ist
    fAbleitung=f.Ableitung()
    Rundung=int(14/f.Grad) #Rundung für den Fall, dass das Verfahren gegen eine rationale Zahl konvergiert
    
    # if (f.Koeffizienten[0]==0):
    #     NSTList.append(0.0)

    while (len(NSTList)<AnzahlNST):# or ((bool(len(NSTList)%2))==bool((f.Grad)%2))==(NSTDoppelt)):
        #Startwert=StartwertFindung(f,10)
        print(NSTList)
        etta=NewtonVerfahren.NewtonVerfahrenPolynom(f,Max, NSTList)
        if (f.Wert(round(etta,Rundung))==0):
            etta=round(etta,Rundung)
        if (abs(f.Wert(etta))<(Genauigkeit) and Bisektion(f,etta-Genauigkeit,etta+Genauigkeit)):#and etta not in NSTList):
            NSTList.append(etta)
            if (fAbleitung.Wert(etta)==0 ):#or fAbleitung.Wert(round(etta,Rundung))==0):
                NSTDoppelt=not(NSTDoppelt)
                
        else:
            etta2=NewtonVerfahren.NewtonVerfahrenPolynom(f, Min, NSTList)
            if (f.Wert(round(etta2,Rundung))==0 ):
                etta2=round(etta2,Rundung)
            if(abs(f.Wert(etta2))<Genauigkeit and Bisektion(f,etta-Genauigkeit,etta+Genauigkeit)):# and etta2 not in NSTList):
                    NSTList.append(etta2)
                    if (fAbleitung.Wert(etta2)==0):# or fAbleitung.Wert(round(etta2,Rundung))==0):
                        NSTDoppelt=not(NSTDoppelt)
                        
            else:
                
                AnzahlNST+=-1
    for i in range(len(NSTList)):
        print(f.Wert(NSTList[i]))
    return NSTList     



def StartwertFindung(f,steps):

    Hilfskoeffizienten1=[]
    for i in range (f.Grad-1):
        Hilfskoeffizienten1.append(0)
    Hilfskoeffizienten1.append(f.Koeffizienten[-1])
    HilfsFunktion1=Funktion.Funktion(f.Grad,Hilfskoeffizienten1)
    
    Hilfskoeffizienten2=[]
    for i in range (f.Grad-1):
        Hilfskoeffizienten2.append(abs(f.Koeffizienten[i]))
    HilfsFunktion2=Funktion.Funktion(f.Grad,Hilfskoeffizienten2)
    
    i=1
    while (abs(HilfsFunktion1.Wert(steps*abs(steps)**(i-1)))<abs(HilfsFunktion2.Wert(steps*abs(steps)**(i-1)))):
        i+=1
    print(steps*abs(steps)**(i-1))
    return (steps*abs(steps)**(i-1))



def Bisektion (f,x1,x2): #Keine echte Bisektion 
    if (f.Wert(x1)*f.Wert(x2)<0):
        return True          #TRUE steht für eine ungerade Anzahl Nullstellen (mindestens eine)
    else:
        return False         #FALSE steht für eine gerade Anzahl bzw keine Nullstellen


def GenauigkeitBerechnen(f):

    groessterKoeff=0
    for i in range (len(f.Koeffizienten)):
        if (abs(f.Koeffizienten[i])>groessterKoeff):
            groessterKoeff=abs(f.Koeffizienten[i])
    if (groessterKoeff>10**14 ):
        return (0.1)
    elif(groessterKoeff>1):
        return (groessterKoeff*(10**(-12)))
    else:
        return (10**(-13))
      #return (10**(-15))         
    
def Bisektion2(f):
    # if((f.Grad)%2):
    #     return False
    # else:
    #     return True        
    return (not((f.Grad)%2))   
        
# Koeff=[-3,1]
# f=Funktion.Funktion(2,Koeff)
# test=Bisektion(f,1,2)
# print(test)