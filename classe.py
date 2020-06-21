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
        
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        DefMax = np.amax(abs(DefYMax))
        
        # Flèche de la poutre
        flèche = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] <= a :
                flèche[i] = -(P/(E*Igz*longueur))*((b/6)*(x[i]**3)+a*(longueur*a/2-(a**2)/6-(longueur**2)/3)*x[i])
            elif x[i] > a :
                flèche[i] = -P*a/(E*Igz*longueur)*(-(x[i]**3)/6+longueur*(x[i]**2)/2+(-(a**2)/6-(longueur**2)/3)*x[i]+((a**2)*longueur)/6)
        FlècheMax = np.amax(abs(flèche))
        
    def charge_concentrée_encastrement(self, hauteur, longueur, Igz, E, x, NbrePointsX):
        a = self.a
        b = longueur - self.a
        P = self.P
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
        ContrainteMax = np.amax(abs(ContrainteYMax))
        
        # Contrainte pour tout y [MPa]
        #Contrainte = np.matmul(-(Mf/Igz),y)
        
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        DefMax = np.amax(abs(DefYMax))
        
        # Flèche de la poutre
        flèche = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] <= a :
                flèche[i] = -RA*(x[i]**2)/(6*E*Igz)*(3*a-x[i])  #-(RA/(E*Igz))*((x[i]**3)/6+a*(x[i]**2)/2)
            elif x[i] > a :
                flèche[i] = -RA*(a**2)/(6*E*Igz)*(3*x[i]-a) #-(RA/(E*Igz))*((3/2)*(a**2)*x[i]-(5/6)*(a**3))
        FlècheMax = np.amax(abs(flèche))
        
class charge_répartie :
    nbr = 0
    def __init__(self, q): 
        self.q = q
        charge_répartie.nbr += 1
        
    def charge_répartie_appuis_simples(hauteur, longueur, Igz, E, x) :
        q = self.q
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
        ContrainteMax = np.amax(abs(ContrainteYMax))
        print('contrainte max = ', ContrainteMax)
        
        # Contrainte pour tout y [MPa]
        #Contrainte = np.matmul(-(Mf/Igz),y)
        
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        DefMax = np.amax(abs(DefYMax))
        print('DefMax', DefMax)
        
        # Flèche de la poutre
        flèche = q*x/(24*E*Igz)*((longueur**3)-2*longueur*(x**2)+(x**3))
        FlècheMax = np.amax(abs(flèche))
        
    def charge_répartie_encastrement(hauteur, longueur, Igz, E, x):
        q = self.q
        # Réactions aux appuis (à améliorer quand y aura plus de 2 appuis)
        RA = q*longueur
        
        # Efforts tranchants [N]
        EffortTranch = RA-q*x  # EffortTranch est de type <class 'numpy.ndarray'>. 
        
        # Moment Fléchissant [N.mm]
        Mf = (q/2)*(x-longueur)**2
        
        # Contrainte pour y = h/2 [MPa]
        ContrainteYMax = -(Mf/Igz)*(hauteur/2)
        ContrainteMax = np.amax(abs(ContrainteYMax))
        
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        DefMax = np.amax(abs(DefYMax))
        
        # Flèche de la poutre
        flèche = q*(((longueur-x)**4)+4*(longueur**3)*x-(longueur**4))/(24*E*Igz)
        FlècheMax = np.amax(abs(flèche))
        
class charge_répartie_partielle :
    nbr = 0
    def __init__(self, q, a, b): 
        self.q = q
        self.a = a
        self.b = b
        charge_répartie_partielle.nbr += 1
        
    def charge_répartie_partielle_appuis_simples(hauteur, longueur, Igz, E, x, NbrePointsX):
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
        ContrainteMax = np.amax(abs(ContrainteYMax))
        
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        DefMax = np.amax(abs(DefYMax))
        
        # Flèche de la poutre        ##NE FONCTIONNE PAS
        flèche = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] <= a :
                flèche[i] = -RA/(E*Igz)*((x[i]**3)/6-(q/(48*longueur*RA)*b*(b+2*c)*(4*((longueur**2)-(a**2))-((b+2*c)**2)-(b**2))+(a**2)/6)*x[i])
            elif x[i] > a and x[i] <= (a+b):
                flèche[i] = q/(48*E*Igz*longueur)*(b*(b+2*c)*x[i]*(4*((longueur**2)-(x[i]**2))-((b+2*c)**2)-(b**2))+2*longueur*((x[i]-a)**4))
            elif x[i] > (a+b) :
                flèche[i] = -RB/(E*Igz)*(longueur*(x[i]**2)/2-(x[i]**3)/6+((1/c)*(q/(48*longueur*RB)*(b*(b+2*c)*(a+b)*(4*((longueur**2)-((a+b)**2))-((b+2*c)**2)-(b**2))+2*longueur*(b**4))+longueur*((a+b)**2)/2-((a+b)**3)/6-(longueur**3)/3))*(x[i]-longueur)-(longueur**3)/3)
        FlècheMax = np.amax(abs(flèche))

        
