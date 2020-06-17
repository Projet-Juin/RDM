# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 17:24:39 2020

@author: Clara
"""


class charge_concentrée :
    
    def __init__(self, P, a, b): # Notre méthode constructeur
        self.P = P
        self.a = a
        self.b = b
        
class charge_répartie :
    
    def __init__(self, q): 
        self.q = q
        
class charge_répartie_partielle :
    
    def __init__(self, q, a, b, c): 
        self.q = q
        self.a = a
        self.b = b
        self.c = c
        
class charge_répartie_partielle_proche :
    
    def __init__(self, q, a):
        self.q = q
        self.a = a
        
class charge_triangulaire :
    
    def __init__(self, q, a, b): # Notre méthode constructeur
        self.q = q
        self.a = a
        self.b = b
        
class charge_triangulaire_monotone :
    
    def __init__(self, q): 
        self.q = q
        
class charge_répartie_partielle_proche :
    
    def __init__(self, q, a):
        self.q = q
        self.a = a
        
class charge_triangulaire_antisymétrique :
    
    def __init__(self, q):
        self.q = q
        
class charge_trapézoïdale_symétrique :
    
    def __init__(self, q, a, b): # Notre méthode constructeur
        self.q = q
        self.a = a
        self.b = b
        
class charge_parabolique :
    
    def __init__(self, q): 
        #
        
    
    