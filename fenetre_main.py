# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:38:00 2020

@author: Forjot Henri
"""

from tkinter import *

font_titre1 = ("Arial", 45, "bold")
font_titre2 = ("Arial", 14, "bold italic")
font_texte1 = ("Arial", 8, "bold")

gris_clair='#EDEDED'
gris_fonce='#9B9B9B'


"""
Création du main
"""
def main():
    #fenetre principale
    main=Tk()
    main.title("RDM6+++ --- Écran principal") #Titre de l'encadré
    main.config(bg=gris_clair)
    width = main.winfo_screenwidth() 
    height = main.winfo_screenheight() 
    main.geometry("%dx%d" % (width, height)) 
    main.resizable(width=FALSE, height=FALSE)
    
    #encadré haut
    top_frame= Frame(main, bg="red", width=1920, height=50)
    
    #encadré gauche
    left_frame= Frame(main, bg="green", width=400, height=1030)
    
    #encadré droite
    right_frame = Frame(main, bg='cyan', width =1520, height=1030)



    #contenu top_frame
    top_frame_message1=Label(top_frame,text='top',anchor=W,bg=gris_clair) #définit le message 1
    
    #contenu left_frame
    left_frame_message1=Label(left_frame,text='left',width=50, height=2,bg=gris_clair) #définit le message 2
    
    #contenu right_frame
    right_frame_message1=Label(right_frame,text='right',width=50, height=2,bg=gris_clair) #définit le message 3


    top_frame.grid(row=0,column=0,columnspan=5)
    left_frame.grid(row=1, column=0,columnspan=1)
    right_frame.grid(row=1, column=1,columnspan=4)
    main.mainloop()