class charge_triangulaire :
    nbr = 0
    def __init__(self, q, a): # Notre méthode constructeur
        self.q = q
        self.a = a
        charge_triangulaire.nbr += 1
        
    def charge_triangulaire_appuis_simples(hauteur, longueur, Igz, E, x, NbrePointsX):
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
        ContrainteMax = np.amax(abs(ContrainteYMax))
        
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        DefMax = np.amax(abs(DefYMax))
        
        # Flèche de la poutre
        flèche = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] <= a :
                flèche[i] = q*x[i]*(3*(x[i]**4)+a*(longueur+b)*(7*longueur**2-3*b**2-10*x[i]**2))/(360*E*Igz*a)
            elif x[i] > a :
                flèche[i] = q*(longueur-x[i])*(3*((longueur-x[i])**4)+b*(longueur+a)*(7*longueur**2-3*a**2-10*(longueur-x[i])**2))/(360*E*Igz*b)
        FlècheMax = np.amax(abs(flèche))
        
        
class charge_triangulaire_monotone :
    nbr = 0
    def __init__(self, q): 
        self.q = q
        charge_triangulaire_monotone.nbr += 1
        
    def charge_triangulaire_monotone_appuis_simples(hauteur, longueur, Igz, E, x, NbrePointsX):
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
        ContrainteMax = np.amax(abs(ContrainteYMax))
        
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        DefMax = np.amax(abs(DefYMax))
        
        # Flèche de la poutre
        flèche = q*x*(longueur**2-x**2)*(7*longueur**2-3*x**2)/(360*E*Igz*longueur)
        FlècheMax = np.amax(abs(flèche))

        
class charge_triangulaire_antisymétrique :
    nbr = 0
    def __init__(self, q):
        self.q = q
        charge_triangulaire_antisymétrique.nbr += 1
        
    def charge_triangulaire_antisymétrique_appuis_simples(hauteur, longueur, Igz, E, x, NbrePointsX):
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
        ContrainteMax = np.amax(abs(ContrainteYMax))
        
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        DefMax = np.amax(abs(DefYMax))
        
        # Flèche de la poutre
        flèche = -q*x*(6*(x**4)-15*longueur*(x**3)+10*longueur**2*x**2-(longueur**4))/(360*E*Igz*longueur)
        FlècheMax = np.amax(abs(flèche))

        
class charge_trapézoïdale_symétrique :
    nbr = 0
    def __init__(self, q, a, l): # Notre méthode constructeur
        self.q = q
        self.a = a
        self.l = l
        charge_trapézoïdale_symétrique.nbr += 1
        
    def charge_trapézoïdale_symétrique_appuis_simples(hauteur, longueur, Igz, E, x, NbrePointsX):
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
        ContrainteMax = np.amax(abs(ContrainteYMax))
        
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        DefMax = np.amax(abs(DefYMax))
        
        # Flèche de la poutre
        flèche = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] <= a :
                flèche[i]=0
            elif x[i] > a and x[i] <= (a+b):
                 flèche[i]=0
            elif x[i] > (a+b) :
              flèche[i]=0
        flèche = 0*x #pas de flèche encore
        FlècheMax = np.amax(abs(flèche))

        
class charge_parabolique :
    nbr = 0
    def __init__(self, q): 
        self.q = q
        charge_parabolique.nbr += 1
        
    def charge_parabolique_appuis_simples(hauteur, longueur, Igz, E, x, NbrePointsX):
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
        ContrainteMax = np.amax(abs(ContrainteYMax))
        
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        DefMax = np.amax(abs(DefYMax))
        
        # Flèche de la poutre
        flèche = -q/(3*(longueur**2)*E*Igz)*((x**6)/30-2*longueur*(x**5)/20+(longueur**3)*(x**3)/6-(longueur**5)/10*x)
        FlècheMax = np.amax(abs(flèche))

        
