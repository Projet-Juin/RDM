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
    RA = -P
    
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
            Mf[i] = -EffortTranch[i]*(x[i]-a)
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
            flèche[i] = -RA*(x[i]**2)/(6*E*Igz)*(3*a-x[i])  #-(RA/(E*Igz))*((x[i]**3)/6+a*(x[i]**2)/2)
        elif x[i] > a :
            flèche[i] = -RA*(a**2)/(6*E*Igz)*(3*x[i]-a) #-(RA/(E*Igz))*((3/2)*(a**2)*x[i]-(5/6)*(a**3))
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
    RA = q*longueur
    
    # Efforts tranchants [N]
    EffortTranch = RA-q*x  # EffortTranch est de type <class 'numpy.ndarray'>. 
    
    # Moment Fléchissant [N.mm]
    Mf = (q/2)*(x-longueur)**2
    
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
    flèche = q*(((longueur-x)**4)+4*(longueur**3)*x-(longueur**4))/(24*E*Igz)
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

def charge_répartie_partielle(hauteur, longueur, Igz, E, LimElast, q, x, NbrePointsX, a, b, c):
    
    #avec une charge qui ne s'étend pas partout
    # Réactions aux appuis
    RA = -q*b
    
    # Efforts tranchants [N]
    EffortTranch = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
    for i in range(NbrePointsX):
        if x[i] <= a :
            EffortTranch[i] = -RA
        elif x[i] > a and x[i] <= (a+b):
            EffortTranch[i] = -RA-q*(x[i]-a)
        elif x[i] > (a+b) and x[i] <= longueur :
            EffortTranch[i] = 0
    
    # Moment Fléchissant [N.mm]
    Mf = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
    for i in range(NbrePointsX):
        if x[i] <= a :
            Mf[i] = RA*(x[i]-a-b/2)
        elif x[i] > a and x[i] <= (a+b):
            Mf[i] = RA*(x[i]-a-b/2)+q*((x[i]**2)/2-a*x[i]+(a**2)/2)
        elif x[i] > (a+b) :
            Mf[i] = 0
    
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
    flèche = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
    for i in range(NbrePointsX):
        if x[i] <= a :
            flèche[i] = RA/(E*Igz)*((x[i]**3)/6-(a+b/2)*(x[i]**2)/2)
        elif x[i] > a and x[i] <= (a+b):
            flèche[i] = RA/(E*Igz)*((x[i]**3)/6-(a+b/2)*(x[i]**2)/2)+q/(E*Igz)*((x[i]**4)/24-a*(x[i]**3)/6+(a**2)*(x[i]**2)/4-(a**3)*x[i]/6+(a**4)/24)
        elif x[i] > (a+b) :
            #K5 = RA*(((a+b)**2)/2-(a+b/2)*(a+b))+q*(((a+b)**3)/6-a*((a+b)**2)/2+(a**2)*(a+b)/2-(a**3)/3)
            #K6 = RA/(E*Igz)*(((a+b)**3)/6-(a+b/2)*((a+b)**2)/2)+q/(E*Igz)*(((a+b)**4)/24-a*((a+b)**3)/6+(a**2)*((a+b)**2)/4-(a**3)*(a+b)/6+(a**4)/24)-K5*(a+b)/(E*Igz)

            K5 = RA/(E*Igz)*(((a+b)**2)/2-(a+b/2)*(a+b))+q/(E*Igz)*(((a+b)**3)/6-a*((a+b)**2)/2+(a**2)*(a+b)/2-(a**3)/6)
            K6 = RA/(E*Igz)*(((a+b)**3)/6-(a+b/2)*((a+b)**2)/2)+q/(E*Igz)*(((a+b)**4)/24-a*((a+b)**3)/6+(a**2)*((a+b)**2)/4-(a**3)*(a+b)/6+(a**4)/24)-K5*(a+b)
            flèche[i] = K5*x[i]+K6
    FlècheMax = np.amin(flèche)
    print(flèche)

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

def charge_croissante(hauteur, longueur, Igz, E, LimElast, q, x):
    
    # Réactions aux appuis 
    RA = -q*longueur/2
    
    # Efforts tranchants [N]
    EffortTranch = RA*((x**2)/(longueur**2)-1)  # EffortTranch est de type <class 'numpy.ndarray'>. 
    
    # Moment Fléchissant [N.mm]
    Mf = q*((longueur-x)**2)*(2*longueur+x)/(6*longueur)
    
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
    flèche = q*(x**2)*(20*(longueur**3)-10*longueur**2*x+(x**3))/(120*E*Igz*longueur)
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
    
def charge_décroissante(hauteur, longueur, Igz, E, LimElast, q, x):
    
    # Réactions aux appuis 
    RA = -q*longueur/2
    
    # Efforts tranchants [N]
    EffortTranch = q*((longueur-x)**2)/(2*longueur)
    
    # Moment Fléchissant [N.mm]
    Mf = q*((longueur-x)**3)/(6*longueur)
    
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
    flèche = q*(4*(longueur**5)-5*(longueur**4)*(longueur-x)+((longueur-x)**5))/(120*E*Igz*longueur)
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
    
    #