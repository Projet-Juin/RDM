# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:44:02 2020

@author: Simon
"""
import numpy as np
import matplotlib.pyplot as plt

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
Igz = (largeur *(pow(hauteur,3)))/12

NbrePointsX = 100 
x = np.linspace(0, longueur, NbrePointsX+1)
# np.mat(x)
NbrePointsY = 40
y = np.linspace(0, hauteur, NbrePointsY+1)
# np.mat(y)
print('y = ', y, 'nombre de lignes : ', np.shape(y)[0], 'nombre de colonnes : ', np.shape(y)[1])

Mf = q*(longueur-x)*(x/2)
Mf.reshape(101,1)
print('mf = ', Mf, '\n', 'avec des éléments de type : ', Mf.dtype, 'nmbre de lignes : ', np.shape(Mf)[0], '\n', 'nombre de colonnes : ', np.shape(Mf)[0])
# calcul = (-1/Igz)*np.matmul(Mf,y)
# print(calcul)



