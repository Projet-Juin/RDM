# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:17:14 2020

@author: Simon
"""

import numpy as np
import matplotlib.pyplot as plt
import classe
import géométrie_poutre
import Appuis_simples

# LES IMPUTS SONT :

    # Géométrie de la poutre :
hauteur = 10
longueur = 1200
largeur = 20
    # Pour l'instant considérons une poutre rectangulaire remplie, on fera les géométries Igz complexes plus tard
    
    # Matériau de la poutre :
matériau = 'bois'
E = 210000
MasseVol = 0.75
LimElast = 40
géométrie = 'carré'
    # plus tard dans le projet, on pourrait importer une base de données pour faire en sorte qu'avec la seule connaissance du matériau, le logiciel pourrait en déduire automatiquement E, la masse volumque etc...

(Masse, Igz) = géométrie_poutre.géométrie_poutre(hauteur, longueur, largeur, MasseVol)

    # Forces appliquées [N.mm]
q = -200
P = -200
a = 600
c = 500
b = longueur - a 
    
    # Discrétisations (pour l'instant le pas ne peut pas être choisis mais il pourra l'être plus tard)
NbrePointsX = 101
x = np.linspace(0, longueur, NbrePointsX)
NbrePointsY = 41
y = np.linspace(0, hauteur, NbrePointsY)

# LES CALCULS :

# a = classe.charge_concentrée(P,a)
# a.charge_concentrée_appuis_simples(hauteur, longueur, Igz, E, x, NbrePointsX)

# fonction que l'on pourra appeler qui s'occupe de calculer différentes données d'une poutre qui subit seulement une charge répartie
    
#(RACR, RBCR, EffortTranchCR, MfCR, ContrainteYMaxCR, ContrainteMaxCR, DefYMaxCR, DefMaxCR, flècheCR, FlècheMaxCR, \
#GrapheEffortTranchCR, GrapheMfCR, GrapheContrainteYMaxCR, GrapheDefYMaxCR, GrapheFlècheCR) = \
#Appuis_simples.charge_répartie(hauteur, longueur, Igz, E, LimElast, q, x) 
  
(RA, RB, EffortTranch, Mf, ContrainteYMax, ContrainteMax, DefYMax, DefMax, flèche, FlècheMax) = Appuis_simples.charge_concentrée(hauteur, longueur, Igz, E, LimElast, P, x, NbrePointsX, a, b)
(RA1, RB1, EffortTranch1, Mf1, ContrainteYMax1, ContrainteMax1, DefYMax1, DefMax1, flèche1, FlècheMax1) = Appuis_simples.charge_concentrée(hauteur, longueur, Igz, E, LimElast, P, x, NbrePointsX, a, b)
print("RA = ", RA + RA1, "RB = ", RB+RB1, "ContrainteMax = ", ContrainteMax+ContrainteMax1, "DefMax = ", DefMax+DefMax1, "FlècheMax = ", FlècheMax+FlècheMax1)
    

#(RACCE, EffortTranchCCE, MfCCE, ContrainteYMaxCCE, ContrainteMaxCCE, DefYMaxCCE, DefMaxCCE, flècheCCE, FlècheMaxCCE) = \
#Liaison_encastrement.charge_concentrée(hauteur, longueur, Igz, E, LimElast, P, x, NbrePointsX, a, b)

#(RA, EffortTranch, Mf, ContrainteYMax, ContrainteMax, DefYMax, DefMax, flèche, FlècheMax) = \
#Liaison_encastrement.charge_répartie(hauteur, longueur, Igz, E, LimElast, q, x)

#Liaison_encastrement.charge_croissante(hauteur, longueur, Igz, E, LimElast, q, x)
    
#Liaison_encastrement.charge_décroissante(hauteur, longueur, Igz, E, LimElast, q, x)

#(RA, RB, EffortTranch, Mf, ContrainteYMax, ContrainteMax, DefYMax, DefMax, flèche, FlècheMax)\
#Appuis_simples.charge_répartie_partielle(hauteur, longueur, Igz, E, LimElast, q, x, NbrePointsX, a, b, c)

#Appuis_simples.charge_répartie_partielle_proche(hauteur, longueur, Igz, E, LimElast, q, x, NbrePointsX, a)

#Appuis_simples.charge_triangulaire(hauteur, longueur, Igz, E, LimElast, q, x, NbrePointsX, a, b)

#Appuis_simples.charge_triangulaire_monotone(hauteur, longueur, Igz, E, LimElast, q, x, NbrePointsX)

#Appuis_simples.charge_triangulaire_antisymétrique(hauteur, longueur, Igz, E, LimElast, q, x, NbrePointsX)

#Appuis_simples.charge_trapézoïdale_symétrique(hauteur, longueur, Igz, E, LimElast, q, x, NbrePointsX, a, b)

#Appuis_simples.charge_parabolique(hauteur, longueur, Igz, E, LimElast, q, x, NbrePointsX)
#2