class couple :
    nbr = 0
    def __init__(self, C, a): 
        self.C = C
        self.a = a
        couple.nbr += 1
        
    def couple_appuis_simples(hauteur, longueur, Igz, E, x, NbrePointsX):
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
        ContrainteMax = np.amax(abs(ContrainteYMax))
        
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        DefMax = np.amax(abs(DefYMax))
        
        # Flèche de la poutre
        flèche = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] <= a :
                flèche[i] = C*x[i]*(x[i]**2-longueur**2+3*(longueur-a)**2)/(6*E*Igz*longueur)
            elif x[i] > a :
                flèche[i] = C*((x[i]**3)-3*longueur*x[i]**2+(2*longueur**2+3*a**2)*x[i]-3*(a**2)*longueur)/(6*E*Igz*longueur)
        FlècheMax = np.amax(abs(flèche))
        
    def couple_encastrement(hauteur, longueur, Igz, E, x, NbrePointsX):
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
        ContrainteMax = np.amax(abs(ContrainteYMax))
        
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        DefMax = np.amax(abs(DefYMax))
        
        # Flèche de la poutre
        flèche = np.linspace(0, NbrePointsX-1, num=NbrePointsX)
        for i in range(NbrePointsX):
            if x[i] <= a :
                flèche[i] = -C*(x[i]**2)/(2*E*Igz)
            elif x[i] > a :
                flèche[i] = -C*a*(x[i]-a/2)/(E*Igz)
        FlècheMax = np.amax(abs(flèche))

        
class couple_réparti :
    nbr = 0
    def __init__(self, C): 
        self.C = C
        couple_réparti.nbr += 1
        
    def couple_réparti_appuis_simples(hauteur, longueur, Igz, E, x, NbrePointsX):
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
        ContrainteMax = np.amax(abs(ContrainteYMax))
        
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        DefMax = np.amax(abs(DefYMax))
        
        # Flèche de la poutre
        flèche = 0*x
        FlècheMax = np.amax(abs(flèche))

        
class charge_croissante :
    nbr = 0
    def __init__(self, q): 
        self.q = q
        charge_croissante.nbr += 1
        
    def charge_croissante_encastrement(hauteur, longueur, Igz, E, x):
        q = self.q
        # Réactions aux appuis 
        RA = -q*longueur/2
        
        # Efforts tranchants [N]
        EffortTranch = RA*((x**2)/(longueur**2)-1)  # EffortTranch est de type <class 'numpy.ndarray'>. 
        
        # Moment Fléchissant [N.mm]
        Mf = q*((longueur-x)**2)*(2*longueur+x)/(6*longueur)
        
        # Contrainte pour y = h/2 [MPa]
        ContrainteYMax = -(Mf/Igz)*(hauteur/2)
        ContrainteMax = np.amax(abs(ContrainteYMax))
        
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        DefMax = np.amax(abs(DefYMax))
        
        # Flèche de la poutre
        flèche = q*(x**2)*(20*(longueur**3)-10*longueur**2*x+(x**3))/(120*E*Igz*longueur)
        FlècheMax = np.amax(abs(flèche))


class charge_décroissante :
    nbr = 0
    def __init__(self, q): 
        self.q = q
        charge_décroissante.nbr += 1
        
    def charge_décroissante_encastrement(hauteur, longueur, Igz, E, x):
        q = self.q
        # Réactions aux appuis 
        RA = -q*longueur/2
        
        # Efforts tranchants [N]
        EffortTranch = q*((longueur-x)**2)/(2*longueur)
        
        # Moment Fléchissant [N.mm]
        Mf = q*((longueur-x)**3)/(6*longueur)
        
        # Contrainte pour y = h/2 [MPa]
        ContrainteYMax = -(Mf/Igz)*(hauteur/2)
        ContrainteMax = np.amax(abs(ContrainteYMax))
        
        # Déformation pour y = h/2 [SD]
        DefYMax = ContrainteYMax/E
        DefMax = np.amax(abs(DefYMax))
        
        # Flèche de la poutre
        flèche = q*(4*(longueur**5)-5*(longueur**4)*(longueur-x)+((longueur-x)**5))/(120*E*Igz*longueur)
        FlècheMax = np.amax(abs(flèche))

    