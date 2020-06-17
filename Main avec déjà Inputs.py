# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:17:14 2020

@author: Simon
"""

import numpy as np
import matplotlib.pyplot as plt
import Appuis_simples
import Liaison_encastrement
import géométrie_poutre

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
P = 0
a = 0
b = longueur - a
c = 0
    
    # Discrétisations (pour l'instant le pas ne peut pas être choisis mais il pourra l'être plus tard)
NbrePointsX = 101 
x = np.linspace(0, longueur, NbrePointsX)
NbrePointsY = 41
y = np.linspace(0, hauteur, NbrePointsY)

# LES CALCULS :
# fonction que l'on pourra appeler qui s'occupe de calculer différentes données d'une poutre qui subit seulement une charge répartie
    
# (RACC, RBCR, EffortTranchCR, MfCR, ContrainteYMaxCR, ContrainteMaxCR, DefYMaxCR, DefMaxCR, flècheCR, FlècheMaxCR, \
# GrapheEffortTranchCR, GrapheMfCR, GrapheContrainteYMaxCR, GrapheDefYMaxCR, GrapheFlècheCR) = \
# Appuis_simples.charge_répartie(hauteur, longueur, Igz, E, LimElast, q, x) 
  
# (RACC, RBCC, EffortTranchCC, MfCC, ContrainteYMaxCC, ContrainteMaxCC, DefYMaxCC, DefMaxCC, flècheCC, FlècheMaxCC, \
# GrapheEffortTranchCC, GrapheMfCC, GrapheContrainteYMaxCC, GrapheDefYMaxCC, GrapheFlècheCC) = \
# Appuis_simples.charge_concentrée(hauteur, longueur, Igz, E, LimElast, P, x, NbrePointsX, a, b)

# (RACCE, EffortTranchCCE, MfCCE, ContrainteYMaxCCE, ContrainteMaxCCE, DefYMaxCCE, DefMaxCCE, flècheCCE, FlècheMaxCCE) = \
# Liaison_encastrement.charge_concentrée(hauteur, longueur, Igz, E, LimElast, P, x, NbrePointsX, a, b)

(RA, EffortTranch, Mf, ContrainteYMax, ContrainteMax, DefYMax, DefMax, flèche, FlècheMax) = \
Liaison_encastrement.charge_répartie(hauteur, longueur, Igz, E, LimElast, q, x)

#Liaison_encastrement.charge_croissante(hauteur, longueur, Igz, E, LimElast, q, x)
    
#Liaison_encastrement.charge_décroissante(hauteur, longueur, Igz, E, LimElast, q, x)

# (RA, RB, EffortTranch, Mf, ContrainteYMax, ContrainteMax, DefYMax, DefMax, flèche, FlècheMax)\
# = Appuis_simples.charge_répartie_partielle(hauteur, longueur, Igz, E, LimElast, q, x, NbrePointsX, a, b, c)

# Appuis_simples.charge_répartie_partielle_proche(hauteur, longueur, Igz, E, LimElast, q, x, NbrePointsX, a)

# Appuis_simples.charge_triangulaire(hauteur, longueur, Igz, E, LimElast, q, x, NbrePointsX, a, b)

# Appuis_simples.charge_triangulaire_monotone(hauteur, longueur, Igz, E, LimElast, q, x, NbrePointsX)

# Appuis_simples.charge_triangulaire_antisymétriqu(hauteur, longueur, Igz, E, LimElast, q, x, NbrePointsX)

# Appuis_simples.charge_trapézoïdale_symétrique(hauteur, longueur, Igz, E, LimElast, q, x, NbrePointsX, a, b)

# Appuis_simples.charge_parabolique(hauteur, longueur, Igz, E, LimElast, q, x, NbrePointsX)
#