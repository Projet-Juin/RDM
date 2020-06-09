# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:12:41 2020
@author: Simon
"""
import numpy as np
import matplotlib.pyplot as plt
import charge_répartie

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


charge_répartie.charge_répartie(hauteur, longueur, largeur, matériau, E, MasseVol, LimElast, q, x) 