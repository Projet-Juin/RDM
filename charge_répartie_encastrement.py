# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 19:32:15 2020

@author: Simon
"""
import numpy as np
import matplotlib.pyplot as plt

# poutre encastrée gauche et libre à droite

def charge_répartie_encastrement(hauteur, longueur, Igz, E, LimElast, q, x):
    
    # Réactions aux appuis (à améliorer quand y aura plus de 2 appuis)
    RA = q*longueur
    
    # Efforts tranchants [N]
    EffortTranch = -RA + q*x # EffortTranch est de type <class 'numpy.ndarray'>. 
    
    # Moment Fléchissant [N.mm]
    Mf = RA*x-(q/2)*((x**2)-(longueur**2))
    
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
    
    return RA, EffortTranch, Mf, ContrainteYMax, ContrainteMax, DefYMax, DefMax, flèche, FlècheMax