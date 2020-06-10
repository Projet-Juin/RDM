# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:17:14 2020

@author: Simon
"""

import numpy as np
import matplotlib.pyplot as plt
import charge_répartie
import charge_concentrée
import géométrie_poutre
import charge_concentrée_encastrement

# LES IMPUTS SONT :

    # Géométrie de la poutre :
hauteur = 100
longueur = 20000
largeur = 200
    # Pour l'instant considérons une poutre rectangulaire remplie, on fera les géométries Igz complexes plus tard
    
    # Matériau de la poutre :
matériau = 'bois'
E = 210000
MasseVol = 0.75
LimElast = 40
    # plus tard dans le projet, on pourrait importer une base de données pour faire en sorte qu'avec la seule connaissance du matériau, le logiciel pourrait en déduire automatiquement E, la masse volumque etc...

(Masse, Igz) = géométrie_poutre.géométrie_poutre(hauteur, longueur, largeur, MasseVol)

    # Forces appliquées
q = -200
P = -1000
a = 10000
b = longueur - a
    
    # Discrétisations (pour l'instant le pas ne peut pas être choisis mais il pourra l'être plus tard)
NbrePointsX = 101 
x = np.linspace(0, longueur, NbrePointsX)
NbrePointsY = 41
y = np.linspace(0, hauteur, NbrePointsY)

# LES CALCULS :
# fonction que l'on pourra appeler qui s'occupe de calculer différentes données d'une poutre qui subit seulement une charge répartie
    
(RACC, RBCR, EffortTranchCR, MfCR, ContrainteYMaxCR, ContrainteMaxCR, DefYMaxCR, DefMaxCR, flècheCR, FlècheMaxCR, \
GrapheEffortTranchCR, GrapheMfCR, GrapheContrainteYMaxCR, GrapheDefYMaxCR, GrapheFlècheCR) = \
charge_répartie.charge_répartie(hauteur, longueur, Igz, E, LimElast, q, x) 
  
(RACC, RBCC, EffortTranchCC, MfCC, ContrainteYMaxCC, ContrainteMaxCC, DefYMaxCC, DefMaxCC, flècheCC, FlècheMaxCC, \
GrapheEffortTranchCC, GrapheMfCC, GrapheContrainteYMaxCC, GrapheDefYMaxCC, GrapheFlècheCC) = \
charge_concentrée.charge_concentrée(hauteur, longueur, Igz, E, LimElast, P, x, NbrePointsX, a, b)

(RACCE, EffortTranchCCE, MfCCE, ContrainteYMaxCCE, ContrainteMaxCCE, DefYMaxCCE, DefMaxCCE, flècheCCE, FlècheMaxCCE) = \
charge_concentrée_encastrement.charge_concentrée_encastrement(hauteur, longueur, Igz, E, LimElast, P, x, NbrePointsX, a, b)