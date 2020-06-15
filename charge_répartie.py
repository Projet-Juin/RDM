# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 21:05:36 2020

@author: Simon
"""

import numpy as np
import matplotlib.pyplot as plt

def charge_répartie(hauteur, longueur, Igz, E, LimElast, q, x) :
    
    # Réactions aux appuis (à améliorer quand y aura plus de 2 appuis)
    RA = -(q*longueur)/2
    RB = -(q*longueur)/2
    
    # Efforts tranchants [N]
    EffortTranch = q*longueur/2 - q*x # EffortTranch est de type <class 'numpy.ndarray'>. 
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
