# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 12:51:09 2020

@author: Clara
"""
import classe 
import géométrie_poutre
import numpy as np

P = -200
a = 600
hauteur = 10
longueur = 1200
largeur = 20
E = 210000
MasseVol = 0.75
LimElast = 40
(Masse, Igz) = géométrie_poutre.géométrie_poutre(hauteur, longueur, largeur, MasseVol)
NbrePointsX = 101
x = np.linspace(0, longueur, NbrePointsX)

tabl_c_concentrée = []
VarEcrase = classe.charge_concentrée(P, a)
tabl_c_concentrée.append(VarEcrase)  
VarEcrase1 = classe.charge_concentrée(P, a)
tabl_c_concentrée.append(VarEcrase1)  
VarEcrase1 = classe.charge_concentrée(P, a)
tabl_c_concentrée.append(VarEcrase1)  
somme = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

dernierj = classe.charge_concentrée.nbr
# for j in range(dernierj) :
#     [RAt, RBt, EffortTrancht, Mft, ContrainteYMaxt, ContrainteMaxt, DefYMaxt, DefMaxt, flèchet, FlècheMaxt] = tabl_c_concentrée[j].charge_concentrée_appuis_simples(hauteur, longueur, Igz, E, x, NbrePointsX)
#     RA += RAt
#     RB += RBt
#     ContrainteMax += ContrainteMaxt
#     DefMax += DefMaxt
#     FlècheMax += FlècheMaxt

for j in range(classe.charge_concentrée.nbr) :
    print(j)
    [RAt, RBt, EffortTrancht, Mft, ContrainteYMaxt, ContrainteMaxt, DefYMaxt, DefMaxt, flèchet, FlècheMaxt] = tabl_c_concentrée[j].charge_concentrée_appuis_simples(hauteur, longueur, Igz, E, x, NbrePointsX)
    conversion = np.array([RAt, RBt, EffortTrancht, Mft, ContrainteYMaxt, ContrainteMaxt, DefYMaxt, DefMaxt, flèchet, FlècheMaxt])
    somme = somme + conversion


print("RA = ", RAt, "RB = ", RBt, "ContrainteMax = ", ContrainteMaxt, "DefMax = ", DefMaxt, "FlècheMax = ", FlècheMaxt)
print("RA = ", somme[0], "RB = ", somme[1], "ContrainteMax = ", somme[5], "DefMax = ", somme[7], "FlècheMax = ", somme[9])