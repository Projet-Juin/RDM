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
        nbr += 1  
        
class charge_répartie :
    
    def __init__(self, q): 
        self.q = q
        
class charge_répartie_partielle :
    
    def __init__(self, q, a, l): 
        self.q = q
        self.a = a
        self.l = l
        
        
class charge_triangulaire :
    
    def __init__(self, q, a): # Notre méthode constructeur
        self.q = q
        self.a = a
        
class charge_triangulaire_monotone :
    
    def __init__(self, q): 
        self.q = q
        
class charge_triangulaire_antisymétrique :
    
    def __init__(self, q):
        self.q = q
        
class charge_trapézoïdale_symétrique :
    
    def __init__(self, q, a, l): # Notre méthode constructeur
        self.q = q
        self.a = a
        self.l = l
        
class charge_parabolique :
    
    def __init__(self, q): 
        self.q = q
        
class couple :
    
    def __init__(self, C, a): 
        self.C = C
        self.a = a
        
class couple_réparti :
    
    def __init__(self, C): 
        self.C = C
        
class charge_croissante :
    
    def __init__(self, q): 
        self.q = q

class charge_décroissante :
    
    def __init__(self, q): 
        self.q = q
    