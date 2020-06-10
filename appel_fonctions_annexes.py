# -*- coding: utf-8 -*-
"""
@author: Forjot Henri

Création de fonctions annexes
"""

from tkinter import *
import sys
import os

#Définition du visuel
font_titre1 = ("Arial", 45, "bold")
font_titre2 = ("Arial", 14, "bold italic")
font_texte1 = ("Arial", 8, "bold")
gris_clair='#EDEDED'
gris_fonce='#9B9B9B'

"""
Création d'une fenetre de bienvenue
"""
def fenetre_bienvenue():    
    bienvenue = Tk() #création de la fenetre bienvenue
    bienvenue.title("RDM6+++ --- BIENVENUE") #Titre de l'encadré
    bienvenue.config(bg=gris_clair)
    bienvenue.resizable(width=FALSE, height=FALSE)
    bienvenue_message1=Label(bienvenue,fg="red",font=font_titre2,text='Bienvenue sur RDM6+++ qui casse la barraque',width=50, height=2,bg=gris_clair) #définit le message 1
    bienvenue_message1.pack() # affiche le message 1
    bienvenue_message2=Label(bienvenue,font=font_texte1,text='Ce programme à pour intérêt d\'étudier l\'efffet que peut avoir une charge sur une poutre.',wraplength=300,bg=gris_clair) #définit le message 2
    bienvenue_message2.pack() # affiche le message 2
    bouton_continuer = Button(bienvenue, text="Entrer",borderwidth=6,activebackground=gris_clair,relief="raised",overrelief="groove",command=quitter_bienvenue)
    bouton_continuer.pack(anchor='se')
    bienvenue.mainloop()

# Quitter une interface graphique correctement 
def quitter_bienvenue() :
    bienvenue.destroy()
def quitter_main() :
    fenetre.destroy()

def reboot_programme():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

