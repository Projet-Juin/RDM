# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:25:43 2020

@author: Forjot Henri
"""

from tkinter import *
import main

#Définition du visuel
font_titre1 = ("Arial", 45, "bold")
font_titre2 = ("Arial", 14, "bold italic")
font_texte1 = ("Arial", 8, "bold")
gris_clair='#EDEDED'
gris_fonce='#9B9B9B'


"""
création d'une fenetre de bienvenue
"""
bienvenue = Tk() #création de la fenetre bienvenue
bienvenue.title("RDM6+++ --- BIENVENUE") #Titre de l'encadré
bienvenue.config(bg=gris_clair)
bienvenue.resizable(width=FALSE, height=FALSE)
bienvenue_message1=Label(bienvenue,fg="red",font=font_titre2,text='Bienvenue sur RDM6+++ qui casse la barraque',width=50, height=2,bg=gris_clair) #définit le message 1
bienvenue_message1.pack() # affiche le message 1
bienvenue_message2=Label(bienvenue,font=font_texte1,text='Ce programme à pour intérêt d\'étudier l\'efffet que peut avoir une charge sur une poutre.',wraplength=300,bg=gris_clair) #définit le message 2
bienvenue_message2.pack() # affiche le message 2
#Création d'un bouton pour entrer dans le programme
def detruire_la_fenetre():
    global bienvenue
    bienvenue.destroy()
    main()
bouton_continuer = Button(bienvenue, text="Entrer",borderwidth=6,activebackground=gris_clair,relief="groove",command=detruire_la_fenetre)
bouton_continuer.pack(anchor='se')
bienvenue.mainloop()
