# -*- coding: utf-8 -*-
"""
@author: Forjot Henri

Création de fonctions annexes
"""

from tkinter import *
import tkinter.filedialog
import sys
import os

#Définition du visuel
font_titre1 = ("Arial", 45, "bold")
font_titre2 = ("Arial", 14, "bold italic")
font_texte1 = ("Arial", 8, "bold")
gris_clair='#EDEDED'
gris_fonce='#9B9B9B'

def donothing():
    nouvelle_fenetre =Tk()
    boutton = Button(nouvelle_fenetre, text="Ne fait rien pour le moment")
    boutton.pack(side='top')  
    nouvelle_fenetre.mainloop()

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
    bouton_continuer = Button(bienvenue, text="Entrer",borderwidth=6,activebackground=gris_clair,relief="raised",overrelief="groove",command=bienvenue.destroy)
    bouton_continuer.pack(anchor='se')
    bienvenue.mainloop()

def reboot_programme():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def error():
    error_fenetre=Tk()
    error_fenetre.title('ERREUR')  
    # logo = BitmapImage('error.xbm', foreground='red')
    # Label(image=logo).grid()
    msg=Label(error_fenetre,text='Argument non valable... Veuillez recommencer !',borderwidth=1,font=font_titre2)
    msg_bis=Label(error_fenetre,bitmap='error',fg='red',borderwidth=1,font=("Arial", 30, "bold"))
    msg_bis2=Label(error_fenetre,bitmap='error',fg='red',borderwidth=1,font=("Arial", 30, "bold"))
    msg.grid(column=1)
    msg_bis.grid(column=0,sticky='w')
    msg_bis2.grid(column=2,sticky='e')
    error_fenetre.mainloop()
    
def ouvrir():
    # S'il n'est pas du bon genre, renvoie une erreur
    # if IOError: 
    #     error()
    # else:
    o=tkinter.filedialog.askopenfilename(title="Ouvrir un fichier csv RDM6+++",filetypes=[('.txt')],defaultextension=".txt")
    print(o)
        
    # reboot_programme()
    # fh = open('name_of_a_file', "r") 
    # some_data = fh.read() 
    # fh.close() 
    #     
    
def sauvegarder():
    #Il faut lire si je fichier existe déjà
    if e_s != None: #le fichier existe pas
        return sauvegarder_sous()
    else: #le fichier existe, il faut juste le modifier
        text2save = str(0,1,2) # fichier à sauvegarder... ATENTION  forcément un str
        e_s.write(text2save) # on ouvre et on stock
        e_s.close() # on referme
    
def sauvegarder_sous():
    # si le fichier existe déjà, cela vaut dire qu'on veut changer de répertoire ou le renommer donc on fait rien
    e_s=tkinter.filedialog.asksaveasfile(title="Enregistrer sous",filetypes=[('.txt')],defaultextension=".txt") # ouvre la fenêtre pour enregistrer
    text2save = str(0,1,2) # fichier à sauvegarder... ATENTION  forcément un str
    e_s.write(text2save) # on ouvre et on stock
    e_s.close() # on referme
    return print(e_s),e_s

    
