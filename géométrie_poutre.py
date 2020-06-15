# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:02:26 2020

@author: Simon
"""

def géométrie_poutre(hauteur, longueur, largeur, MasseVol, géométrie):
    
    géométrie = 1
    switch(géométrie) 
        case 1 : 
            hauteur = 1 ;
        break;
        case 2 : 
            hauteur = 1 ;
        break;
        
    
    # Masse de la poutre
    Masse = largeur*longueur*hauteur*MasseVol*(10^(-6))
    
    # Moment d'inertie (à améliorer quand la géométrie changera) [mm^4]
    Igz = (largeur *(pow(hauteur,3)))/12
    
    return Masse, Igz