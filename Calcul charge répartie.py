# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:12:41 2020
@author: Simon
"""
import numpy as np
import matplotlib.pyplot as plt

# LES IMPUTS SONT :

    # Géométrie de la poutre :
hauteur = float(input('Entrer la hauteur de la poutre en mm : '))
longueur = float(input('Entrer la longueur de la poutre en mm : '))
largeur = float(input('Entrer la largeur de la poutre en mm : '))
    # Pour l'instant considérons une poutre rectangulaire remplie, on fera les géométries Igz complexes plus tard
    
    # Matériau de la poutre :
matériau = input('Quel est le matériau utilisé ?')
E = float(input('Entrer son Module de Young de la poutre en MPa:'))
MasseVol = float(input('Entrer sa Masse Volumique de la poutre en g/cm^3:'))
LimElast = float(input('Entrer sa limite élastique MPa:'))
    # plus tard dans le projet, on pourrait importer une base de données pour faire en sorte qu'avec la seule connaissance du matériau, le logiciel pourrait en déduire automatiquement E, la masse volumque etc...

    # Forces appliquées
q = float(input('Entrer la Force linéique de la charge répartie en N/mm :')) 

    # Discrétisations (pour l'instant le pas ne peut pas être choisis mais il pourra l'être plus tard)
NbrePoints = 100 # réfléchir au nom
x = np.linspace(0, longueur, NbrePoints+1)
print(x)

# LES CALCULS :
# fonction que l'on pourra appeler qui s'occupe de calculer différentes données d'une poutre qui subit seulement une charge répartie

def charge_répartie(hauteur, longueur, largeur, matériau, E, MasseVol, LimElast, q) :
    
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
    print(FlècheMax = max(x))
    
    plt.figure(1) #Ma première figure
    plt.xlabel("x") 
    plt.ylabel("flèche") 
    plt.title("Tracé de la flèche") #Titre de la courbe
    plt.plot(x,flèche,label="flèche") #Le tracé en lui-même
    plt.legend('salut') 
    plt.show()

charge_répartie(hauteur, longueur, largeur, matériau, E, MasseVol, LimElast, q) 