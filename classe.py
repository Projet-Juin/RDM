# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 17:24:39 2020

@author: Clara
"""


class charge_concentrée :
    nbr = 0
    def __init__(self, P, a): # Notre méthode constructeur
        self.P = P
        self.a = a
        charge_concentrée.nbr += 1
        
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
    