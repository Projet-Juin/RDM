# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:41:18 2020

@author: Simon
"""
import numpy as np
import matplotlib.pyplot as plt

def charge_concentrée(hauteur, longueur, Igz, E, LimElast, P, x, NbrePointsX, a, b):
    
    # Réactions aux appuis (à améliorer quand y aura plus de 2 appuis)
    RA = -(P*b)/longueur
    RB = -(P*a)/longueur
    print(RA, RB)
    
    # Efforts tranchants [N] 
    EffortTranch = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
    for i in range(NbrePointsX):
        if x[i] < a :
            EffortTranch[i] = -RA
        elif x[i] > a :
            EffortTranch[i] = RB
        else :
            EffortTranch[i] = 0
    
    # Moment Fléchissant [N.mm] 
    Mf = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
    for i in range(NbrePointsX):
        if x[i] < a :
            Mf[i] = RA*x[i]
        elif x[i] >= a :
            Mf[i] = RB*(longueur-x[i])
    
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
            flèche[i] = -(P/(E*Igz*longueur))*((b/6)*(x[i]**3)+a*(longueur*a/2-(a**2)/6-(longueur**2)/3)*x[i])
        elif x[i] > a :
            flèche[i] = -P*a/(E*Igz*longueur)*(-(x[i]**3)/6+longueur*(x[i]**2)/2+(-(a**2)/6-(longueur**2)/3)*x[i]+((a**2)*longueur)/6)
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
    
    return RA, RB, EffortTranch, Mf, ContrainteYMax, ContrainteMax, DefYMax, DefMax, flèche, FlècheMax, \
    GrapheEffortTranchCC, GrapheMfCC, GrapheContrainteYMaxCC, GrapheDefYMaxCC, GrapheFlècheCC
    
    
def charge_répartie(hauteur, longueur, Igz, E, LimElast, q, x) :
    
    # Réactions aux appuis
    RA = -(q*longueur)/2
    RB = -(q*longueur)/2
    
    # Efforts tranchants [N]
    EffortTranch = -((-q*longueur/2) + q*x) # EffortTranch est de type <class 'numpy.ndarray'>. 
    # En tant qu'instances de classe, il possède donc des attributs et méthodes
    
    # Moment Fléchissant [N.mm]
    Mf = -q*(longueur-x)*(x/2)
    
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
    flèche = q*x/(24*E*Igz)*((longueur**3)-2*longueur*(x**2)+(x**3))
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
    
    return RA, RB, EffortTranch, Mf, ContrainteYMax, ContrainteMax, DefYMax, DefMax, flèche, FlècheMax, \
    GrapheEffortTranchCR, GrapheMfCR, GrapheContrainteYMaxCR, GrapheDefYMaxCR, GrapheFlècheCR
    

def charge_répartie_partielle(hauteur, longueur, Igz, E, LimElast, q, x, NbrePointsX, a, b, c):
    
    x = np.array(x)
    
    #avec une charge qui ne s'étend pas partout
    # Réactions aux appuis
    RA = -q*b*(b + 2*c)/(2*longueur)
    RB = -q*b*(b + 2*a)/(2*longueur)
    
    # Efforts tranchants [N]
    EffortTranch = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
    for i in range(NbrePointsX):
        if x[i] <= a :
            EffortTranch[i] = -RA
        elif x[i] > a and x[i] <= (a+b):
            EffortTranch[i] = -RA-q*(x[i]-a)
        elif x[i] > (a+b) and x[i] <= longueur :
            EffortTranch[i] = RB
    
    # Moment Fléchissant [N.mm]
    Mf = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
    for i in range(NbrePointsX):
        if x[i] <= a :
            Mf[i] = RA*x[i]
        elif x[i] > a and x[i] <= (a+b):
            Mf[i] = RA*x[i]-q*(((x[i]-a)**2)/2)
        elif x[i] > (a+b) :
            Mf[i] = RB*(longueur-x[i])
    
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
    flèche = -q/(48*E*Igz*longueur)*(b*(b+2*c)*x*(4*(longueur**2-x**2)-(b+2*c)**2-b**2)+2*longueur*(x-a)**4)
    FlècheMax = np.amin(flèche)

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
    
    return RA, RB, EffortTranch, Mf, ContrainteYMax, ContrainteMax, DefYMax, DefMax, flèche, FlècheMax

def charge_répartie_partielle_proche(hauteur, longueur, Igz, E, LimElast, q, x, NbrePointsX, a):
    #avec une charge qui ne s'étend pas partout et proche d'un appui
    # Réactions aux appuis
    RA = q*a*(longueur - (a/2))/longueur
    RB = q*(a**2)/(2*longueur)
    
    # Efforts tranchants [N]
    EffortTranch = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
    for i in range(NbrePointsX):
        if x[i] <= a :
            EffortTranch[i] = -q*(a*(2*longueur-a)-2*longueur*x[i])/(2*longueur)
        elif x[i] > a and x[i] <= longueur :
            EffortTranch[i] = q*(a**2)/(2*longueur)
    
    # Moment Fléchissant [N.mm]
    Mf = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
    for i in range(NbrePointsX):
        if x[i] <= a : 
            Mf[i] = q*x[i]*(a*(2*longueur-a)-longueur*x[i])/(2*longueur)
        elif x[i] > a :
            Mf[i] = q*(a**2)*(longueur-x[i])/(2*longueur)
    
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
            flèche[i] = -q*x[i]*((a**2)*(2*longueur-a)**2-2*a*(2*longueur-a)*(x[i]**2)+longueur*(x[i]**3))/(24*E*Igz*longueur)
        elif x[i] > a :
            flèche[i] = -q*a**2*(longueur-x[i])*(4*longueur*x[i]-2*x[i]**2-a**2)/(2*E*Igz*longueur)
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

def charge_triangulaire(hauteur, longueur, Igz, E, LimElast, q, x, NbrePointsX, a, b):
     #avec une charge répartie sous forme de triangle
    # Réactions aux appuis
    RA = q*(longueur+b)/6 
    RB = q*(longueur+a)/6 
    
    # Efforts tranchants [N]
    EffortTranch = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
    for i in range(NbrePointsX):
        if x[i] <= a :
            EffortTranch[i] = -q*(a*(longueur+b)-3*x[i]**2)/(6*a)
        elif x[i] > a and x[i] <= longueur :
            EffortTranch[i] = -q*(3*x[i]**2-6*longueur*x[i]+2*longueur**2+a**2)/(6*b)
    
    # Moment Fléchissant [N.mm]
    Mf = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
    for i in range(NbrePointsX):
        if x[i] <= a : 
            Mf[i] = q*x[i]*(a*(longueur+b)-3*x[i]**2)/(6*a)
        elif x[i] > a :
            Mf[i] = q*(longueur-x[i])*(2*longueur*x[i]-x[i]**2-a**2)/(6*b)
    
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
            flèche[i] = -q*x[i]*(3*(x[i]**4)+a*(longueur+b)*(7*longueur**2-3*b**2-10*x[i]**2))/(360*E*Igz*a)
        elif x[i] > a :
            flèche[i] = -q*(longueur-x[i])*(3*((longueur-x[i])**4)+b*(longueur+a)*(7*longueur**2-3*a**2-10*(longueur-x[i])**2))/(360*E*Igz*b)
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
    
def charge_triangulaire_monotone(hauteur, longueur, Igz, E, LimElast, q, x, NbrePointsX):
    # comme triangle mais avec a = longueur et b = 0
    # Réactions aux appuis
    RA = q*(longueur)/6 
    RB = q*(longueur)/3 
    
    # Efforts tranchants [N]
    EffortTranch = -q*(longueur**2-3*x**2)/(6*longueur)
    
    # Moment Fléchissant [N.mm]
    Mf = q*x*(longueur**2-x**2)/(6*longueur)
    
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
    flèche = -q*x*(longueur**2-x**2)*(7*longueur**2-3*x**2)/(360*E*Igz*longueur)
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
    
def charge_triangulaire_antisymétrique(hauteur, longueur, Igz, E, LimElast, q, x, NbrePointsX):
    # q s'inverse à la moitié de la poutre
    # Réactions aux appuis
    RA = q*(longueur)/6 
    RB = -q*(longueur)/6 
    
    # Efforts tranchants [N]
    EffortTranch = -q*(6*x**2-6*longueur*x+longueur**2)/(6*longueur)
    
    # Moment Fléchissant [N.mm]
    Mf = q*x*(longueur-x)*(longueur-2*x)/(6*longueur)
    
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
    flèche = q*x*(6*(x**4)-15*longueur*(x**3)+10*longueur**2*x**2-(longueur**4))/(360*E*Igz*longueur)
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
    
def charge_trapézoïdale_symétrique(hauteur, longueur, Igz, E, LimElast, q, x, NbrePointsX, a, b):
    # q forme un trapèze
    # Réactions aux appuis
    RA = q*(longueur-a)/2
    RB = RA
    
    # Efforts tranchants [N]
    EffortTranch = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
    for i in range(NbrePointsX):
        if x[i] <= a :
            EffortTranch[i] = -q*(a*longueur-a**2-x[i]**2)/(2*a) 
        elif x[i] > a and x[i] <= (a+b):
            EffortTranch[i] = -q*(longueur-2*x[i])/2
        elif x[i] > (a+b) and x[i] <= longueur :
            EffortTranch[i] =  -q*((longueur-x[i])**2-a*(longueur-a))/(2*a)
    
    # Moment Fléchissant [N.mm]
    Mf = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
    for i in range(NbrePointsX):
        if x[i] <= a :
            Mf[i] = q*x[i]*(3*a*longueur-3*a**2-x[i]**2)/(6*a)
        elif x[i] > a and x[i] <= (a+b):
            Mf[i] = q*(3*longueur*x[i]-3*x**2-a**2)/6 
        elif x[i] > (a+b) :
            Mf[i] = q*(longueur-x[i])*(3*a*(longueur-a)-(longueur-x[i])**2)/(6*a)
    
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
    flèche = 0#pas de flèche encore
    FlècheMax = np.amin(flèche)

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
    
def charge_parabolique(hauteur, longueur, Igz, E, LimElast, q, x, NbrePointsX):
    # q forme une parabole
    # Réactions aux appuis
    RA = q*longueur/3 
    RB = RA 
    
    # Efforts tranchants [N]
    EffortTranch = -q*(4*(x**3)-(6*longueur*x**2)+(longueur**3))/(3*longueur**2)
    
    # Moment Fléchissant [N.mm]
    Mf = q*x*((x**3)-2*longueur*x**2+(longueur**3))/(3*longueur**2)
    
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
    flèche = q*x*((x**5)*-3*longueur*(x**4)+5*(longueur**3)*x**2-3*(longueur**5))/(90*E*Igz*longueur**2)
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