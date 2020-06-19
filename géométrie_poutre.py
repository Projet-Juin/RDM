# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:02:26 2020

@author: Simon
"""
import math

def géométrie_poutre(hauteur, longueur, largeur, MasseVol):
    
    Masse = largeur*hauteur*longueur*MasseVol*(10^(-6))
    Igz = (largeur *(pow(hauteur,3)))/12
    # if géométrie == 'carré' :
    #     S = a**2
    #     Igz = (S**2)/12 #[mm^4]
        
    # elif géométrie == 'carré vide' :
    #     S = A**2 - a**2
    #     Igz = ((A**4)-(a**4))/12
        
    # elif géométrie == 'rectangle' :
    #     S = hauteur*largeur
    #     Igz = (largeur *(pow(hauteur,3)))/12
    
    # elif géométrie == 'rectangle vide' :
    #     S = hauteur*largeur - phauteur*plargeur
    #     Igz = ((largeur*(hauteur**3)) - plargeur*(phauteur**3))/12
        
    # elif géométrie == 'I' :
    #     S = hauteur*largeur - phauteur*(largeur-plargeur)
    #     Igz = (largeur*(hauteur**3)-(phauteur**3)*(largeur-plargeur)/12
    
    return Masse, Igz
        
    # elif géométrie == 'T' :
    #     S = hauteur*largeur - phauteur*(largeur-plargeur)
    #     Igz = ((largeur**2)*(hauteur**4) + phauteur*(largeur-plargeur)*((phauteur**3)*(largeur-plargeur)+6*largeur*(hauteur**2)*(phauteur**2)-4*largeur*(hauteur**3)*phauteur-4*largeur*hauteur*(phauteur**3)))/(12*S)
        
    # elif géométrie == 'L' :
    #     S = hauteur*largeur - phauteur*(largeur-plargeur)
    #     Igz = ((largeur-plargeur)*(4*largeur*hauteur*((hauteur-phauteur)**3)-((hauteur-phauteur)**3)*(largeur-plargeur)*(3*(hauteur-phauteur)+4*phauteur)-6*((hauteur-phauteur)**2)*plargeur*(hauteur**2)-4*plargeur*(hauteur**3)*phauteur)-(hauteur**4)*plargeur*(4*largeur-3*plargeur))/(12*S)

    # elif géométrie == 'Z' :
    #     S = hauteur*largeur - phauteur*(largeur-plargeur)
    #     Igz = (largeur*(hauteur**3)-(phauteur**3)*(largeur-plargeur))/12
        
    # elif géométrie == 'triangle' :
    #     S = hauteur*largeur/2
    #     Igz = largeur*(hauteur**3)/36
        
    # elif géométrie == 'cercle' :
    #     S = (math.pi * diamètre**2)/4
    #     Igz = (math.pi * (diamètre**4)) / 64
        
    # elif géométrie == 'anneau' :
    #     S = (math.pi * (diamètre**2 - pdiamètre**2)/4
    #     Igz = (math.pi * (diamètre**4)-(pdiamètre**4))/64
        
    # elif géométrie == 'demi cercle' :
    #     S = (math.pi * (diamètre**2))/8
    #     Igz = (diamètre**4)*((math.pi/8)-8/(9*math.pi))/16
        
    # elif géométrie == 'quart cercle' :
    #     S = (math.pi*((diamètre/2)**2))/8
    #     Igz = ((diamètre/2)**4)*((math.pi/8)-8/(9*math.pi))/2
        
# #    elif géométrie == 'ellipse' :
#         S = (math.pi*largeur*hauteur)/4
#         Igz = (math.pi*largeur*(hauteur**2))/65
        
    # elif géométrie == 'croix' :
    #     S = 2*plargeur*hauteur - plargeur**2
    #     Igz = (plargeur*(hauteur**3)+(plargeur**3)*hauteur-(plargeur**4))/12
        
    # elif géométrie == 'losange' :
    #     S = hauteur**2/2
    #     Igz = (hauteur**4)/48
        


    