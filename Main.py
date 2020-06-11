# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:12:41 2020
@author: Simon
"""
import numpy as np
import matplotlib.pyplot as plt
import Appuis_simples
import Liaison_encastrement
import géométrie_poutre

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

(Masse, Igz) = géométrie_poutre.géométrie_poutre(hauteur, longueur, largeur, MasseVol)

    # Forces appliquées
q = float(input('Entrer la Force linéique de la charge répartie en N/mm :')) 
P = float(input('Entrer la Force exercée par la charge concentrée en N/mm :'))
if P != 0:
    a = float(input('Entrer la position de la charge concentrée sur l\'axe des x en mm :'))
    b = longueur - a

    # Discrétisations (pour l'instant le pas ne peut pas être choisis mais il pourra l'être plus tard)
NbrePointsX = 101 # réfléchir au nom
x = np.linspace(0, longueur, NbrePointsX)
print(x)

# LES CALCULS :
# fonction que l'on pourra appeler qui s'occupe de calculer différentes données d'une poutre qui subit seulement une charge répartie

(RACC, RBCR, EffortTranchCR, MfCR, ContrainteYMaxCR, ContrainteMaxCR, DefYMaxCR, DefMaxCR, flècheCR, FlècheMaxCR, \
GrapheEffortTranchCR, GrapheMfCR, GrapheContrainteYMaxCR, GrapheDefYMaxCR, GrapheFlècheCR) = \
Appuis_simples.charge_répartie(hauteur, longueur, Igz, E, LimElast, q, x) 
  
(RACC, RBCC, EffortTranchCC, MfCC, ContrainteYMaxCC, ContrainteMaxCC, DefYMaxCC, DefMaxCC, flècheCC, FlècheMaxCC, \
GrapheEffortTranchCC, GrapheMfCC, GrapheContrainteYMaxCC, GrapheDefYMaxCC, GrapheFlècheCC) = \
Appuis_simples.charge_concentrée(hauteur, longueur, Igz, E, LimElast, P, x, NbrePointsX, a, b)

(RACCE, EffortTranchCCE, MfCCE, ContrainteYMaxCCE, ContrainteMaxCCE, DefYMaxCCE, DefMaxCCE, flècheCCE, FlècheMaxCCE) = \
Liaison_encastrement.charge_concentrée(hauteur, longueur, Igz, E, LimElast, P, x, NbrePointsX, a, b)

(RA, EffortTranch, Mf, ContrainteYMax, ContrainteMax, DefYMax, DefMax, flèche, FlècheMax) = \
Liaison_encastrement.charge_répartie(hauteur, longueur, Igz, E, LimElast, q, x)

