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
    
    def charge_concentrée_appuis_simples(self, hauteur, longueur, Igz, E, x, NbrePointsX):
        a = self.a
        b = longueur - self.a
        P = self.P
        # Réactions aux appuis 
        RA = -(P*b)/longueur
        RB = -(P*a)/longueur
    
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
    
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
    
        # Flèche de la poutre [mm]
        flèche = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] <= a :
                flèche[i] = -(P/(E*Igz*longueur))*((b/6)*(x[i]**3)+a*(longueur*a/2-(a**2)/6-(longueur**2)/3)*x[i])
            elif x[i] > a :
                flèche[i] = -P*a/(E*Igz*longueur)*(-(x[i]**3)/6+longueur*(x[i]**2)/2+(-(a**2)/6-(longueur**2)/3)*x[i]+((a**2)*longueur)/6)


        return RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche
        
    def charge_concentrée_encastrement(self, hauteur, longueur, Igz, E, x, NbrePointsX):
        a = self.a
        b = longueur - self.a
        P = self.P
        # Réactions aux liaisons
        RA = -P
        RB = 0
        
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
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        
        # Flèche de la poutre
        flèche = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] <= a :
                flèche[i] = -RA*(x[i]**2)/(6*E*Igz)*(3*a-x[i])  #-(RA/(E*Igz))*((x[i]**3)/6+a*(x[i]**2)/2)
            elif x[i] > a :
                flèche[i] = -RA*(a**2)/(6*E*Igz)*(3*x[i]-a) #-(RA/(E*Igz))*((3/2)*(a**2)*x[i]-(5/6)*(a**3))
        
        return RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche
        
class charge_répartie :
    nbr = 0
    def __init__(self, q): 
        self.q = q
        charge_répartie.nbr += 1
        
    def charge_répartie_appuis_simples(self, hauteur, longueur, Igz, E, x) :
        q = self.q
        # Réactions aux appuis
        RA = -(q*longueur)/2
        RB = -(q*longueur)/2
        
        # Efforts tranchants [N]
        EffortTranch = -((-q*longueur/2) + q*x) 
        
        # Moment Fléchissant [N.mm]
        Mf = -q*(longueur-x)*(x/2)
        
        # Contrainte pour y = h/2 [MPa]
        ContrainteYMax = -(Mf/Igz)*(hauteur/2)
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        
        # Flèche de la poutre
        flèche = q*x/(24*E*Igz)*((longueur**3)-2*longueur*(x**2)+(x**3))
        
        return RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche
        
    def charge_répartie_encastrement(self, hauteur, longueur, Igz, E, x):
        q = self.q
        # Réactions aux appuis (à améliorer quand y aura plus de 2 appuis)
        RA = q*longueur
        RB = 0
        
        # Efforts tranchants [N]
        EffortTranch = RA-q*x  # EffortTranch est de type <class 'numpy.ndarray'>. 
        
        # Moment Fléchissant [N.mm]
        Mf = (q/2)*(x-longueur)**2
        
        # Contrainte pour y = h/2 [MPa]
        ContrainteYMax = -(Mf/Igz)*(hauteur/2)
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        
        # Flèche de la poutre
        flèche = q*(((longueur-x)**4)+4*(longueur**3)*x-(longueur**4))/(24*E*Igz)
        
        return RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche
        
