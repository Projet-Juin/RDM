# -*- coding: utf-8 -*-
"""
@author: Forjot Henri

Création du main

"""

from tkinter import *
from fenetre_bienvenue import fenetre_bienvenue
import appel_fonctions

#Définition du visuel
font_titre1 = ("Arial", 45, "bold")
font_titre2 = ("Arial", 14, "bold italic")
font_texte1 = ("Arial", 8, "bold")
gris_clair='#EDEDED'
gris_fonce='#9B9B9B'




### Création fenetre principale ###

main=Tk()
main.title("RDM6+++ --- Écran principal") #Titre de l'encadré
main.config(bg=gris_clair)
width = main.winfo_screenwidth()  #obtient la taille de l'écran de l'utilisateur en largeur
height = main.winfo_screenheight()  #obtient la taille de l'écran de l'utilisateur en hauteur
main.geometry("%dx%d" % (width, height)) 
# main.resizable(width=FALSE, height=FALSE) #empêche de déformer la fenetre

### Création de 3 frames principales ###

#encadré haut
top_frame= Frame(main, bg="red", width=1920, height=50)
#encadré gauche
left_frame= Frame(main, bg="green", width=400, height=1030)
#encadré droite
right_frame = Frame(main, bg='cyan', width =1520, height=1030)
#Gestion sur une grille des 3 frames principales
top_frame.grid(row=0,column=0,columnspan=5)
left_frame.grid(row=1, column=0,columnspan=1)
right_frame.grid(row=1, column=1,columnspan=4)


### Lancement du rendu général ###

#lancer le main
main.mainloop()
#import le bienvenue
fenetre_bienvenue()#contenu top_frame




# top_frame_message1=Label(top_frame,text='top',anchor=W,bg=gris_clair) #définit le message 1

# #contenu left_frame
# left_frame_message1=Label(left_frame,text='left',width=50, height=2,bg=gris_clair) #définit le message 2

# #contenu right_frame
# right_frame_message1=Label(right_frame,text='right',width=50, height=2,bg=gris_clair) #définit le message 3
