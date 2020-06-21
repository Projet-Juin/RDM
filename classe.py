# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 17:24:39 2020

@author: Clara
"""
import numpy as np
import matplotlib.pyplot as plt

class charge_concentrée :
    nbr = 0
    def __init__(self, P, a): # Notre méthode constructeur
        self.P = P
        self.a = a
        charge_concentrée.nbr += 1
    
    def charge_concentrée(self, hauteur, longueur, Igz, E, x, NbrePointsX):
        a = self.a
        b = longueur - self.b
        P = self.P
        # Réactions aux appuis
        RA = -(P*b)/longueur
        RB = -(P*a)/longueur
        
        # Efforts tranchants [N] 
        EffortTranch = np.linspace(0, 0, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] < a :
                EffortTranch[i] = -RA
            elif x[i] > a :
                EffortTranch[i] = RB
            else :
                EffortTranch[i] = 0
        
        # Moment Fléchissant [N.mm] 
        Mf = np.linspace(0, 0, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] < a :
                Mf[i] = RA*x[i]
            elif x[i] >= a :
                Mf[i] = RB*(longueur-x[i])
        
        # Contrainte pour y = h/2 [MPa]
        ContrainteYMax = -(Mf/Igz)*(hauteur/2)
        ContrainteMax = np.amax(abs(ContrainteYMax))
        print('ContrainteMax', ContrainteMax)
        
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        DefMax = np.amax(abs(DefYMax))
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
        
class charge_répartie :
    nbr = 0
    def __init__(self, q): 
        self.q = q
        charge_répartie.nbr += 1
        
class charge_répartie_partielle :
    nbr = 0
    def __init__(self, q, a, l): 
        self.q = q
        self.a = a
        self.l = l
        charge_répartie_partielle.nbr += 1
        
class charge_triangulaire :
    nbr = 0
    def __init__(self, q, a): # Notre méthode constructeur
        self.q = q
        self.a = a
        charge_triangulaire.nbr += 1
        
class charge_triangulaire_monotone :
    nbr = 0
    def __init__(self, q): 
        self.q = q
        charge_triangulaire_monotone.nbr += 1
        
class charge_triangulaire_antisymétrique :
    nbr = 0
    def __init__(self, q):
        self.q = q
        charge_triangulaire_antisymétrique.nbr += 1
        
class charge_trapézoïdale_symétrique :
    nbr = 0
    def __init__(self, q, a, l): # Notre méthode constructeur
        self.q = q
        self.a = a
        self.l = l
        charge_trapézoïdale_symétrique.nbr += 1
        
class charge_parabolique :
    nbr = 0
    def __init__(self, q): 
        self.q = q
        charge_parabolique.nbr += 1
        
class couple :
    nbr = 0
    def __init__(self, C, a): 
        self.C = C
        self.a = a
        couple.nbr += 1
        
class couple_réparti :
    nbr = 0
    def __init__(self, C): 
        self.C = C
        couple_réparti.nbr += 1
        
class charge_croissante :
    nbr = 0
    def __init__(self, q): 
        self.q = q
        charge_croissante.nbr += 1

class charge_décroissante :
    nbr = 0
    def __init__(self, q): 
        self.q = q
        charge_décroissante.nbr += 1
    