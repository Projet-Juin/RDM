# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:17:14 2020
@author: Simon
"""

import numpy as np
import matplotlib.pyplot as plt
import charge_répartie

# LES IMPUTS SONT :

    # Géométrie de la poutre :
hauteur = 100
longueur = 20000
largeur = 200
    # Pour l'instant considérons une poutre rectangulaire remplie, on fera les géométries Igz complexes plus tard
    
    # Matériau de la poutre :
matériau = 'bois'
E = 12000
MasseVol = 0.75
LimElast = 40
    # plus tard dans le projet, on pourrait importer une base de données pour faire en sorte qu'avec la seule connaissance du matériau, le logiciel pourrait en déduire automatiquement E, la masse volumque etc...

    # Forces appliquées
q = -200
    
    # Discrétisations (pour l'instant le pas ne peut pas être choisis mais il pourra l'être plus tard)
NbrePointsX = 100 
x = np.linspace(0, longueur, NbrePointsX+1)
NbrePointsY = 40
y = np.linspace(0, hauteur, NbrePointsY+1)

# LES CALCULS :
# fonction que l'on pourra appeler qui s'occupe de calculer différentes données d'une poutre qui subit seulement une charge répartie

    
charge_répartie.charge_répartie(hauteur, longueur, largeur, matériau, E, MasseVol, LimElast, q, x, y) 