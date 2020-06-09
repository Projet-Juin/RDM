# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 21:05:36 2020

@author: Simon
"""

import numpy as np
import matplotlib.pyplot as plt

def charge_répartie(hauteur, longueur, largeur, matériau, E, MasseVol, LimElast, q, x) :
    
    # Réactions aux appuis (à améliorer quand y aura plus de 2 appuis)
    RA = (q*longueur)/2
    RB = (q*longueur)/2
    
    # Moment d'inertie (à améliorer quand la géométrie changera) [mm^4]
    Igz = (largeur *(pow(hauteur,3)))/12
    
    # Masse de la poutre
    Masse = largeur*longueur*hauteur*MasseVol*(10^(-6))
    
    # Efforts tranchants [N]
    EffortTranch = (-q*longueur/2) + q*x # EffortTranch est de type <class 'numpy.ndarray'>. 
    # En tant qu'instances de classe, il possède donc des attributs et méthodes
    
    # Moment Fléchissant [N.mm]
    Mf = q*(longueur-x)*(x/2)
    
    # Contrainte pour y = h/2 [MPa]
    ContrainteYMax = (Mf/Igz)*(hauteur/2)
    
    # Déformation pour y = h/2 [SD]
    DeformationYMax = ContrainteYMax/E
    
    # Flèche de la poutre
    flèche = -(q/(24*E*Igz))*(2*longueur*pow(x,3)-pow(x,4)-pow(longueur,3)*x)
    FlècheMax = max(x)
    
    plt.figure(1) #Ma première figure
    plt.xlabel("x") 
    plt.ylabel("flèche") 
    plt.title("Tracé de la flèche") #Titre de la courbe
    plt.plot(x,flèche,label="flèche") #Le tracé en lui-même
    plt.legend('salut') 
    plt.show()