class charge_répartie_partielle :
    nbr = 0
    def __init__(self, q, a, b): 
        self.q = q
        self.a = a
        self.b = b
        charge_répartie_partielle.nbr += 1
        
    def charge_répartie_partielle_appuis_simples(self, hauteur, longueur, Igz, E, x, NbrePointsX):
        q = self.q
        a = self.a
        b = self.b
        c = longueur - (self.a + self.b)
        # Réactions aux appuis
        RA = -q*b*(b + 2*c)/(2*longueur)
        RB = -q*b*(b + 2*a)/(2*longueur)
        
        # Efforts tranchants [N]
        EffortTranch = np.linspace(0, 0, num=NbrePointsX)
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
                Mf[i] = (RA-q*a)*x[i]+q/2*((x[i])**2)+q/2*(a**2)
            elif x[i] > (a+b) :
                Mf[i] = RB*(longueur-x[i])
        
        # Contrainte pour y = h/2 [MPa]
        ContrainteYMax = -(Mf/Igz)*(hauteur/2)
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        
        # Flèche de la poutre 
        flèche = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] <= a :
                flèche[i] = -RA/(24*E*Igz)*(-4*(x[i]**3)+(4*(longueur**2)-((b+2*c)**2)-(b**2))*x[i])
            elif x[i] > a and x[i] <= (a+b):
                flèche[i] = q/(48*E*Igz*longueur)*(b*(b+2*c)*x[i]*(4*((longueur**2)-(x[i]**2))-((b+2*c)**2)-(b**2))+2*longueur*((x[i]-a)**4))
            elif x[i] > (a+b) :
                K5 = q/(48*longueur*RB)*(b*(b+2*c)*(4*(longueur**2)-12*((a+b)**2)-((b+2*c)**2)-(b**2))+2*longueur*(4*((a+b)**3)-12*a*((a+b)**2)+12*(a**2)*(a+b)-4*(a**3)))-longueur*(a+b)+((a+b)**2)/2
                K6 = -(longueur**3)/3-K5*longueur
                flèche[i] = RB*(longueur*(x[i]**2)/2-(x[i]**3)/6+K5*x[i]+K6)/(E*Igz)


        return RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche
        
class charge_répartie_partielle_proche :
    nbr = 0
    def __init__(self, q, l): 
        self.q = q
        self.l = l
        charge_répartie_partielle_proche.nbr += 1
        
    def charge_répartie_partielle_proche_appuis_simples(self, hauteur, longueur, Igz, E, x, NbrePointsX):
        q = self.q
        a = self.l
        # Réactions aux appuis
        RA = -q*a*(longueur - (a/2))/longueur
        RB = -q*(a**2)/(2*longueur)
        
        # Efforts tranchants [N]
        EffortTranch = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] <= a :
                EffortTranch[i] = -RA-q*x[i]
            elif x[i] > a and x[i] <= longueur :
                EffortTranch[i] = RB
                
        # Moment Fléchissant [N.mm]
        Mf = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] <= a : 
                Mf[i] = RA*x[i]+q*(x[i]**2)/2
            elif x[i] > a :
                Mf[i] = RB*(longueur-x[i])
                
        # Contrainte pour y = h/2 [MPa]
        ContrainteYMax = -(Mf/Igz)*(hauteur/2)
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        
        # Flèche de la poutre
        flèche = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] <= a :
                flèche[i] = q*x[i]*((a**2)*((2*longueur-a)**2)-2*a*(2*longueur-a)*(x[i]**2)+longueur*(x[i]**3))/(24*E*Igz*longueur)
            elif x[i] > a :
                flèche[i] = q*a**2*(longueur-x[i])*(4*longueur*x[i]-2*x[i]**2-a**2)/(24*E*Igz*longueur)
        
        return RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche
    
    def charge_répartie_partielle_proche_encastrement(self, hauteur, longueur, Igz, E, x, NbrePointsX):
        q = self.q
        a = self.l
        b = longueur - self.l
        # Réactions aux appuis
        RA = -q*b
        RB = 0
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
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        
        # Flèche de la poutre
        flèche = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] <= a :
                flèche[i] = RA/(E*Igz)*((x[i]**3)/6-(a+b/2)*(x[i]**2)/2)
            elif x[i] > a and x[i] <= (a+b):
                flèche[i] = RA/(E*Igz)*((x[i]**3)/6-(a+b/2)*(x[i]**2)/2)+q/(E*Igz)*((x[i]**4)/24-a*(x[i]**3)/6+(a**2)*(x[i]**2)/4-(a**3)*x[i]/6+(a**4)/24)
            elif x[i] > (a+b) :
                K5 = RA/(E*Igz)*(((a+b)**2)/2-(a+b/2)*(a+b))+q/(E*Igz)*(((a+b)**3)/6-a*((a+b)**2)/2+(a**2)*(a+b)/2-(a**3)/6)
                K6 = RA/(E*Igz)*(((a+b)**3)/6-(a+b/2)*((a+b)**2)/2)+q/(E*Igz)*(((a+b)**4)/24-a*((a+b)**3)/6+(a**2)*((a+b)**2)/4-(a**3)*(a+b)/6+(a**4)/24)-K5*(a+b)
                flèche[i] = K5*x[i]+K6
    
        return RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche
    
