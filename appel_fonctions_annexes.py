# -*- coding: utf-8 -*-
"""
@author: Forjot Henri

Création de fonctions annexes
"""
### IMPORTATIONS ###
from tkinter import *
import tkinter.filedialog
from tkinter.messagebox import *
import sys
import os

#Définition du visuel
font_titre1 = ("Arial", 45, "bold")
font_titre2 = ("Arial", 14, "bold italic")
font_texte1 = ("Arial", 8, "bold")
gris_clair='#EDEDED'
gris_fonce='#9B9B9B'

def donothing(): # Pour eviter les bugs, fonctions qui dit que rien n'est encore codé quand on sélectionne un élts non codés
    nouvelle_fenetre =Tk()
    boutton = Button(nouvelle_fenetre, text="Ne fait rien pour le moment \n A venir très prochainement !")
    boutton.pack(side='top')  
    nouvelle_fenetre.mainloop()

def fenetre_bienvenue(): #Création d'une fenetre de bienvenue    
    bienvenue = Tk() #création de la fenetre bienvenue
    bienvenue.title("RDM6+++ --- BIENVENUE") #Titre de l'encadré
    bienvenue.config(bg=gris_clair)
    bienvenue.resizable(width=FALSE, height=FALSE)
    bienvenue_message1=Label(bienvenue,fg="red",font=font_titre2,text='Bienvenue sur RDM6+++ qui casse la barraque',width=50, height=2,bg=gris_clair) #définit le message 1
    bienvenue_message1.pack() # affiche le message 1
    bienvenue_message2=Label(bienvenue,font=font_texte1,text='Ce programme à pour intérêt d\'étudier l\'efffet que peut avoir une charge sur une poutre.',wraplength=300,bg=gris_clair) #définit le message 2
    bienvenue_message2.pack() # affiche le message 2
    bouton_continuer = Button(bienvenue, text="Entrer",borderwidth=6,activebackground=gris_clair,relief="raised",overrelief="groove",command=bienvenue.destroy)
    bouton_continuer.pack(anchor='se')
    bienvenue.mainloop()

def reboot_programme(): #relance le programme de zéro
    python = sys.executable
    os.execl(python, python, * sys.argv)

def error(): #affiche une fenêtre pour les erreurs
    showerror(title='ERREUR !!!',message='Argument non valable... Veuillez recommencer !')
    
def ouvrir():
    # S'il n'est pas du bon genre, renvoie une erreur
    # if IOError: 
    #     error()
    # else:
    o=tkinter.filedialog.askopenfilename(title="Ouvrir un fichier csv RDM6+++",filetypes=[("Fichier Text","*.csv")])
    print(o)
        
    # reboot_programme()
    # fh = open('name_of_a_file', "r") 
    # some_data = fh.read() 
    # fh.close() 
    #     
    
def sauvegarder(): # Extention de sauvegarder sous
    #Il faut lire si je fichier existe déjà
    if e_s != None: #le fichier existe pas
        return sauvegarder_sous()
    else: #le fichier existe, il faut juste le modifier
        text2save = str(0,1,2) # fichier à sauvegarder... ATENTION  forcément un str
        e_s.write(text2save) # on ouvre et on stock
        e_s.close() # on referme
    
def sauvegarder_sous(): # sauvegarder les données crééent par le calcul
    # si le fichier existe déjà, cela vaut dire qu'on veut changer de répertoire ou le renommer donc on fait rien
    e_s=tkinter.filedialog.asksaveasfile(title="Enregistrer sous",filetypes=[("Fichier Text","*.csv")]) # ouvre la fenêtre pour enregistrer
    text2save = str(0,1,2) # fichier à sauvegarder... ATENTION  forcément un str
    e_s.write(text2save) # on ouvre et on stock
    e_s.close() # on referme
    return print(e_s),e_s

def switch_elts_finis(): # fonction qui renvoie sur le programme d'élts finis
    donothing()

def import_elts_finis(): # fonction qui import des données de géometrie,chargement,matériau du programme d'élts finis vers celui de rdm
    donothing()
    
def export_elts_finis(): # fonction qui import des données de géometrie,chargement,matériau du programme de rdm vers celui d'élts finis
    donothing()
    
def aide(): # fourni les liens URLs de la plateforme d'aide en ligne, du pdf et de la page youtube
    donothing()
    
def ctds_de_fct(): # annonce les conditions dans lequels le programme renvois des valeurs "exactes"
    donothing()
    
def credit(): # annonce la version du programme, les concepteurs du programme et l'année de développement
    donothing()
    