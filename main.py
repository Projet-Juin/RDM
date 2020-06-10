# -*- coding: utf-8 -*-
"""
@author: Forjot Henri

Création du main

"""
### IMPORTATIONS ###
from tkinter import *
from appel_fonctions_annexes import *
#from gestion_des_entrées import *
from gestion_des_calculs import *

### Définition du visuel ###
font_titre1 = ("Arial", 45, "bold")
font_titre2 = ("Arial", 14, "bold italic")
font_texte1 = ("Arial", 8, "bold")
gris_clair='#EDEDED'
gris_fonce='#9B9B9B'
gris_tres_fonce='#7E7E7E'
"""
Fin
"""


### Création fenetre principale ###
main=Tk()
main.title("RDM6+++ --- Écran principal") #Titre de l'encadré
main.config(bg=gris_clair)
width = main.winfo_screenwidth()  #obtient la taille de l'écran de l'utilisateur en largeur
height = main.winfo_screenheight()  #obtient la taille de l'écran de l'utilisateur en hauteur
main.geometry("%dx%d" % (width, height)) 
# main.resizable(width=FALSE, height=FALSE) #empêche de déformer la fenetre
"""
Fin
"""

### Creation d'une Barre de menu ###
barre_de_menu = Menu(main, tearoff=0)
main.config(menu=barre_de_menu)
# Création d'un menu fichier et ajout d'items
fichier_menu = Menu(barre_de_menu,activebackground=gris_clair) # Création d'un menu fichier
fichier_menu.add_command(label='Ouvrir',command=ouvrir) # ajout de l'item ouvrir
fichier_menu.add_command(label='Sauvegarder            (Ctrl+S)',command=sauvegarder) # ajout de l'item sauvegarder
fichier_menu.add_command(label='Sauvegarder Sous   (Shift+Ctrl+S)',command=sauvegarder_sous) # ajout de l'item sauvegarder sous
fichier_menu.add_command(label='Redémarrer',command=reboot_programme) # ajout de l'item redémarrer
fichier_menu.add_separator() #ajout d'un separateur
fichier_menu.add_command(label='Quitter',command=main.destroy) # ajout de l'item quitter
# Création d'un menu éléments finis et ajout d'items
elts_finis_menu = Menu(barre_de_menu,activebackground=gris_clair) # Création d'un menu élts finis
elts_finis_menu.add_command(label='Switch vers Éléments finis',command=switch_elts_finis) # ajout de l'item permettant d'aller en élément finis
elts_finis_menu.add_separator() #ajout d'un separateur
elts_finis_menu.add_command(label='Importer les Inputs d\'Éléments finis',command=import_elts_finis) # ajout de l'item permettant d'importer les données d'éléments finis
elts_finis_menu.add_command(label='Exporter les Inputs d\'Éléments finis',command=export_elts_finis) # ajout de l'item permettant d'exporter les données d'éléments finis
# Création d'un menu autres et ajout d'items
autres_menu = Menu(barre_de_menu,activebackground=gris_clair) # Création d'un menu autres
autres_menu.add_command(label='Aide',command=aide) # ajout de l'item aide
autres_menu.add_command(label='Conditions de fonctionnement',command=ctds_de_fct) # ajout de l'item conditions de la rdm
autres_menu.add_separator() #ajout d'un separateur
autres_menu.add_command(label='Crédit',command=credit) # ajout de l'item crédit
#Ajouts des barres de menus
barre_de_menu.add_cascade(label='Fichier', menu=fichier_menu,command=donothing) # ajouter de fichier_menu dans barre_de_menu
barre_de_menu.add_cascade(label='Éléments finis', menu=elts_finis_menu,command=donothing) # ajouter de elts_finis_menu dans barre_de_menu
barre_de_menu.add_cascade(label='Autres', menu=autres_menu,command=donothing) # ajouter de autres_menu dans barre_de_menu
"""
Fin
"""

### Création de 2 frames principales ###
#encadré gauche
left_frame= Frame(main, bg="blue", width=400, height=1080)
#encadré droite
right_frame = Frame(main, bg='green', width =1520, height=1080)
#paramètres de grille et Gestion sur une grille des 2 frames principales
main.columnconfigure(0,weight=1)
main.columnconfigure(1,weight=4)
left_frame.grid(row=0,column=0,in_=main)
right_frame.grid(row=0,column=1,in_=main)
"""
Fin
"""

### left_frame ###
### frame_géométrie ###
frame_geometrie=LabelFrame(left_frame,labelanchor='nw',bg=gris_tres_fonce,bd=5,cursor='arrow', padx=1, pady=1,width=350,height=150).grid(column=0,row=0,in_=left_frame)
### frame_matériau ###
frame_materiau=LabelFrame(left_frame,labelanchor='nw',bg=gris_tres_fonce,bd=5,cursor='arrow', padx=1, pady=1,width=350,height=150).grid(column=0,row=1,in_=left_frame)
### frame_chargement ###
frame_chargement=LabelFrame(left_frame,labelanchor='nw',bg=gris_tres_fonce,bd=5,cursor='arrow', padx=1, pady=1,width=350,height=150).grid(column=0,row=2,in_=left_frame)
#paramètres de grille left_frame
# left_frame.rowconfigure(0,weight=2)
# left_frame.rowconfigure(1,weight=2)
# left_frame.rowconfigure(2,weight=2)
# left_frame.rowconfigure(3,weight=1)


### Bouton Calculer ###
# bouton_calculer= Button(left_frame, text="Calculer",textvariable="Re-Calculer",relief="raised",overrelief="groove", font=("Tahoma", 20,"bold"), bg=gris_tres_fonce, fg ="white", command=calcul)
# bouton_calculer.grid(column=0,row=3)
"""
Fin
"""

### right frame ###

"""
Fin
"""



### Lancement du rendu général ###
# Fenetre de bienvenue #
#fenetre_bienvenue()
#lancer le main
main.mainloop()
"""
Fin
"""




#contenu top_frame
# top_frame_message1=Label(top_frame,text='top',anchor=W,bg=gris_clair) #définit le message 1

# #contenu left_frame
# left_frame_message1=Label(left_frame,text='left',width=50, height=2,bg=gris_clair) #définit le message 2

# #contenu right_frame
# right_frame_message1=Label(right_frame,text='right',width=50, height=2,bg=gris_clair) #définit le message 3
