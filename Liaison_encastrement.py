# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:38:05 2020

@author: Simon
"""
import numpy as np
import matplotlib.pyplot as plt

# poutre encastrée gauche et libre à droite

def charge_concentrée(hauteur, longueur, Igz, E, LimElast, P, x, NbrePointsX, a, b):
   
     # Réactions aux liaisons
    RA = P
    
    # Efforts tranchants [N] 
    EffortTranch = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
    for i in range(NbrePointsX):
        if x[i] < a :
            EffortTranch[i] = -RA
        elif x[i] >= a :
            EffortTranch[i] = 0 # car -RA+ P = RB= 0
    
    # Moment Fléchissant [N.mm] 
    Mf = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
    for i in range(NbrePointsX):
        if x[i] < a :
            Mf[i] = -EffortTranch[i]*(x[i]+a)
        elif x[i] >= a :
            Mf[i] = 0
            
    # Contrainte pour y = h/2 [MPa]
    ContrainteYMax = -(Mf/Igz)*(hauteur/2)
    ContrainteMax = np.amax(ContrainteYMax)
    print('ContrainteMax', ContrainteMax)
    
    # Contrainte pour tout y [MPa]
    #Contrainte = np.matmul(-(Mf/Igz),y)
    
    # Déformation pour y = h/2 [SD]
    DefYMax = ContrainteYMax/E
    DefMax = np.amax(DefYMax)
    print('DefMax', DefMax)
    
    # Flèche de la poutre
    flèche = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
    for i in range(NbrePointsX):
        if x[i] <= a :
            flèche[i] = -(RA/(E*Igz))*((x[i]**3)/6+a*(x[i]**2)/2)
        elif x[i] > a :
            flèche[i] = -(RA/(E*Igz))*((3/2)*(a**2)*x[i]-(5/6)*(a**3))
    FlècheMax = np.amin(flèche)
    print('flèche max : ',FlècheMax)
    
    plt.figure(1) #Graphe effort tranchant
    plt.xlabel("x [mm]") 
    plt.ylabel("T [N]") 
    plt.title("Effort Tranchant le long de la poutre") #Titre de la courbe
    GrapheEffortTranchCC = plt.plot(x,EffortTranch) #Le tracé en lui-même
    plt.show()
    
    plt.figure(2) #Graphe moment fléchissant
    plt.xlabel("x [mm]") 
    plt.ylabel("Mf [N.mm]") 
    plt.title("Tracé du Moment Fléchissant") 
    GrapheMfCC = plt.plot(x,Mf)
    plt.show()
    
    plt.figure(3) #Graphe de la contrainte en y = h/2
    plt.xlabel("x [mm]") 
    plt.ylabel("Contrainte Max [MPa]") 
    plt.title("Tracé de la Contrainte Maximale") 
    GrapheContrainteYMaxCC = plt.plot(x,ContrainteYMax) 
    plt.show()
    
    plt.figure(4) #Graphe de la déformation en y = h/2
    plt.xlabel("x [mm]") 
    plt.ylabel("Déformation Max [SD]") 
    plt.title("Tracé de la Déformation Maximale") 
    GrapheDefYMaxCC = plt.plot(x,DefYMax) 
    plt.show()
    
    plt.figure(5) #Graphe de la flèche
    plt.xlabel("x [mm]") 
    plt.ylabel("flèche [mm]") 
    plt.title("Tracé de la flèche") 
    GrapheFlècheCC = plt.plot(x,flèche,label="flèche")
    plt.show()
    
    return RA, EffortTranch, Mf, ContrainteYMax, ContrainteMax, DefYMax, DefMax, flèche, FlècheMax


def charge_répartie(hauteur, longueur, Igz, E, LimElast, q, x):
    
    # Réactions aux appuis (à améliorer quand y aura plus de 2 appuis)
    RA = -q*longueur
    
    # Efforts tranchants [N]
    EffortTranch = -(RA + q*x) # EffortTranch est de type <class 'numpy.ndarray'>. 
    
    # Moment Fléchissant [N.mm]
    Mf = RA*x+(q/2)*(x**2)+q*((longueur**2)/2)
    
    # Contrainte pour y = h/2 [MPa]
    ContrainteYMax = -(Mf/Igz)*(hauteur/2)
    ContrainteMax = np.amax(ContrainteYMax)
    print('contrainte max = ', ContrainteMax)
    
    # Contrainte pour tout y [MPa]
    #Contrainte = np.matmul(-(Mf/Igz),y)
    
    # Déformation pour y = h/2 [SD]
    DefYMax = ContrainteYMax/E
    DefMax = np.amax(DefYMax)
    print('DefMax', DefMax)
    
    # Flèche de la poutre
    flèche = -(q/(24*E*Igz))*(-((x**4)/12)+(longueur*(x**3)/3)+((longueur**2)*(x**2)/2))
    FlècheMax = np.amin(flèche)
    print('flèche max : ',FlècheMax)
    
    plt.figure(1) #Graphe effort tranchant
    plt.xlabel("x [mm]") 
    plt.ylabel("T [N]") 
    plt.title("Effort Tranchant le long de la poutre") #Titre de la courbe
    GrapheEffortTranchCR = plt.plot(x,EffortTranch) #Le tracé en lui-même
    plt.show()
    
    plt.figure(2) #Graphe moment fléchissant
    plt.xlabel("x [mm]") 
    plt.ylabel("Mf [N.mm]") 
    plt.title("Tracé du Moment Fléchissant") 
    GrapheMfCR = plt.plot(x,Mf)
    plt.show()
    
    plt.figure(3) #Graphe de la contrainte en y = h/2
    plt.xlabel("x [mm]") 
    plt.ylabel("Contrainte Max [MPa]") 
    plt.title("Tracé de la Contrainte Maximale") 
    GrapheContrainteYMaxCR = plt.plot(x,ContrainteYMax) 
    plt.show()
    
    plt.figure(4) #Graphe de la déformation en y = h/2
    plt.xlabel("x [mm]") 
    plt.ylabel("Déformation Max [SD]") 
    plt.title("Tracé de la Déformation Maximale") 
    GrapheDefYMaxCR = plt.plot(x,DefYMax) 
    plt.show()
    
    plt.figure(5) #Graphe de la flèche
    plt.xlabel("x [mm]") 
    plt.ylabel("flèche [mm]") 
    plt.title("Tracé de la flèche") 
    GrapheFlècheCR = plt.plot(x,flèche,label="flèche")
    plt.show()
    
    return RA, EffortTranch, Mf, ContrainteYMax, ContrainteMax, DefYMax, DefMax, flèche, FlècheMax