class charge_triangulaire :
    nbr = 0
    def __init__(self, q, a): # Notre méthode constructeur
        self.q = q
        self.a = a
        charge_triangulaire.nbr += 1
        
    def charge_triangulaire_appuis_simples(self, hauteur, longueur, Igz, E, x, NbrePointsX):
        q = self.q
        a = self.a
        b = longueur - a
        # Réactions aux appuis
        RA = -q*(longueur+b)/6 
        RB = -q*(longueur+a)/6 
        
        # Efforts tranchants [N]
        EffortTranch = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] <= a :
                EffortTranch[i] = -RA-q/(2*a)*(x[i]**2)
            elif x[i] > a and x[i] <= longueur :
                EffortTranch[i] = q/(6*b)*(3*(x[i]**2)-6*longueur*x[i]+2*(longueur**2)+(a**2))
        
        # Moment Fléchissant [N.mm]
        Mf = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] <= a : 
                Mf[i] = RA*x[i]+q/(6*a)*(x[i]**3)
            elif x[i] > a :
                Mf[i] = -q/(6*b)*((x[i]**3)-3*longueur*(x[i]**2)+(2*(longueur**2)+(a**2))*x[i]-(a**2)*longueur)
        
        # Contrainte pour y = h/2 [MPa]
        ContrainteYMax = -(Mf/Igz)*(hauteur/2)
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        
        # Flèche de la poutre
        flèche = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] <= a :
                flèche[i] = q*x[i]*(3*(x[i]**4)+a*(longueur+b)*(7*longueur**2-3*b**2-10*x[i]**2))/(360*E*Igz*a)
            elif x[i] > a :
                flèche[i] = q*(longueur-x[i])*(3*((longueur-x[i])**4)+b*(longueur+a)*(7*longueur**2-3*a**2-10*(longueur-x[i])**2))/(360*E*Igz*b)

        return RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche
        
class charge_triangulaire_monotone :
    nbr = 0
    def __init__(self, q): 
        self.q = q
        charge_triangulaire_monotone.nbr += 1
        
    def charge_triangulaire_monotone_appuis_simples(self, hauteur, longueur, Igz, E, x, NbrePointsX):
        q = self.q
        # Réactions aux appuis
        RA = -q*(longueur)/6 
        RB = -q*(longueur)/3 
        
        # Efforts tranchants [N]
        EffortTranch = q*((longueur**2)-3*(x**2))/(6*longueur)
        
        # Moment Fléchissant [N.mm]
        Mf = -q*x*((longueur**2)-(x**2))/(6*longueur)
        
        # Contrainte pour y = h/2 [MPa]
        ContrainteYMax = -(Mf/Igz)*(hauteur/2)
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        
        # Flèche de la poutre
        flèche = q*x*(longueur**2-x**2)*(7*longueur**2-3*x**2)/(360*E*Igz*longueur)

        return RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche

        
class charge_triangulaire_antisymétrique :
    nbr = 0
    def __init__(self, q):
        self.q = q
        charge_triangulaire_antisymétrique.nbr += 1
        
    def charge_triangulaire_antisymétrique_appuis_simples(self, hauteur, longueur, Igz, E, x, NbrePointsX):
        q = self.q
        # Réactions aux appuis
        RA = -q*(longueur)/6 
        RB = q*(longueur)/6 
        
        # Efforts tranchants [N]
        EffortTranch = q*(6*x**2-6*longueur*x+longueur**2)/(6*longueur)
        
        # Moment Fléchissant [N.mm]
        Mf = -q*x*(longueur-x)*(longueur-2*x)/(6*longueur)
        
        # Contrainte pour y = h/2 [MPa]
        ContrainteYMax = -(Mf/Igz)*(hauteur/2)
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        
        # Flèche de la poutre
        flèche = -q*x*(6*(x**4)-15*longueur*(x**3)+10*longueur**2*x**2-(longueur**4))/(360*E*Igz*longueur)

        return RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche

        
