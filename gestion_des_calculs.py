# -*- coding: utf-8 -*-
"""
@author: Forjot Henri

Gestion des calculs
"""
### IMPORTATIONS ###
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from appel_fonctions_annexes import *


# def verification_hypotheses_de_la_rdm_section_rectangulaire(L,b): # sous programme de calcul qui renvoi TRUE si les conditions de la rdm sont respectué, sinon FALSE
#     #Vérifie le rapport de x4 pour la géométrie
#     if L/b<=4:
#         showwarning(title="ATTENTION", message="Le calcul va se faire mais les conditions de la RDM ne sont pas respectés \n Pour plus d'informations, rendez vous dans la rubrique Autres / Conditions de fonctionnement")
#         hypotheses_verif=False
#     else:
#         hypotheses_verif=True
#     return hyptohes_verif

def calcul(): # Effectue le calcul sur le bouton calcul
    donothing() #pour le moment, fait rien
    # update()
    # ttk.Progressbar()
    #  valeurs_geometriques=(L,b,b1,b2,h,h1,R,R1,D1,D2) # liste des entrées géométriques
    # E , m , Mv , Re et nu libre dans le programme
    # liste_charges --> liste des charges de la forme [[0 si appui ou 1 si encastrement,"commentaire sur le type de chargement" ,[p,q,a1,c1,I,M]]]
