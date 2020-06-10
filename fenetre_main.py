# -*- coding: utf-8 -*-
"""
@author: Forjot Henri

Création du main

"""

from tkinter import *
from appel_fonctions_annexes import *
# import appel_fonctions

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
### Fenetre de bienvenue ###
fenetre_bienvenue()

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
fichier_menu = Menu(barre_de_menu) # Création d'un menu fichier
fichier_menu.add_command(label='Sauvegarder            (Ctrl+S)') # ajout de l'item redémarrer
fichier_menu.add_command(label='Sauvegarder Sous   (Shift+Ctrl+S)') # ajout de l'item quitter
fichier_menu.add_separator() #ajout d'un separateur
fichier_menu.add_command(label='Redémarrer',command=reboot_programme()) # ajout de l'item redémarrer
fichier_menu.add_command(label='Quitter',command=quitter_main) # ajout de l'item quitter
# Création d'un menu autres et ajout d'items
autres_menu = Menu(barre_de_menu) # Création d'un menu autres
autres_menu.add_command(label='Aide') # ajout de l'item aide
autres_menu.add_separator() #ajout d'un separateur
autres_menu.add_command(label='Crédit') # ajout de l'item crédit
#Ajouts des barres de menus
barre_de_menu.add_cascade(label='Fichier', menu=fichier_menu) # ajouter de fichier_menu dans barre_de_menu
barre_de_menu.add_cascade(label='Autres', menu=autres_menu) # ajouter de autres_menu dans barre_de_menu
"""
Fin
"""

### Création de 3 frames principales ###
#encadré haut
top_frame= Frame(main, bg="red", width=1920, height=50)
#encadré bas
down_frame=Frame(main, bg="yellow", width=1920, height=1030)
#encadré gauche
left_frame= Frame(down_frame, bg="blue", width=400, height=1030)
#encadré droite
right_frame = Frame(down_frame, bg='green', width =1520, height=1030)
#Gestion sur une grille des 4 frames principales
top_frame.grid(row=0,column=0,columnspan=5)
down_frame.grid()
left_frame.grid(row=0, column=0)
right_frame.grid(row=0,column=1,columnspan=4)
"""
Fin
"""

### top_frame ###


"""
Fin
"""

### left_frame ###
### frame_géométrie ###
frame_geometrie=LabelFrame(left_frame,labelanchor='nw',bg=gris_tres_fonce,bd=5,cursor='arrow', padx=10, pady=10)
frame_geometrie.grid(column=0,row=0)
### frame_matériau ###
frame_matériau=LabelFrame(left_frame,labelanchor='nw',bg=gris_tres_fonce,bd=5,cursor='arrow', padx=10, pady=10)
frame_matériau.grid(column=0,row=1)
### frame_chargement ###
frame_chargement=LabelFrame(left_frame,labelanchor='nw',bg=gris_tres_fonce,bd=5,cursor='arrow', padx=10, pady=10)
frame_chargement.grid(column=0,row=2)
### Bouton Calculer ###
bouton_calculer= Button(left_frame, text="Calculer",textvariable="Re-Calculer",relief="raised",overrelief="groove", font=("Tahoma", 20,"bold"), bg=gris_tres_fonce, fg ="white")
# , command=
bouton_calculer.grid(column=0,row=3)
"""
Fin
"""

### right frame ###

"""
Fin
"""

### Lancement du rendu général ###
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