class charge_trapézoïdale_symétrique :
    nbr = 0
    def __init__(self, q, a, l): # Notre méthode constructeur
        self.q = q
        self.a = a
        self.l = l
        charge_trapézoïdale_symétrique.nbr += 1
        
    def charge_trapézoïdale_symétrique_appuis_simples(self, hauteur, longueur, Igz, E, x, NbrePointsX):
        q = self.q
        a = self.a
        b = self.l
        # Réactions aux appuis
        RA = -q*(longueur-a)/2
        RB = RA
        
        # Efforts tranchants [N]
        EffortTranch = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] <= a :
                EffortTranch[i] = q*(a*longueur-(a**2)-(x[i]**2))/(2*a) 
            elif x[i] > a and x[i] <= (a+b):
                EffortTranch[i] = q*(longueur-2*x[i])/2
            elif x[i] > (a+b) and x[i] <= longueur :
                EffortTranch[i] = q*(((longueur-x[i])**2)-a*(longueur-a))/(2*a)
        
        # Moment Fléchissant [N.mm]
        Mf = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] <= a :
                Mf[i] = -q*x[i]*(3*a*longueur-3*(a**2)-(x[i]**2))/(6*a)
            elif x[i] > a and x[i] <= (a+b):
                Mf[i] = -q*(3*longueur*x[i]-3*(x[i]**2)-(a**2))/6 
            elif x[i] > (a+b) :
                Mf[i] = -q*(longueur-x[i])*(3*a*(longueur-a)-((longueur-x[i])**2))/(6*a)
        
        # Contrainte pour y = h/2 [MPa]
        ContrainteYMax = -(Mf/Igz)*(hauteur/2)
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        # Flèche de la poutre
        flèche = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        flèche = 0*x #pas de flèche encore
        FlècheMax = -(q/(1920*E*Igz))*(5*longueur**2 - 4*a**2)**2
        
        return RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche

        
class charge_parabolique :
    nbr = 0
    def __init__(self, q): 
        self.q = q
        charge_parabolique.nbr += 1
        
    def charge_parabolique_appuis_simples(self, hauteur, longueur, Igz, E, x, NbrePointsX):
        q = self.q
        # Réactions aux appuis
        RA = -q*longueur/3 
        RB = RA 
        
        # Efforts tranchants [N]
        EffortTranch = q*(4*(x**3)-(6*longueur*(x**2))+(longueur**3))/(3*(longueur**2))
        
        # Moment Fléchissant [N.mm]
        Mf = -q*x*((x**3)-2*longueur*(x**2)+(longueur**3))/(3*(longueur**2))
        
        # Contrainte pour y = h/2 [MPa]
        ContrainteYMax = -(Mf/Igz)*(hauteur/2)
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        
        # Flèche de la poutre
        flèche = -q/(3*(longueur**2)*E*Igz)*((x**6)/30-2*longueur*(x**5)/20+(longueur**3)*(x**3)/6-(longueur**5)/10*x)

        return RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche

        
class couple :
    nbr = 0
    def __init__(self, C, a): 
        self.C = C
        self.a = a
        couple.nbr += 1
        
    def couple_appuis_simples(self, hauteur, longueur, Igz, E, x, NbrePointsX):
        C = self.C
        a = self.a
        # Réactions aux appuis
        RA = C/longueur 
        RB = -RA
        
        # Efforts tranchants [N]
        EffortTranch = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            EffortTranch[i] = -RA
        
        # Moment Fléchissant [N.mm]
        Mf = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] <= a : 
                Mf[i] = C*x[i]/longueur
            elif x[i] > a :
                Mf[i] = -C*(longueur-x[i])/longueur
        
        # Contrainte pour y = h/2 [MPa]
        ContrainteYMax = -(Mf/Igz)*(hauteur/2)
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        
        # Flèche de la poutre
        flèche = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] <= a :
                flèche[i] = C*x[i]*(x[i]**2-longueur**2+3*(longueur-a)**2)/(6*E*Igz*longueur)
            elif x[i] > a :
                flèche[i] = C*((x[i]**3)-3*longueur*x[i]**2+(2*longueur**2+3*a**2)*x[i]-3*(a**2)*longueur)/(6*E*Igz*longueur)

        return RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche
        
    def couple_encastrement(self, hauteur, longueur, Igz, E, x, NbrePointsX):
        C = self.C
        a = self.a
        # Réactions aux appuis
        RA = 0
        RB = 0
        
        # Efforts tranchants [N]
        EffortTranch = 0
        
        # Moment Fléchissant [N.mm]
        Mf = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] <= a : 
                Mf[i] = C
            elif x[i] > a :
                Mf[i] = 0
        
        # Contrainte pour y = h/2 [MPa]
        ContrainteYMax = -(Mf/Igz)*(hauteur/2)
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        
        # Flèche de la poutre
        flèche = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] <= a :
                flèche[i] = -C*(x[i]**2)/(2*E*Igz)
            elif x[i] > a :
                flèche[i] = -C*a*(x[i]-a/2)/(E*Igz)
        
        return RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche

        
class couple_réparti :
    nbr = 0
    def __init__(self, C): 
        self.C = C
        couple_réparti.nbr += 1
        
    def couple_réparti_appuis_simples(self, hauteur, longueur, Igz, E, x, NbrePointsX):
        C = self.C
        # Réactions aux appuis
        RA = C
        RB = -C 
        
        # Efforts tranchants [N]
        EffortTranch = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            EffortTranch[i] = -C
        
        # Moment Fléchissant [N.mm]
        Mf = 0*x
        
        # Contrainte pour y = h/2 [MPa]
        ContrainteYMax = -(Mf/Igz)*(hauteur/2)
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        
        # Flèche de la poutre
        flèche = 0*x
        
        return RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche

        
class charge_croissante :
    nbr = 0
    def __init__(self, q): 
        self.q = q
        charge_croissante.nbr += 1
        
    def charge_croissante_encastrement(self, hauteur, longueur, Igz, E, x):
        q = self.q
        # Réactions aux appuis 
        RA = -q*longueur/2
        RB = 0
        
        # Efforts tranchants [N]
        EffortTranch = RA*((x**2)/(longueur**2)-1)  # EffortTranch est de type <class 'numpy.ndarray'>. 
        
        # Moment Fléchissant [N.mm]
        Mf = q*((longueur-x)**2)*(2*longueur+x)/(6*longueur)
        
        # Contrainte pour y = h/2 [MPa]
        ContrainteYMax = -(Mf/Igz)*(hauteur/2)
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        
        # Flèche de la poutre
        flèche = q*(x**2)*(20*(longueur**3)-10*longueur**2*x+(x**3))/(120*E*Igz*longueur)
        
        return RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche


class charge_décroissante :
    nbr = 0
    def __init__(self, q): 
        self.q = q
        charge_décroissante.nbr += 1
        
    def charge_décroissante_encastrement(self, hauteur, longueur, Igz, E, x):
        q = self.q
        # Réactions aux appuis 
        RA = -q*longueur/2
        RB = 0
        
        # Efforts tranchants [N]
        EffortTranch = q*((longueur-x)**2)/(2*longueur)
        
        # Moment Fléchissant [N.mm]
        Mf = q*((longueur-x)**3)/(6*longueur)
        
        # Contrainte pour y = h/2 [MPa]
        ContrainteYMax = -(Mf/Igz)*(hauteur/2)
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        
        # Flèche de la poutre
        flèche = q*(4*(longueur**5)-5*(longueur**4)*(longueur-x)+((longueur-x)**5))/(120*E*Igz*longueur)
        
        return RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche

    