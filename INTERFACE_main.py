# -*- coding: utf-8 -*-
"""
@author: Forjot Henri

Création du main

"""
### IMPORTATIONS INTERFACE ###
# Import Biblio
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
# Import feuilles .py
from INTERFACE_Annexe_1 import *

### IMPORTATIONS CALCULS ###
# Import Biblio
import numpy as np
import matplotlib.pyplot as plt
import math
# Import feuilles .py
import Appuis_simples
import Liaison_encastrement
import géométrie_poutre
import classe 

### Définition du visuel ###
font_titre1 = ("Arial", 45, "bold")
font_titre2 = ("Arial", 14, "bold italic")
font_texte1 = ("Arial", 8, "bold")
gris_1_bis='#EAECEE'
gris_1='#D5D8DC'
gris_2='#ABB2B9'
gris_3='#85929E'
gris_4='#808B96'
gris_5='#5D6D7E'
gris_6='#566573'
gris_7='#34495E'
"""
Fin
"""

### Création fenetre principale ###
main=Tk()
main.title("RDM6+++ --- Écran principal") #Titre de l'encadré
main.config(bg=gris_7)
width = main.winfo_screenwidth()  #obtient la taille de l'écran de l'utilisateur en largeur
height = main.winfo_screenheight()  #obtient la taille de l'écran de l'utilisateur en hauteur
main.geometry("%dx%d" % (width,height))
# main.resizable(width=FALSE, height=FALSE) #empêche de déformer la fenetre
"""
Fin
"""

### Creation d'une Barre de menu ###
barre_de_menu = Menu(main, tearoff=0)
main.config(menu=barre_de_menu)
# Création d'un menu fichier et ajout d'items
fichier_menu = Menu(barre_de_menu,activebackground=gris_5, tearoff=0) # Création d'un menu fichier
fichier_menu.add_command(label='Ouvrir',command=ouvrir) # ajout de l'item ouvrir
fichier_menu.add_command(label='Sauvegarder            (Ctrl+S)',command=sauvegarder) # ajout de l'item sauvegarder
fichier_menu.add_command(label='Sauvegarder Sous   (Shift+Ctrl+S)',command=sauvegarder_sous) # ajout de l'item sauvegarder sous
fichier_menu.add_command(label='Redémarrer',command=reboot_programme) # ajout de l'item redémarrer
fichier_menu.add_separator() #ajout d'un separateur
fichier_menu.add_command(label='Quitter',command=main.destroy) # ajout de l'item quitter (ou sys.exit)
# Création d'un menu éléments finis et ajout d'items
elts_finis_menu = Menu(barre_de_menu,activebackground=gris_5, tearoff=0) # Création d'un menu élts finis
elts_finis_menu.add_command(label='Switch vers Éléments finis',command=switch_elts_finis) # ajout de l'item permettant d'aller en élément finis
elts_finis_menu.add_separator() #ajout d'un separateur
elts_finis_menu.add_command(label='Importer les Inputs d\'Éléments finis',command=import_elts_finis) # ajout de l'item permettant d'importer les données d'éléments finis
elts_finis_menu.add_command(label='Exporter les Inputs d\'Éléments finis',command=export_elts_finis) # ajout de l'item permettant d'exporter les données d'éléments finis
# Création d'un menu autres et ajout d'items
autres_menu = Menu(barre_de_menu,activebackground=gris_5, tearoff=0) # Création d'un menu autres
autres_menu.add_command(label='Aide',command=aide) # ajout de l'item aide
autres_menu.add_command(label='Conditions de fonctionnement',command=ctds_de_fct) # ajout de l'item conditions de la rdm
autres_menu.add_separator() #ajout d'un separateur
autres_menu.add_command(label='Crédit',command=credit) # ajout de l'item crédit
# Ajouts des barres de menus
barre_de_menu.add_cascade(label='Fichier', menu=fichier_menu,command=donothing) # ajouter de fichier_menu dans barre_de_menu
barre_de_menu.add_cascade(label='Éléments finis', menu=elts_finis_menu,command=donothing) # ajouter de elts_finis_menu dans barre_de_menu
barre_de_menu.add_cascade(label='Autres', menu=autres_menu,command=donothing) # ajouter de autres_menu dans barre_de_menu
"""
Fin
"""

### Notebook Style ###
noteStyler = ttk.Style()
noteStyler.configure("TNotebook", background=gris_7, borderwidth=0)
noteStyler.configure("TNotebook.Tab", background=gris_7, foreground=gris_7, lightcolor=gris_7, borderwidth=0)
noteStyler.configure("TFrame", background=gris_7, foreground=gris_7, borderwidth=0)
"""
Fin
"""

### Importation des images nécessaires ###
img_geo_carre = PhotoImage(file='images/section carré.PNG')
img_geo_carre_t = PhotoImage(file='images/section carré troué.PNG')
img_geo_rectangle = PhotoImage(file='images/section rectangle.PNG')
img_geo_rectangle_t = PhotoImage(file='images/section rectangle troué.PNG')
img_geo_forme_i = PhotoImage(file='images/section forme i.PNG')
img_geo_forme_t = PhotoImage(file='images/section forme T.PNG')
img_geo_forme_l = PhotoImage(file='images/section forme L.PNG')
img_geo_forme_z = PhotoImage(file='images/section forme Z.PNG')
img_geo_forme_croix = PhotoImage(file='images/section forme croix.PNG')
img_geo_triangle_rec = PhotoImage(file='images/section triangle rectangle.PNG')
img_geo_cercle = PhotoImage(file='images/section cercle.PNG')
img_geo_cercle_t = PhotoImage(file='images/section cercle troué.PNG')
img_geo_demi_cercle = PhotoImage(file='images/section demi-cercle.PNG')
img_geo_quart_de_cercle = PhotoImage(file='images/section quart de cercle.PNG')
img_geo_ovale = PhotoImage(file='images/section ovale.PNG')
img_geo_losange = PhotoImage(file='images/section losange.PNG')
img_charge_con_app_simple = PhotoImage(file='images/charge concentrée appuis simples.PNG')
img_charge_con_encas = PhotoImage(file='images/charge concentrée encastrement.PNG')
img_charge_rep_app_simple = PhotoImage(file='images/charge répartie appuis simples.PNG')
img_charge_rep_encas = PhotoImage(file='images/charge répartie encastrement.PNG')
img_charge_rep_part = PhotoImage(file='images/charge partiellement répartie appuis simples.PNG')
img_charge_triang = PhotoImage(file='images/charge triangulaire appuis simples.PNG')
img_charge_triang_monotone = PhotoImage(file='images/charge triangulaire monotone appuis simples.PNG')
img_charge_triang_croiss = PhotoImage(file='images/charge triangulaire croissante encastrement.PNG')
img_charge_triang_décroiss = PhotoImage(file='images/charge triangulaire décroissante encastrement.PNG')
img_charge_triang_anti = PhotoImage(file='images/charge triangulaire antisymétrique appuis simples.PNG')
img_charge_trapèze = PhotoImage(file='images/charge trapézoïdale appuis simples.PNG')
img_charge_parabo = PhotoImage(file='images/charge parabolique appuis simples.PNG')
img_charge_moment_app_simple = PhotoImage(file='images/moment appuis simples.PNG')
img_charge_moment_encas = PhotoImage(file='images/moment encastrement.PNG')
img_charge_moment_unfi = PhotoImage(file='images/moment uniformément répartie appuis simples.PNG')
"""
Fin
"""

### Création de 2 frames principales ###
# Fenetre principale en 2 frames
left_frame= Frame(main, bg=gris_5) # encadré gauche
right_frame = Frame(main, bg=gris_5) #encadré droite
# left frame en 2 canvas
left_canvas1=Canvas(left_frame, bg=gris_5) # encadré gauche haut
left_canvas2=Canvas(left_frame, bg=gris_5) # encadré gauche bas
# placement sur la grille des deux 2 frames principales
left_frame.place(relx=0,rely=0, relwidth=0.25, relheight=1)
right_frame.place(relx=0.25,y=0, relwidth =0.75, relheight=1)
# placement des deux 2 canvas de left_frame
left_canvas1.place(relx=0,rely=0,relwidth=1, relheight=0.9)
left_canvas2.place(relx=0,rely=0.9,relwidth=1, relheight=0.1)
"""
Fin
"""

### NoteBook - left_canvas1 ###
notebook = ttk.Notebook(left_canvas1, style='TNotebook') # Creation du Notebook
#,height=900,width=500
notebook.enable_traversal() # permet de swtich avec le clavier d'un tab à l'autre [Ctl+tab,Ctrl+shift+tab,Alt+K]
notebook.pack(expand=1, fill='both') # on place le notebook
"""
Fin
"""

### Barre 1 : Géométrie ###
tab1 = ttk.Frame(notebook, style='TFrame') # Creation de la barre 1
# notebook.add(tab1, text='Géométrie') # Ajout de la barre 1 au notebook
img1 = PhotoImage(file='images/sphere.png')
notebook.add(tab1,text='Géométrie',image=img1, compound=LEFT) # Ajout de la barre 1 au notebook
canva_tab1 = Canvas(tab1, bg=gris_5)
canva_tab1.pack(expand=1, fill='both')
# Création labelframe 1
canva_tab1_labelframe1 = LabelFrame(canva_tab1,font = ("Arial",14 , "bold"),text = 'Type de section',bg =gris_5) #définit le message 1
canva_tab1_labelframe1.place(relx=0.01,rely=0.01,relwidth=0.98, relheight=0.12) # affiche le labelframe type de section    
# Choisir quelle est la géométrie du problème
canva_tab1_labelframe1_label = Label(canva_tab1_labelframe1,text = "Choissiez le type de géométrie de votre poutre :",bg=gris_5,font = ("Arial",10,"bold"))
canva_tab1_labelframe1_label.place(relx=0.01,rely=0.05,relwidth=0.98, relheight=0.30)
geometrie = StringVar()
canva_tab1_labelframe1_Combobox1 = ttk.Combobox(canva_tab1_labelframe1, textvariable = geometrie , state = "readonly",justify='center')
canva_tab1_labelframe1_Combobox1['values'] = ["","Rectangle", "Carré", "Forme", "Triangle", "Cercle", "Losange"]
canva_tab1_labelframe1_Combobox1.place(relx=0.01,rely=0.36,relwidth=0.98, relheight=0.30) # affichage de la combobox
canva_tab1_labelframe1_Combobox1.current(0) # onglet actif dans la combobox quand on démarre 
def ajout_combobox(event):
    global geometrie2,geometrie3,geometrie4,geometrie5,geometrie6,geometrie7,\
        canva_tab1_labelframe1_Combobox2,canva_tab1_labelframe1_Combobox3,canva_tab1_labelframe1_Combobox4,\
            canva_tab1_labelframe1_Combobox5,canva_tab1_labelframe1_Combobox6,canva_tab1_labelframe1_Combobox7
    print("Sélection en cours du Combobox 1 :  index <",canva_tab1_labelframe1_Combobox1.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox1.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
    if str(geometrie.get()) == 'Rectangle':
        geometrie2 = StringVar()
        canva_tab1_labelframe1_Combobox2 = ttk.Combobox(canva_tab1_labelframe1, textvariable = geometrie2 , state = "readonly",justify='center')
        canva_tab1_labelframe1_Combobox2['values'] = ["","Normal","Troué"]
        canva_tab1_labelframe1_Combobox2.place(relx=0.01,rely=0.67,relwidth=0.98, relheight=0.30) # affichage de la combobox
        canva_tab1_labelframe1_Combobox2.current(0) # onglet actif dans la combobox quand on démarre
        # Passage d'une combobox à l'autre   
        canva_tab1_labelframe1_Combobox2.bind("<<ComboboxSelected>>", nouveau_labelframe)
    if str(geometrie.get()) == 'Carré':
        geometrie3 = StringVar()
        canva_tab1_labelframe1_Combobox3 = ttk.Combobox(canva_tab1_labelframe1, textvariable = geometrie3 , state = "readonly",justify='center')
        canva_tab1_labelframe1_Combobox3['values'] = ["","Normal","Troué"]
        canva_tab1_labelframe1_Combobox3.place(relx=0.01,rely=0.67,relwidth=0.98, relheight=0.30) # affichage de la combobox
        canva_tab1_labelframe1_Combobox3.current(0) # onglet actif dans la combobox quand on démarre
        # Passage d'une combobox à l'autre   
        canva_tab1_labelframe1_Combobox3.bind("<<ComboboxSelected>>", nouveau_labelframe) 
    if str(geometrie.get()) == 'Forme':
        geometrie4 = StringVar()
        canva_tab1_labelframe1_Combobox4 = ttk.Combobox(canva_tab1_labelframe1, textvariable = geometrie4 , state = "readonly",justify='center')
        canva_tab1_labelframe1_Combobox4['values'] = ["","I","T","L","Z","Croix"]
        canva_tab1_labelframe1_Combobox4.place(relx=0.01,rely=0.67,relwidth=0.98, relheight=0.30) # affichage de la combobox
        canva_tab1_labelframe1_Combobox4.current(0) # onglet actif dans la combobox quand on démarre
        # Passage d'une combobox à l'autre   
        canva_tab1_labelframe1_Combobox4.bind("<<ComboboxSelected>>", nouveau_labelframe)
    if str(geometrie.get()) == 'Triangle':
        geometrie5 = StringVar()
        canva_tab1_labelframe1_Combobox5 = ttk.Combobox(canva_tab1_labelframe1, textvariable = geometrie5 , state = "readonly",justify='center')
        canva_tab1_labelframe1_Combobox5['values'] = ["","Rectangle"]
        canva_tab1_labelframe1_Combobox5.place(relx=0.01,rely=0.67,relwidth=0.98, relheight=0.30) # affichage de la combobox
        canva_tab1_labelframe1_Combobox5.current(0) # onglet actif dans la combobox quand on démarre
        # Passage d'une combobox à l'autre   
        canva_tab1_labelframe1_Combobox5.bind("<<ComboboxSelected>>", nouveau_labelframe)
    if str(geometrie.get()) == 'Cercle':
        geometrie6 = StringVar()
        canva_tab1_labelframe1_Combobox6 = ttk.Combobox(canva_tab1_labelframe1, textvariable = geometrie6 , state = "readonly",justify='center')
        canva_tab1_labelframe1_Combobox6['values'] = ["","Normal","Troué","Demi Cercle","Quart de Cercle","Ovale"]
        canva_tab1_labelframe1_Combobox6.place(relx=0.01,rely=0.67,relwidth=0.98, relheight=0.30) # affichage de la combobox
        canva_tab1_labelframe1_Combobox6.current(0) # onglet actif dans la combobox quand on démarre
        # Passage d'une combobox à l'autre   
        canva_tab1_labelframe1_Combobox6.bind("<<ComboboxSelected>>", nouveau_labelframe)
    if str(geometrie.get()) == 'Losange': 
        geometrie7 = StringVar()
        canva_tab1_labelframe1_Combobox7 = ttk.Combobox(canva_tab1_labelframe1, textvariable = geometrie7 , state = "readonly",justify='center')
        canva_tab1_labelframe1_Combobox7['values'] = ["","Normal"]
        canva_tab1_labelframe1_Combobox7.place(relx=0.01,rely=0.67,relwidth=0.98, relheight=0.30) # affichage de la combobox
        canva_tab1_labelframe1_Combobox7.current(0) # onglet actif dans la combobox quand on démarre
        # Passage d'une combobox à l'autre   
        canva_tab1_labelframe1_Combobox7.bind("<<ComboboxSelected>>", nouveau_labelframe)
def nouveau_labelframe(event): # nouvelle frame où on rentre les données
    global label_longueur,label_largeur,label_largeur1,label_largeur2,label_rayon,label_rayon1\
        ,label_hauteur,label_hauteur1,label_diagonale1,label_diagonale2\
            ,saisie_longueur,saisie_largeur, saisie_largeur1 , saisie_largeur2 ,saisie_rayon,saisie_rayon1\
                ,saisie_hauteur,saisie_hauteur1,saisie_diagonale1,saisie_diagonale2\
                    ,canva_tab1_labelframe2,valeurs_geometriques
    # Création labelframe 2
    canva_tab1_labelframe2 = LabelFrame(canva_tab1,font = ("Arial",14 , "bold"),text = 'Données',bg = gris_5) #définit le message 2
    canva_tab1_labelframe2.place(relx=0.01,rely=0.15,relwidth=0.98, relheight=0.44) # affiche le labelframe type de section   
    # Bouton pour valider l'entrée des données de géométrie pour rassurer l'utilisateur
    Button(canva_tab1_labelframe2,relief="raised",overrelief="groove", text='Valider la géométrie', font=("Tahoma", 14,"bold"), command=valider_la_géométrie, bg=gris_3,fg ="white").place(relx=0,rely=0.89,relwidth=1, relheight=0.10) # affiche le bouton valider  
    if str(geometrie.get()) == 'Rectangle':
        if str(geometrie2.get()) == 'Normal':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Longueur L de votre poutre en mm :',bg=gris_5)
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Largeur b de votre poutre en mm :',bg=gris_5)
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Hauteur h de votre poutre en mm :',bg=gris_5)
            # saisie des inputs L,b,h
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_largeur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_hauteur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            # Placement des items sur une grille
            label_longueur.pack(fill='both')
            saisie_longueur.pack(fill='both',pady=5)
            label_largeur.pack(fill='both')
            saisie_largeur.pack(fill='both',pady=5)
            label_hauteur.pack(fill='both')
            saisie_hauteur.pack(fill='both',pady=5)
            # saisie affichage de départ
            saisie_longueur.insert(0, "0.0")
            saisie_largeur.insert(0, "0.0") 
            saisie_hauteur.insert(0, "0.0") 
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_longueur.focus() 
            saisie_longueur.select_range(0,END)
            # main au dessus de la case
            saisie_longueur.config(cursor='hand1')
            saisie_largeur.config(cursor='hand1')
            saisie_hauteur.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_geo_rectangle)
            # lancement retour des touches
            saisie_longueur.bind('<Return>',largeur_next)
            saisie_largeur.bind('<Return>',hauteur_next)
            saisie_hauteur.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 2 :  index <",canva_tab1_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(geometrie2.get()) == 'Troué':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Longueur L de votre poutre en mm :',bg=gris_5)
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Largeur b de votre poutre en mm :',bg=gris_5)
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Hauteur h de votre poutre en mm :',bg=gris_5)
            label_largeur1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Largeur b1 de votre poutre en mm :',bg=gris_5)
            label_hauteur1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Hauteur h1 de votre poutre en mm :',bg=gris_5)
            # saisie des inputs L,b,h
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_largeur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_hauteur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_largeur1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_hauteur1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            # Placement des items sur une grille
            label_longueur.pack(fill='both')
            saisie_longueur.pack(fill='both',pady=5)
            label_largeur.pack(fill='both')
            saisie_largeur.pack(fill='both',pady=5)
            label_hauteur.pack(fill='both')
            saisie_hauteur.pack(fill='both',pady=5)
            label_largeur1.pack(fill='both')
            saisie_largeur1.pack(fill='both',pady=5)
            label_hauteur1.pack(fill='both')
            saisie_hauteur1.pack(fill='both',pady=5)
            # saisie affichage de départ
            saisie_longueur.insert(0, "0.0")
            saisie_largeur.insert(0, "0.0") 
            saisie_hauteur.insert(0, "0.0")
            saisie_largeur1.insert(0, "0.0") 
            saisie_hauteur1.insert(0, "0.0") 
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_longueur.focus() 
            saisie_longueur.select_range(0,END)
            # main au dessus de la case
            saisie_longueur.config(cursor='hand1')
            saisie_largeur.config(cursor='hand1')
            saisie_hauteur.config(cursor='hand1')
            saisie_largeur1.config(cursor='hand1')
            saisie_hauteur1.config(cursor='hand1')
            # la photo de la configuration
            canva_tab4.create_image(700,500, image=img_geo_rectangle_t)
            # lancement retour des touches
            saisie_longueur.bind('<Return>',largeur_next)
            saisie_largeur.bind('<Return>',hauteur_next)
            saisie_hauteur.bind('<Return>',largeur1_next)
            saisie_largeur1.bind('<Return>',hauteur1_next)
            saisie_hauteur1.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 2 :  index <",canva_tab1_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
    if str(geometrie.get()) == 'Carré':
        if str(geometrie3.get()) == 'Normal':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Longueur L de votre poutre en mm :',bg=gris_5)
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Largeur b de votre poutre en mm :',bg=gris_5)
            # saisie des inputs L,b,h
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_largeur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            # Placement des items sur une grille
            label_longueur.pack(fill='both')
            saisie_longueur.pack(fill='both',pady=5)
            label_largeur.pack(fill='both')
            saisie_largeur.pack(fill='both',pady=5)
            # saisie affichage de départ
            saisie_longueur.insert(0, "0.0")
            saisie_largeur.insert(0, "0.0")  
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_longueur.focus() 
            saisie_longueur.select_range(0,END)
            # main au dessus de la case
            saisie_longueur.config(cursor='hand1')
            saisie_largeur.config(cursor='hand1')
            # la photo de la configuration
            canva_tab4.create_image(700,500, image=img_geo_carre)
            # lancement retour des touches
            saisie_longueur.bind('<Return>',largeur_next)
            saisie_largeur.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 3 :  index <",canva_tab1_labelframe1_Combobox3.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox3.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(geometrie3.get()) == 'Troué':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Longueur L de votre poutre en mm :',bg=gris_5)
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Largeur b de votre poutre en mm :',bg=gris_5)
            label_largeur1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Largeur b1 de votre poutre en mm :',bg=gris_5)
            # saisie des inputs L,b,h
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_largeur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_largeur1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            # Placement des items sur une grille
            label_longueur.pack(fill='both')
            saisie_longueur.pack(fill='both',pady=5)
            label_largeur.pack(fill='both')
            saisie_largeur.pack(fill='both',pady=5)
            label_largeur1.pack(fill='both')
            saisie_largeur1.pack(fill='both',pady=5)
            # saisie affichage de départ
            saisie_longueur.insert(0, "0.0")
            saisie_largeur.insert(0, "0.0") 
            saisie_largeur1.insert(0, "0.0") 
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_longueur.focus() 
            saisie_longueur.select_range(0,END)
            # main au dessus de la case
            saisie_longueur.config(cursor='hand1')
            saisie_largeur.config(cursor='hand1')
            saisie_largeur1.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_geo_carre_t)
            # lancement retour des touches
            saisie_longueur.bind('<Return>',largeur_next)
            saisie_largeur.bind('<Return>',largeur1_next)
            saisie_largeur1.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 3 :  index <",canva_tab1_labelframe1_Combobox3.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox3.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
    if str(geometrie.get()) == 'Forme':
        if str(geometrie4.get()) == 'I':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Longueur L de votre poutre en mm :',bg=gris_5)
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Largeur b de votre poutre en mm :',bg=gris_5)
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Hauteur h de votre poutre en mm :',bg=gris_5)
            label_largeur1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Largeur de l’aile supérieure b1 de votre poutre en mm :',bg=gris_5)
            label_largeur2 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Largeur de l’aile inférieure b2 de votre poutre en mm :',bg=gris_5)
            label_hauteur1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Hauteur du tronc h1 de votre poutre en mm :',bg=gris_5)
            # saisie des inputs L,b,h
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_largeur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_hauteur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_largeur1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_largeur2 = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_hauteur1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            # Placement des items sur une grille
            label_longueur.pack(fill='both')
            saisie_longueur.pack(fill='both',pady=5)
            label_largeur.pack(fill='both')
            saisie_largeur.pack(fill='both',pady=5)
            label_hauteur.pack(fill='both')
            saisie_hauteur.pack(fill='both',pady=5)
            label_largeur1.pack(fill='both')
            saisie_largeur1.pack(fill='both',pady=5)
            label_largeur2.pack(fill='both')
            saisie_largeur2.pack(fill='both',pady=5)
            label_hauteur1.pack(fill='both')
            saisie_hauteur1.pack(fill='both',pady=5)
            # saisie affichage de départ
            saisie_longueur.insert(0, "0.0")
            saisie_largeur.insert(0, "0.0") 
            saisie_hauteur.insert(0, "0.0")
            saisie_largeur1.insert(0, "0.0")
            saisie_largeur2.insert(0, "0.0") 
            saisie_hauteur1.insert(0, "0.0") 
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_longueur.focus() 
            saisie_longueur.select_range(0,END)
            # main au dessus de la case
            saisie_longueur.config(cursor='hand1')
            saisie_largeur.config(cursor='hand1')
            saisie_hauteur.config(cursor='hand1')
            saisie_largeur1.config(cursor='hand1')
            saisie_largeur2.config(cursor='hand1')
            saisie_hauteur1.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_geo_forme_i)            
            # lancement retour des touches
            saisie_longueur.bind('<Return>',largeur_next)
            saisie_largeur.bind('<Return>',hauteur_next)
            saisie_hauteur.bind('<Return>',largeur1_next)
            saisie_largeur1.bind('<Return>',largeur2_next)
            saisie_largeur2.bind('<Return>',hauteur1_next)
            saisie_hauteur1.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 4 :  index <",canva_tab1_labelframe1_Combobox4.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox4.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(geometrie4.get()) == 'T':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Longueur L de votre poutre en mm :',bg=gris_5)
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Largeur b de votre poutre en mm :',bg=gris_5)
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Hauteur h de votre poutre en mm :',bg=gris_5)
            label_largeur1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Largeur de l’aile b1 de votre poutre en mm :',bg=gris_5)
            label_hauteur1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Hauteur du tronc h1 de votre poutre en mm :',bg=gris_5)
            # saisie des inputs L,b,h
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_largeur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_hauteur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_largeur1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_hauteur1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            # Placement des items sur une grille
            label_longueur.pack(fill='both')
            saisie_longueur.pack(fill='both',pady=5)
            label_largeur.pack(fill='both')
            saisie_largeur.pack(fill='both',pady=5)
            label_hauteur.pack(fill='both')
            saisie_hauteur.pack(fill='both',pady=5)
            label_largeur1.pack(fill='both')
            saisie_largeur1.pack(fill='both',pady=5)
            label_hauteur1.pack(fill='both')
            saisie_hauteur1.pack(fill='both',pady=5)
            # saisie affichage de départ
            saisie_longueur.insert(0, "0.0")
            saisie_largeur.insert(0, "0.0") 
            saisie_hauteur.insert(0, "0.0")
            saisie_largeur1.insert(0, "0.0") 
            saisie_hauteur1.insert(0, "0.0") 
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_longueur.focus() 
            saisie_longueur.select_range(0,END)
            # main au dessus de la case
            saisie_longueur.config(cursor='hand1')
            saisie_largeur.config(cursor='hand1')
            saisie_hauteur.config(cursor='hand1')
            saisie_largeur1.config(cursor='hand1')
            saisie_hauteur1.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_geo_forme_t)
            # lancement retour des touches
            saisie_longueur.bind('<Return>',largeur_next)
            saisie_largeur.bind('<Return>',hauteur_next)
            saisie_hauteur.bind('<Return>',largeur1_next)
            saisie_largeur1.bind('<Return>',hauteur1_next)
            saisie_hauteur1.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 4 :  index <",canva_tab1_labelframe1_Combobox4.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox4.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(geometrie4.get()) == 'L':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Longueur L de votre poutre en mm :',bg=gris_5)
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Largeur b de votre poutre en mm :',bg=gris_5)
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Hauteur h de votre poutre en mm :',bg=gris_5)
            label_largeur1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Largeur de l’aile b1 de votre poutre en mm :',bg=gris_5)
            label_hauteur1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Hauteur du tronc h1 de votre poutre en mm :',bg=gris_5)
            # saisie des inputs L,b,h
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_largeur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_hauteur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_largeur1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_hauteur1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            # Placement des items sur une grille
            label_longueur.pack(fill='both')
            saisie_longueur.pack(fill='both',pady=5)
            label_largeur.pack(fill='both')
            saisie_largeur.pack(fill='both',pady=5)
            label_hauteur.pack(fill='both')
            saisie_hauteur.pack(fill='both',pady=5)
            label_largeur1.pack(fill='both')
            saisie_largeur1.pack(fill='both',pady=5)
            label_hauteur1.pack(fill='both')
            saisie_hauteur1.pack(fill='both',pady=5)
            # saisie affichage de départ
            saisie_longueur.insert(0, "0.0")
            saisie_largeur.insert(0, "0.0") 
            saisie_hauteur.insert(0, "0.0")
            saisie_largeur1.insert(0, "0.0") 
            saisie_hauteur1.insert(0, "0.0") 
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_longueur.focus() 
            saisie_longueur.select_range(0,END)
            # main au dessus de la case
            saisie_longueur.config(cursor='hand1')
            saisie_largeur.config(cursor='hand1')
            saisie_hauteur.config(cursor='hand1')
            saisie_largeur1.config(cursor='hand1')
            saisie_hauteur1.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_geo_forme_l)
            # lancement retour des touches
            saisie_longueur.bind('<Return>',largeur_next)
            saisie_largeur.bind('<Return>',hauteur_next)
            saisie_hauteur.bind('<Return>',largeur1_next)
            saisie_largeur1.bind('<Return>',hauteur1_next)
            saisie_hauteur1.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 4 :  index <",canva_tab1_labelframe1_Combobox4.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox4.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(geometrie4.get()) == 'Z':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Longueur L de votre poutre en mm :',bg=gris_5)
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Largeur b de votre poutre en mm :',bg=gris_5)
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Hauteur h de votre poutre en mm :',bg=gris_5)
            label_largeur1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Largeur de l’aile b1 de votre poutre en mm :',bg=gris_5)
            label_largeur2 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Largeur de l’aile inférieure b2 de votre poutre en mm :',bg=gris_5)
            label_hauteur1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Hauteur du tronc h1 de votre poutre en mm :',bg=gris_5)
            # saisie des inputs L,b,h
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_largeur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_hauteur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_largeur1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_largeur2 = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_hauteur1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            # Placement des items sur une grille
            label_longueur.pack(fill='both')
            saisie_longueur.pack(fill='both',pady=5)
            label_largeur.pack(fill='both')
            saisie_largeur.pack(fill='both',pady=5)
            label_hauteur.pack(fill='both')
            saisie_hauteur.pack(fill='both',pady=5)
            label_largeur1.pack(fill='both')
            saisie_largeur1.pack(fill='both',pady=5)
            label_largeur2.pack(fill='both')
            saisie_largeur2.pack(fill='both',pady=5)
            label_hauteur1.pack(fill='both')
            saisie_hauteur1.pack(fill='both',pady=5)
            # saisie affichage de départ
            saisie_longueur.insert(0, "0.0")
            saisie_largeur.insert(0, "0.0") 
            saisie_hauteur.insert(0, "0.0")
            saisie_largeur1.insert(0, "0.0")
            saisie_largeur2.insert(0, "0.0")
            saisie_hauteur1.insert(0, "0.0") 
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_longueur.focus() 
            saisie_longueur.select_range(0,END)
            # main au dessus de la case
            saisie_longueur.config(cursor='hand1')
            saisie_largeur.config(cursor='hand1')
            saisie_hauteur.config(cursor='hand1')
            saisie_largeur1.config(cursor='hand1')
            saisie_largeur2.config(cursor='hand1')
            saisie_hauteur1.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_geo_forme_z)
            # lancement retour des touches
            saisie_longueur.bind('<Return>',largeur_next)
            saisie_largeur.bind('<Return>',hauteur_next)
            saisie_hauteur.bind('<Return>',largeur1_next)
            saisie_largeur1.bind('<Return>',largeur2_next)
            saisie_largeur2.bind('<Return>',hauteur1_next)
            saisie_hauteur1.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 4 :  index <",canva_tab1_labelframe1_Combobox4.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox4.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(geometrie4.get()) == 'Croix':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Longueur L de votre poutre en mm :',bg=gris_5)
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Largeur b de votre poutre en mm :',bg=gris_5)
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Hauteur h de votre poutre en mm :',bg=gris_5)
            # saisie des inputs L,b,h
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_largeur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_hauteur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            # Placement des items sur une grille
            label_longueur.pack(fill='both')
            saisie_longueur.pack(fill='both',pady=5)
            label_largeur.pack(fill='both')
            saisie_largeur.pack(fill='both',pady=5)
            label_hauteur.pack(fill='both')
            saisie_hauteur.pack(fill='both',pady=5)
            # saisie affichage de départ
            saisie_longueur.insert(0, "0.0")
            saisie_largeur.insert(0, "0.0") 
            saisie_hauteur.insert(0, "0.0") 
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_longueur.focus() 
            saisie_longueur.select_range(0,END)
            # main au dessus de la case
            saisie_longueur.config(cursor='hand1')
            saisie_largeur.config(cursor='hand1')
            saisie_hauteur.config(cursor='hand1')
            # la photo de la configuration 
            canva_tab4.create_image(700,500, image=img_geo_forme_croix)            
            # lancement retour des touches            
            saisie_longueur.bind('<Return>',largeur_next)
            saisie_largeur.bind('<Return>',hauteur_next)
            saisie_hauteur.bind('<Return>',valider_la_géométrie_auto) 
            print("Sélection en cours du Combobox 4 :  index <",canva_tab1_labelframe1_Combobox4.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox4.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
    if str(geometrie.get()) == 'Triangle':
        if str(geometrie5.get()) == 'Rectangle':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Longueur L de votre poutre en mm :',bg=gris_5)
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Largeur b de votre poutre en mm :',bg=gris_5)
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Hauteur h de votre poutre en mm :',bg=gris_5)
            # saisie des inputs L,b,h
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_largeur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_hauteur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            # Placement des items sur une grille
            label_longueur.pack(fill='both')
            saisie_longueur.pack(fill='both',pady=5)
            label_largeur.pack(fill='both')
            saisie_largeur.pack(fill='both',pady=5)
            label_hauteur.pack(fill='both')
            saisie_hauteur.pack(fill='both',pady=5)
            # saisie affichage de départ
            saisie_longueur.insert(0, "0.0")
            saisie_largeur.insert(0, "0.0") 
            saisie_hauteur.insert(0, "0.0") 
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_longueur.focus() 
            saisie_longueur.select_range(0,END)
            # main au dessus de la case
            saisie_longueur.config(cursor='hand1')
            saisie_largeur.config(cursor='hand1')
            saisie_hauteur.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_geo_triangle_rec)
            # lancement retour des touches
            saisie_longueur.bind('<Return>',largeur_next)
            saisie_largeur.bind('<Return>',hauteur_next)
            saisie_hauteur.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 5 :  index <",canva_tab1_labelframe1_Combobox5.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox5.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
    if str(geometrie.get()) == 'Cercle':
        if str(geometrie6.get()) == 'Normal':
            # messages des inputs L,R
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Longueur L de votre poutre en mm :',bg=gris_5)
            label_rayon = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer le Rayon R de votre poutre en mm :',bg=gris_5)
            # saisie des inputs L,R
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_rayon = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            # Placement des items sur une grille
            label_longueur.pack(fill='both')
            saisie_longueur.pack(fill='both',pady=5)
            label_rayon.pack(fill='both')
            saisie_rayon.pack(fill='both',pady=5)
            # saisie affichage de départ        
            saisie_longueur.insert(0, "0.0") # saisie affichage de départ
            saisie_rayon.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_longueur.focus() 
            saisie_longueur.select_range(0,END)
            # main au dessus de la case
            saisie_longueur.config(cursor='hand1')
            saisie_rayon.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_geo_cercle)
            # lancement retour des touches
            saisie_longueur.bind('<Return>',rayon_next)
            saisie_rayon.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 6 :  index <",canva_tab1_labelframe1_Combobox6.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox6.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(geometrie6.get()) == 'Troué':
            # messages des inputs L,R
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Longueur L de votre poutre en mm :',bg=gris_5)
            label_rayon = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer le Rayon R de votre poutre en mm :',bg=gris_5)
            label_rayon1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer le Rayon R1 de votre poutre en mm :',bg=gris_5)
            # saisie des inputs L,R
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_rayon = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_rayon1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            # Placement des items sur une grille
            label_longueur.pack(fill='both')
            saisie_longueur.pack(fill='both',pady=5)
            label_rayon.pack(fill='both')
            saisie_rayon.pack(fill='both',pady=5)
            label_rayon1.pack(fill='both')
            saisie_rayon1.pack(fill='both',pady=5)
            # saisie affichage de départ        
            saisie_longueur.insert(0, "0.0") # saisie affichage de départ
            saisie_rayon.insert(0, "0.0") # saisie affichage de départ
            saisie_rayon1.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_longueur.focus() 
            saisie_longueur.select_range(0,END)
            # main au dessus de la case
            saisie_longueur.config(cursor='hand1')
            saisie_rayon.config(cursor='hand1')
            saisie_rayon1.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_geo_cercle_t)
            # lancement retour des touches
            saisie_longueur.bind('<Return>',rayon_next)
            saisie_rayon.bind('<Return>',rayon1_next)
            saisie_rayon1.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 6 :  index <",canva_tab1_labelframe1_Combobox6.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox6.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(geometrie6.get()) == 'Demi Cercle':
            # messages des inputs L,R
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Longueur L de votre poutre en mm :',bg=gris_5)
            label_rayon = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer le Rayon R de votre poutre en mm :',bg=gris_5)
            # saisie des inputs L,R
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_rayon = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            # Placement des items sur une grille
            label_longueur.pack(fill='both')
            saisie_longueur.pack(fill='both',pady=5)
            label_rayon.pack(fill='both')
            saisie_rayon.pack(fill='both',pady=5)
            # saisie affichage de départ        
            saisie_longueur.insert(0, "0.0") # saisie affichage de départ
            saisie_rayon.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_longueur.focus() 
            saisie_longueur.select_range(0,END)
            # main au dessus de la case
            saisie_longueur.config(cursor='hand1')
            saisie_rayon.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_geo_demi_cercle)
            # lancement retour des touches
            saisie_longueur.bind('<Return>',rayon_next)
            saisie_rayon.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 6 :  index <",canva_tab1_labelframe1_Combobox6.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox6.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(geometrie6.get()) == 'Quart de Cercle':
            # messages des inputs L,R
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Longueur L de votre poutre en mm :',bg=gris_5)
            label_rayon = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer le Rayon R de votre poutre en mm :',bg=gris_5)
            # saisie des inputs L,R
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_rayon = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            # Placement des items sur une grille
            label_longueur.pack(fill='both')
            saisie_longueur.pack(fill='both',pady=5)
            label_rayon.pack(fill='both')
            saisie_rayon.pack(fill='both',pady=5)
            # saisie affichage de départ        
            saisie_longueur.insert(0, "0.0") # saisie affichage de départ
            saisie_rayon.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_longueur.focus() 
            saisie_longueur.select_range(0,END)
            # main au dessus de la case
            saisie_longueur.config(cursor='hand1')
            saisie_rayon.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_geo_quart_de_cercle)
            # lancement retour des touches
            saisie_longueur.bind('<Return>',rayon_next)
            saisie_rayon.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 6 :  index <",canva_tab1_labelframe1_Combobox6.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox6.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(geometrie6.get()) == 'Ovale':
            # messages des inputs L,R
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Longueur L de votre poutre en mm :',bg=gris_5)
            label_diagonale1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la grande diagonale D1 de votre poutre en mm :',bg=gris_5)
            label_diagonale2 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la petite diagonale D2 de votre poutre en mm :',bg=gris_5)
            # saisie des inputs L,R
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_diagonale1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_diagonale2 = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            # Placement des items sur une grille
            label_longueur.pack(fill='both')
            saisie_longueur.pack(fill='both',pady=5)
            label_diagonale1.pack(fill='both')
            saisie_diagonale1.pack(fill='both',pady=5)
            label_diagonale2.pack(fill='both')
            saisie_diagonale2.pack(fill='both',pady=5)
            # saisie affichage de départ        
            saisie_longueur.insert(0, "0.0") # saisie affichage de départ
            saisie_diagonale1.insert(0, "0.0") # saisie affichage de départ
            saisie_diagonale2.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_longueur.focus() 
            saisie_longueur.select_range(0,END)
            # main au dessus de la case
            saisie_longueur.config(cursor='hand1')
            saisie_diagonale1.config(cursor='hand1')
            saisie_diagonale2.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_geo_ovale)            
            # lancement retour des touches
            saisie_longueur.bind('<Return>',diagonale1_next)
            saisie_diagonale1.bind('<Return>',diagonale2_next)
            saisie_diagonale2.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 6 :  index <",canva_tab1_labelframe1_Combobox6.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox6.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
    if str(geometrie.get()) == 'Losange':
        if str(geometrie7.get()) == 'Normal':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Longueur L de votre poutre en mm :',bg=gris_5)
            label_diagonale1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la grande diagonale D1 de votre poutre en mm :',bg=gris_5)
            label_diagonale2 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la petite diagonale D2 de votre poutre en mm :',bg=gris_5)
            # saisie des inputs L,b,h
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_diagonale1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            saisie_diagonale2 = Entry(canva_tab1_labelframe2,disabledbackground = gris_4,font = ("Arial",11),bg=gris_2,justify='center')
            # Placement des items sur une grille
            label_longueur.pack(fill='both')
            saisie_longueur.pack(fill='both',pady=5)
            label_diagonale1.pack(fill='both')
            saisie_diagonale1.pack(fill='both',pady=5)
            label_diagonale2.pack(fill='both')
            saisie_diagonale2.pack(fill='both',pady=5)
            # saisie affichage de départ
            saisie_longueur.insert(0, "0.0") # saisie affichage de départ
            saisie_diagonale1.insert(0, "0.0") # saisie affichage de départ
            saisie_diagonale2.insert(0, "0.0") # saisie affichage de départ 
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_longueur.focus() 
            saisie_longueur.select_range(0,END)
            # main au dessus de la case
            saisie_longueur.config(cursor='hand1')
            saisie_diagonale1.config(cursor='hand1')
            saisie_diagonale2.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_geo_losange)            
            # lancement retour des touches
            saisie_longueur.bind('<Return>',diagonale1_next)
            saisie_diagonale1.bind('<Return>',diagonale2_next)
            saisie_diagonale2.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 7 :  index <",canva_tab1_labelframe1_Combobox7.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox7.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
# Gestion du stockage des valeurs automatique une fois que tous les entry dispos sont rentrés
def valider_la_géométrie_auto(event):
    valider_la_géométrie()
# Gestion du stockage des valeurs pour le bouton
def valider_la_géométrie():
    global label_longueur,label_largeur,label_largeur1,label_largeur2,label_rayon,label_rayon1\
        ,label_hauteur,label_hauteur1,label_diagonale1,label_diagonale2\
            ,saisie_longueur,saisie_largeur,saisie_largeur1,saisie_largeur2,saisie_rayon,saisie_rayon1\
                ,saisie_hauteur,saisie_hauteur1,saisie_diagonale1,saisie_diagonale2\
                    ,canva_tab1_labelframe2,valeurs_geometriques
    if str(geometrie.get()) == 'Rectangle':  
        L = float(saisie_longueur.get())
        if str(geometrie2.get()) == 'Normal':
            b = float(saisie_largeur.get())
            h = float(saisie_hauteur.get())
            if L!='' and b!='' and h!='' and L!=0.0 and b!=0.0 and h!=0.0 :
                b1=None ; b2=None ; h1=None ; R=None ; R1=None ; D1=None ; D2=None
                valeurs_geometriques=[geometrie.get(),geometrie2.get(),L,b,b1,b2,h,h1,R,R1,D1,D2]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or h==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or h=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie2.get(),") :",valeurs_geometriques)
        if str(geometrie2.get()) == 'Troué':
            L = float(saisie_longueur.get())
            b = float(saisie_largeur.get())
            b1 = float(saisie_largeur1.get())
            h = float(saisie_hauteur.get())    
            h1 = float(saisie_hauteur1.get())
            if L!='' and b!='' and b1!='' and h!='' and h1!='' and L!=0.0 and b!=0.0 and b1!=0.0 and h!=0.0 and h1!=0.0 :
                b2=None; R=None ; R1=None ; D1=None ; D2=None
                valeurs_geometriques=[geometrie.get(),geometrie2.get(),L,b,b1,b2,h,h1,R,R1,D1,D2]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or b1==0 or h==0 or h1==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or b1=='' or h=='' or h1=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie2.get(),") :",valeurs_geometriques)
    if str(geometrie.get()) == 'Carré':
        if str(geometrie3.get()) == 'Normal':
            L = float(saisie_longueur.get())
            b = float(saisie_largeur.get())            
            if L!='' and b!='' and L!=0.0 and b!=0.0:
                b1=None ; b2=None ; h=None ; h1=None ; R=None ; R1=None ; D1=None ; D2=None
                valeurs_geometriques=[geometrie.get(),geometrie3.get(),L,b,b1,b2,h,h1,R,R1,D1,D2]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie3.get(),") :",valeurs_geometriques)
        if str(geometrie3.get()) == 'Troué':
            L = float(saisie_longueur.get())
            b = float(saisie_largeur.get())
            b1 = float(saisie_largeur1.get())            
            if L!='' and b!='' and b1!='' and L!=0.0 and b!=0.0 and b1!=0.0 :
                b2=None ; h=None ; h1=None ; R=None ; R1=None ; D1=None ; D2=None
                valeurs_geometriques=[geometrie.get(),geometrie3.get(),L,b,b1,b2,h,h1,R,R1,D1,D2]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or b1==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or b1=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie3.get(),") :",valeurs_geometriques)            
    if str(geometrie.get()) == 'Forme':
        if str(geometrie4.get()) == 'I':
            L = float(saisie_longueur.get())
            b = float(saisie_largeur.get())
            b1 = float(saisie_largeur1.get())
            b2 = float(saisie_largeur2.get())
            h = float(saisie_hauteur.get())
            h1 = float(saisie_hauteur1.get())
            if L!='' and b!='' and b1!='' and h!='' and h1!='' and b2!='' and L!=0.0 and b!=0.0 and b1!=0.0 and h!=0.0 and h1!=0.0 and b2!=0.0:
                R=None ; R1=None ; D1=None ; D2=None
                valeurs_geometriques=[geometrie.get(),geometrie4.get(),L,b,b1,b2,h,h1,R,R1,D1,D2]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or b1==0 or h==0 or h1==0 or b2==0:
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or b1=='' or h=='' or h1=='' or b2=='':
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie4.get(),") :",valeurs_geometriques)
        if str(geometrie4.get()) == 'T':
            L = float(saisie_longueur.get())
            b = float(saisie_largeur.get())
            b1 = float(saisie_largeur1.get())
            h = float(saisie_hauteur.get())
            h1 = float(saisie_hauteur1.get())            
            if L!='' and b!='' and b1!='' and h!='' and h1!='' and L!=0.0 and b!=0.0 and b1!=0.0 and h!=0.0 and h1!=0.0 :
                b2=None; R=None ; R1=None ; D1=None ; D2=None
                valeurs_geometriques=[geometrie.get(),geometrie4.get(),L,b,b1,b2,h,h1,R,R1,D1,D2]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or b1==0 or h==0 or h1==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or b1=='' or h=='' or h1=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie4.get(),") :",valeurs_geometriques)
        if str(geometrie4.get()) == 'L':
            L = float(saisie_longueur.get())
            b = float(saisie_largeur.get())
            b1 = float(saisie_largeur1.get())
            h = float(saisie_hauteur.get())
            h1 = float(saisie_hauteur1.get())
            if L!='' and b!='' and b1!='' and h!='' and h1!='' and L!=0.0 and b!=0.0 and b1!=0.0 and h!=0.0 and h1!=0.0:
                b2=None; R=None ; R1=None ; D1=None ; D2=None
                valeurs_geometriques=[geometrie.get(),geometrie4.get(),L,b,b1,b2,h,h1,R,R1,D1,D2]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or b1==0 or h==0 or h1==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or b1=='' or h=='' or h1=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie4.get(),") :",valeurs_geometriques)
        if str(geometrie4.get()) == 'Z':
            L = float(saisie_longueur.get())
            b = float(saisie_largeur.get())
            b1 = float(saisie_largeur1.get())
            b2 = float(saisie_largeur2.get())
            h = float(saisie_hauteur.get())
            h1 = float(saisie_hauteur1.get())
            if L!='' and b!='' and b1!='' and h!='' and h1!='' and b2!=''and L!=0.0 and b!=0.0 and b1!=0.0 and h!=0.0 and h1!=0.0 and b2!=0.0:
                R=None ; R1=None ; D1=None ; D2=None
                valeurs_geometriques=[geometrie.get(),geometrie4.get(),L,b,b1,b2,h,h1,R,R1,D1,D2]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or b1==0 or h==0 or h1==0 or b2==0:
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or b1=='' or h=='' or h1=='' or b2=='':
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie4.get(),") :",valeurs_geometriques)
        if str(geometrie4.get()) == 'Croix':
            L = float(saisie_longueur.get())
            b = float(saisie_largeur.get())
            h = float(saisie_hauteur.get())
            if L!='' and b!='' and h!='' and L!=0.0 and b!=0.0 and h!=0.0 :
                b1=None ; b2=None ; h1=None ; R=None ; R1=None ; D1=None ; D2=None
                valeurs_geometriques=[geometrie.get(),geometrie4.get(),L,b,b1,b2,h,h1,R,R1,D1,D2]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or h==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or h=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie4.get(),") :",valeurs_geometriques)
    if str(geometrie.get()) == 'Triangle':
        if str(geometrie5.get()) == 'Rectangle':
            L = float(saisie_longueur.get())
            b = float(saisie_largeur.get())
            h = float(saisie_hauteur.get())
            if L!='' and b!='' and h!='' and L!=0.0 and b!=0.0 and h!=0.0 :
                b1=None ; b2=None ; h1=None ; R=None ; R1=None ; D1=None ; D2=None
                valeurs_geometriques=[geometrie.get(),geometrie5.get(),L,b,b1,b2,h,h1,R,R1,D1,D2]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or h==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or h=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie5.get(),") :",valeurs_geometriques)
    if str(geometrie.get()) == 'Cercle':
        if str(geometrie6.get()) == 'Normal':
            L = float(saisie_longueur.get())
            R = float(saisie_rayon.get())
            if L!='' and R!='' and L!=0.0 and R!=0.0 :
                b=None ; b1=None ; b2=None ; h=None ; h1=None ; R1=None ; D1=None ; D2=None
                valeurs_geometriques=[geometrie.get(),geometrie6.get(),L,b,b1,b2,h,h1,R,R1,D1,D2]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or R==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or R=='':
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie6.get(),") :",valeurs_geometriques)
        if str(geometrie6.get()) == 'Troué':
            L = float(saisie_longueur.get())
            R = float(saisie_rayon.get())
            R1 = float(saisie_rayon1.get())
            if L!='' and R!='' and R1!='' and L!=0.0 and R!=0.0 and R1!=0.0:
                b=None ; b1=None ; b2=None ; h=None ; h1=None ; D1=None ; D2=None
                valeurs_geometriques=[geometrie.get(),geometrie6.get(),L,b,b1,b2,h,h1,R,R1,D1,D2]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or R==0 or R1==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or R=='' or R1=='':
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie6.get(),") :",valeurs_geometriques)
        if str(geometrie6.get()) == 'Demi Cercle':
            L = float(saisie_longueur.get())
            R = float(saisie_rayon.get())
            if L!='' and R!='' and L!=0.0 and R!=0.0 :
                b=None ; b1=None ; b2=None ; h=None ; h1=None ; R1=None ; D1=None ; D2=None
                valeurs_geometriques=[geometrie.get(),geometrie6.get(),L,b,b1,b2,h,h1,R,R1,D1,D2]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or R==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or R=='':
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie6.get(),") :",valeurs_geometriques)
        if str(geometrie6.get()) == 'Quart de Cercle':
            L = float(saisie_longueur.get())
            R = float(saisie_rayon.get())
            if L!='' and R!='' and L!=0.0 and R!=0.0 :
                b=None ; b1=None ; b2=None ; h=None ; h1=None ; R1=None ; D1=None ; D2=None
                valeurs_geometriques=[geometrie.get(),geometrie6.get(),L,b,b1,b2,h,h1,R,R1,D1,D2]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or R==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or R=='':
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie6.get(),") :",valeurs_geometriques)
        if str(geometrie6.get()) == 'Ovale':
            L = float(saisie_longueur.get())
            D1 = float(saisie_diagonale1.get())
            D2 = float(saisie_diagonale2.get())
            if L!='' and D1!='' and D2!='' and L!=0.0 and D1!=0.0 and D2!=0.0 :
                b=None ; b1=None ; b2=None ; h=None ; h1=None ; R=None ; R1=None
                valeurs_geometriques=[geometrie.get(),geometrie6.get(),L,b,b1,b2,h,h1,R,R1,D1,D2]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or D1==0 or D2==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or D1=='' or D2=='':
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie6.get(),") :",valeurs_geometriques)
    if str(geometrie.get()) == 'Losange':
        if str(geometrie7.get()) == 'Normal':
            L = float(saisie_longueur.get())
            D1 = float(saisie_diagonale1.get())
            D2 = float(saisie_diagonale2.get())
            if L!='' and D1!='' and D2!='' and L!=0.0 and D1!=0.0 and D2!=0.0 :
                b=None ; b1=None ; b2=None ; h=None ; h1=None ; R=None ; R1=None
                valeurs_geometriques=[geometrie.get(),geometrie7.get(),L,b,b1,b2,h,h1,R,R1,D1,D2]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or D1==0 or D2==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or D1=='' or D2=='':
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie7.get(),") :",valeurs_geometriques)
# définition de fcts pour les lignes ci-dessous ou on gestionne le passage d'une case à l'autre et la désactivation de certains
def largeur_next(event): #fct pour passer à b
    saisie_largeur.focus()
    saisie_largeur.select_range(0,END)
def largeur1_next(event): #fct pour passer à b
    saisie_largeur1.focus()
    saisie_largeur1.select_range(0,END)
def largeur2_next(event): #fct pour passer à b
    saisie_largeur2.focus()
    saisie_largeur2.select_range(0,END)
def hauteur_next(event): #fct pour passer à h
    saisie_hauteur.focus()
    saisie_hauteur.select_range(0,END)
def hauteur1_next(event): #fct pour passer à h
    saisie_hauteur1.focus()
    saisie_hauteur1.select_range(0,END)
def rayon_next(event): #fct pour passer à R
    saisie_rayon.focus()
    saisie_rayon.select_range(0,END)
def rayon1_next(event): #fct pour passer à R
    saisie_rayon1.focus()
    saisie_rayon1.select_range(0,END)
def diagonale1_next(event): #fct pour passer à R
    saisie_diagonale1.focus()
    saisie_diagonale1.select_range(0,END)
def diagonale2_next(event): #fct pour passer à R
    saisie_diagonale2.focus()
    saisie_diagonale2.select_range(0,END)      
# Passage d'une combobox à l'autre   
canva_tab1_labelframe1_Combobox1.bind("<<ComboboxSelected>>", ajout_combobox)      
"""
Fin
"""

### Barre 2 : Matériau ###
tab2 = ttk.Frame(notebook) # Creation de la barre 1 de Notebook
# notebook.add(tab2, text='Matériau') # Ajout de la barre 1 au notebook
img2 = PhotoImage(file='images/construction-and-tools.png')
notebook.add(tab2,text='Matériau',image=img2, compound=LEFT) # Ajout de la barre 1 au notebook
canva_tab2=Canvas(tab2, bg=gris_5)
canva_tab2.pack(expand=1, fill='both')
#Création labelframe
canva_tab2_labelframe = LabelFrame(canva_tab2,font=("Arial",14 , "bold"),text = 'Données matériau',bg=gris_5) #définit le message 1
canva_tab2_labelframe.place(relx=0.01,rely=0.01,relwidth=0.98, relheight=0.37) # affiche le labelframe type de section
#messages des inputs E,Mv,m,m,Re,nu
label_young = Label(canva_tab2_labelframe,justify='center',font = ("Arial",10,"bold"),text = 'Entrer le Module de Young E de votre poutre en N/mm² ou MPa :',bg=gris_5)
label_massevol = Label(canva_tab2_labelframe,font = ("Arial",10,"bold"),text = 'Entrer la Masse volumique Mv de votre poutre en kg/mm3 : (Option)',bg=gris_5)
label_masse = Label(canva_tab2_labelframe,font = ("Arial",10,"bold"),text = 'Entrer la Masse m de votre poutre en kg : (Option)',bg=gris_5)
label_limiteel = Label(canva_tab2_labelframe,font = ("Arial",10,"bold"),text = 'Entrer la Limite élastique Re de votre poutre en MPa :',bg=gris_5)
label_coeffpoiss = Label(canva_tab2_labelframe,font = ("Arial",10,"bold"),text = 'Entrer le Coefficient de Poisson nu de votre poutre : (Option)',bg=gris_5)
#saisie des inputs E,Mv,m,m,Re,nu
saisie_young = Entry(canva_tab2_labelframe,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
saisie_massevol = Entry(canva_tab2_labelframe,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
saisie_masse = Entry(canva_tab2_labelframe,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
saisie_limiteel = Entry(canva_tab2_labelframe,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
saisie_coeffpoiss = Entry(canva_tab2_labelframe,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
#saisie affichage de départ
saisie_young.insert(0, "0.0")
saisie_massevol.insert(0, "0.0")
saisie_masse.insert(0, "0.0")
saisie_limiteel.insert(0, "0.0")
saisie_coeffpoiss.insert(0, "0.0")
#Placement des items sur la grille
label_young.pack(fill='both')
saisie_young.pack(fill='both',pady=5)
label_massevol.pack(fill='both')
saisie_massevol.pack(fill='both',pady=5)
label_masse.pack(fill='both')
saisie_masse.pack(fill='both',pady=5)
label_limiteel.pack(fill='both')
saisie_limiteel.pack(fill='both',pady=5)
label_coeffpoiss.pack(fill='both')
saisie_coeffpoiss.pack(fill='both',pady=5)
# Gestion du stockage des valeurs
def valider_le_materiau_event(event):
    valider_le_materiau()
def valider_le_materiau():
    global valeurs_materiau
    #Gestion du stockage des valeurs
    E = float(saisie_young.get())
    m = float(saisie_masse.get())
    Mv = float(saisie_massevol.get())
    Re = float(saisie_limiteel.get())
    nu = float(saisie_coeffpoiss.get())
    if E!='' and Re!='' :
        valeurs_materiau = [E,Mv,m,Re,nu]
        saisie_young.focus()
        saisie_young.select_range(0,END)
    if E==0 or Re==0 :
        showerror('Erreur', 'Un champ de coordonnées est vide')
    if E=='' or Re=='' :
        showerror('Erreur', 'Un champ de coordonnées est vide')
    print("Les valeurs de E,Mv,m,Re et nu sont :",valeurs_materiau)
# définition de fcts pour les lignes ci-dessous ou on gestionne le passage d'une case à l'autre et la désactivation de certains
def massevol_next(evt): #fct pour passer à Mv
    saisie_massevol.focus()
    saisie_massevol.select_range(0,END)
def masse_next(evt): #fct pour passer à m
    saisie_masse.focus()
    saisie_masse.select_range(0,END)
def limiteel_next(evt): #fct pour passer à Re
    saisie_limiteel.focus()
    saisie_limiteel.select_range(0,END)
def coeffpoiss_next(evt): #fct pour passer à nu
    saisie_coeffpoiss.focus()
    saisie_coeffpoiss.select_range(0,END)
def detection_passage2(evt): # détecte quand on doit passer d'une case à l'autre
    saisie_young.bind('<Return>', massevol_next) # switch de E à Mv quand on tape sur entrée
    saisie_massevol.bind('<Return>', masse_next) # switch de Mv à m quand on tape sur entrée
    saisie_masse.bind('<Return>', limiteel_next) # switch de m à Re quand on tape sur entrée
    saisie_limiteel.bind('<Return>', coeffpoiss_next) # switch de Re à nu quand on tape sur entrée
    saisie_coeffpoiss.bind('<Return>', valider_le_materiau_event) # switch de Re à nu quand on tape sur entrée   
# initialisation sélection
saisie_young.focus()
saisie_young.select_range(0,END)
saisie_young.bind('<Return>', detection_passage2)         
# Bouton pour valider l'entrée des données de matériau pour rassurer l'utilisateur
Button(canva_tab2_labelframe,relief="raised",overrelief="groove", text='Valider le matériau', command=valider_le_materiau, bg=gris_3,fg ="white", font=("Tahoma", 14,"bold")).place(relx=0,rely=0.90,relwidth=1, relheight=0.10)
"""
Fin
"""

### Barre 3 : Chargement ###
tab3 = ttk.Frame(notebook) # Creation de la barre 1 de Notebook
notebook.add(tab3, text='Chargement') # Ajout de la barre 1 au notebook
img3 = PhotoImage(file='images/loading.png')
notebook.add(tab3,text='Chargement',image=img3, compound=LEFT) # Ajout de la barre 1 au notebook
canva_tab3=Canvas(tab3, bg=gris_5)
canva_tab3.pack(expand=1, fill='both')
# Création labelframe 1
canva_tab3_labelframe1 = LabelFrame(canva_tab3,font = ("Arial",14 , "bold"),text = 'Type de chargement',bg = gris_5) #définit le message 1
canva_tab3_labelframe1.place(relx=0.01,rely=0.01,relwidth=0.98, relheight=0.12) # affiche le labelframe type de chargement    
# Choisir quelle est la charge 1 du problème
canva_tab3_labelframe1_label = Label(canva_tab3_labelframe1,text = "Choissiez le type de charge sur votre poutre :",bg = gris_5,font = ("Arial",10,"bold"))
canva_tab3_labelframe1_label.place(relx=0.01,rely=0.05,relwidth=0.98, relheight=0.30)
chargement = StringVar()
canva_tab3_labelframe1_Combobox1 = ttk.Combobox(canva_tab3_labelframe1, textvariable = chargement , state = "readonly",justify='center')
canva_tab3_labelframe1_Combobox1['values'] = ["","2 appuis simples", "1 encastrement et 1 bord libre"]
canva_tab3_labelframe1_Combobox1.place(relx=0.01,rely=0.36,relwidth=0.98, relheight=0.30) # affichage de la combobox

canva_tab3_labelframe1_Combobox1.current(0) # onglet actif dans la combobox quand on démarre 
# Choisir quelle est la charge 2 du problème
def ajout_combobox_chargement(event):
    global chargement,chargement2,chargement3,canva_tab3_labelframe1_Combobox2,canva_tab3_labelframe1_Combobox3
    print("Sélection en cours du Combobox 1 :  index <",canva_tab3_labelframe1_Combobox1.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox1.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
    if str(chargement.get()) == '2 appuis simples':
        chargement2 = StringVar()
        canva_tab3_labelframe1_Combobox2 = ttk.Combobox(canva_tab3_labelframe1, textvariable = chargement2 , state = "readonly",justify='center')
        canva_tab3_labelframe1_Combobox2['values'] = ["","Charge concentrée", "Charge uniformément répartie", "Charge uniformément répartie partielle",\
                                "Charge triangulaire", "Charge triangulaire monotone", "Charge triangulaire antisymétrique",\
                                    "Charge trapézoïdale","Charge parabolique","Moment","Moment uniformément réparti"]
        canva_tab3_labelframe1_Combobox2.place(relx=0.01,rely=0.67,relwidth=0.98, relheight=0.30) # affichage de la combobox
        canva_tab3_labelframe1_Combobox2.current(0) # onglet actif dans la combobox quand on démarre
        # Passage d'une combobox à l'autre   
        canva_tab3_labelframe1_Combobox2.bind("<<ComboboxSelected>>", ajout_données_chargement)
    if str(chargement.get()) == '1 encastrement et 1 bord libre':
        chargement3 = StringVar()
        canva_tab3_labelframe1_Combobox3 = ttk.Combobox(canva_tab3_labelframe1, textvariable = chargement3 , state = "readonly",justify='center')
        canva_tab3_labelframe1_Combobox3['values'] = ["","Charge concentrée", "Charge uniformément répartie", "Charge uniformément répartie partielle",\
                                "Charge triangulaire croissante", "Charge triangulaire décroissante","Moment"]
        canva_tab3_labelframe1_Combobox3.place(relx=0.01,rely=0.67,relwidth=0.98, relheight=0.30) # affichage de la combobox
        canva_tab3_labelframe1_Combobox3.current(0) # onglet actif dans la combobox quand on démarre
        # Passage d'une combobox à l'autre   
        canva_tab3_labelframe1_Combobox3.bind("<<ComboboxSelected>>", ajout_données_chargement) 
def ajout_données_chargement(event): # nouvelle frame où on rentre les données du chargement
    global label_force_conc_1,label_force_rep_1,label_a1,label_c1,label_I,label_moment,\
        saisie_force_conc_1,saisie_force_rep_1,saisie_a1,saisie_c1,saisie_I,saisie_moment,canva_tab3_labelframe2
    # nouveau_labelframe_chargement
    canva_tab3_labelframe2 = LabelFrame(canva_tab3,font=("Arial",14 , "bold"),text = "Chargement",bg=gris_5) #définit le message 1
    canva_tab3_labelframe2.place(relx=0.01,rely=0.14,relwidth=0.98, relheight=0.23) # affiche le labelframe type de section
    # Apparition du list box
    yDefilB = Scrollbar(canva_tab3, orient='vertical')
    yDefilB.place(relx=0.94,rely=0.38,relwidth=0.05, relheight=0.51)
    Listbox_tab3 = Listbox(canva_tab3,activestyle= 'dotbox',selectmode=SINGLE,yscrollcommand=yDefilB.set)
    Liste_listboxCharges.append(Listbox_tab3)
    Liste_listboxCharges[0].place(relx=0.01,rely=0.38,relwidth=0.93, relheight=0.51)
    yDefilB['command'] = Listbox_tab3.yview
    # Apparition bouton ajouter/supprimer/renommer charge
    Button(canva_tab3,relief="raised",overrelief="groove", text='Ajouter la charge', command=ajout_charge, bg=gris_3,fg ="white", font=("Tahoma", 14,"bold")).place(relx=0.01,rely=0.90,relwidth=0.49, relheight=0.04)
    Button(canva_tab3,relief="raised",overrelief="groove", text='Renommer la charge', command=renommer_charge, bg=gris_3,fg ="white", font=("Tahoma", 14,"bold")).place(relx=0.51,rely=0.90,relwidth=0.48, relheight=0.04)
    Button(canva_tab3,relief="raised",overrelief="groove", text='Supprimer la charge', command=supprimer_charge, bg=gris_3,fg ="white", font=("Tahoma", 14,"bold")).place(relx=0.01,rely=0.95,relwidth=0.98, relheight=0.04)
    if str(chargement.get()) == '2 appuis simples' : 
        if str(chargement2.get()) == 'Charge concentrée' :
            # messages des inputs
            label_force_conc_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Force concentrée P sur votre poutre en N :',bg=gris_5)
            label_a1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la distance a1 de votre poutre en mm :',bg=gris_5)
            # saisie des inputs
            saisie_force_conc_1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            saisie_a1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            # Placement des items sur la grille
            label_force_conc_1.pack(fill='both')
            saisie_force_conc_1.pack(fill='both')
            label_a1.pack(fill='both')
            saisie_a1.pack(fill='both')
            # saisie affichage de départ
            saisie_force_conc_1.insert(0, "0.0") # saisie affichage de départ
            saisie_a1.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_force_conc_1.focus() 
            saisie_force_conc_1.select_range(0,END)
            # main au dessus de la case
            saisie_force_conc_1.config(cursor='hand1')
            saisie_a1.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_charge_con_app_simple)               
            # lancement retour des touches
            saisie_force_conc_1.bind('<Return>',a1_next)
            saisie_a1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 2 :  index <",canva_tab3_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement2.get()) == 'Charge uniformément répartie' :
            # messages des inputs
            label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Force répartie q sur votre poutre en N/mm :',bg=gris_5)
            # saisie des inputs
            saisie_force_rep_1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            # Placement des items sur la grille
            label_force_rep_1.pack(fill='both')
            saisie_force_rep_1.pack(fill='both')
            # saisie affichage de départ
            saisie_force_rep_1.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_force_rep_1.focus() 
            saisie_force_rep_1.select_range(0,END)
            # main au dessus de la case
            saisie_force_rep_1.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_charge_rep_app_simple)               
            # lancement retour des touches
            saisie_force_rep_1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 2 :  index <",canva_tab3_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement2.get()) == 'Charge uniformément répartie partielle' :
            # messages des inputs
            label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Force répartie q sur votre poutre en N/mm :',bg=gris_5)
            label_I = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Distance sur laquelle la charge s’applique I sur votre \n poutre en mm :',bg=gris_5)        
            label_c1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Distance entre le noeud de base et l’endroit du début \n d’application de la charge c1 sur votre poutre en mm :',bg=gris_5)
            # saisie des inputs
            saisie_force_rep_1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            saisie_I = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            saisie_c1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            # Placement des items sur la grille
            label_force_rep_1.pack(fill='both')
            saisie_force_rep_1.pack(fill='both')
            label_I.pack(fill='both')
            saisie_I.pack(fill='both')
            label_c1.pack(fill='both')
            saisie_c1.pack(fill='both')
            # saisie affichage de départ
            saisie_force_rep_1.insert(0, "0.0") # saisie affichage de départ
            saisie_I.insert(0, "0.0") # saisie affichage de départ
            saisie_c1.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_force_rep_1.focus() 
            saisie_force_rep_1.select_range(0,END)
            # main au dessus de la case
            saisie_force_rep_1.config(cursor='hand1')
            saisie_I.config(cursor='hand1')
            saisie_c1.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_charge_rep_part)             
            # lancement retour des touches
            saisie_force_rep_1.bind('<Return>',I_next)
            saisie_I.bind('<Return>',c1_next)
            saisie_c1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 2 :  index <",canva_tab3_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement2.get()) == 'Charge triangulaire' :
            # messages des inputs
            label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Force répartie q sur votre poutre en N :',bg=gris_5)
            label_a1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la distance a1 de votre poutre en mm :',bg=gris_5)
            # saisie des inputs
            saisie_force_rep_1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            saisie_a1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            # Placement des items sur la grille
            label_force_rep_1.pack(fill='both')
            saisie_force_rep_1.pack(fill='both')
            label_a1.pack(fill='both')
            saisie_a1.pack(fill='both')
            # saisie affichage de départ
            saisie_force_rep_1.insert(0, "0.0") # saisie affichage de départ
            saisie_a1.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_force_rep_1.focus() 
            saisie_force_rep_1.select_range(0,END)
            # main au dessus de la case
            saisie_force_rep_1.config(cursor='hand1')
            saisie_a1.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_charge_triang) 
            # lancement retour des touches
            saisie_force_rep_1.bind('<Return>',a1_next)
            saisie_a1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 2 :  index <",canva_tab3_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement2.get()) == 'Charge triangulaire monotone' :
            # messages des inputs
            label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Force répartie q sur votre poutre en N :',bg=gris_5)
            # saisie des inputs
            saisie_force_rep_1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            # Placement des items sur la grille
            label_force_rep_1.pack(fill='both')
            saisie_force_rep_1.pack(fill='both')
            # saisie affichage de départ
            saisie_force_rep_1.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_force_rep_1.focus() 
            saisie_force_rep_1.select_range(0,END)
            # main au dessus de la case
            saisie_force_rep_1.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_charge_triang_monotone) 
            # lancement retour des touches
            saisie_force_rep_1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 2 :  index <",canva_tab3_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement2.get()) == 'Charge triangulaire antisymétrique' :
            # messages des inputs
            label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Force répartie q sur votre poutre en N :',bg=gris_5)
            # saisie des inputs
            saisie_force_rep_1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            # Placement des items sur la grille
            label_force_rep_1.pack(fill='both')
            saisie_force_rep_1.pack(fill='both')
            # saisie affichage de départ
            saisie_force_rep_1.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_force_rep_1.focus() 
            saisie_force_rep_1.select_range(0,END)
            # main au dessus de la case
            saisie_force_rep_1.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_charge_triang_anti) 
            # lancement retour des touches
            saisie_force_rep_1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 2 :  index <",canva_tab3_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement2.get()) == 'Charge trapézoïdale' :
            # messages des inputs
            label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Force répartie q sur votre poutre en N/mm :',bg=gris_5)
            label_I = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Distance sur laquelle la charge s’applique I sur votre \n poutre en mm :',bg=gris_5)        
            label_c1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Distance entre le noeud de base et l’endroit du début \n d’application de la charge c1 sur votre poutre en mm :',bg=gris_5)
            # saisie des inputs
            saisie_force_rep_1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            saisie_I = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            saisie_c1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            # Placement des items sur la grille
            label_force_rep_1.pack(fill='both')
            saisie_force_rep_1.pack(fill='both')
            label_I.pack(fill='both')
            saisie_I.pack(fill='both')
            label_c1.pack(fill='both')
            saisie_c1.pack(fill='both')
            # saisie affichage de départ
            saisie_force_rep_1.insert(0, "0.0") # saisie affichage de départ
            saisie_I.insert(0, "0.0") # saisie affichage de départ
            saisie_c1.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_force_rep_1.focus() 
            saisie_force_rep_1.select_range(0,END)
            # main au dessus de la case
            saisie_force_rep_1.config(cursor='hand1')
            saisie_I.config(cursor='hand1')
            saisie_c1.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_charge_trapèze) 
            # lancement retour des touches
            saisie_force_rep_1.bind('<Return>',I_next)
            saisie_I.bind('<Return>',c1_next)
            saisie_c1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 2 :  index <",canva_tab3_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement2.get()) == 'Charge parabolique' :
            # messages des inputs
            label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Force répartie q sur votre poutre en N :',bg=gris_5)
            # saisie des inputs
            saisie_force_rep_1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            # Placement des items sur la grille
            label_force_rep_1.pack(fill='both')
            saisie_force_rep_1.pack(fill='both')
            # saisie affichage de départ
            saisie_force_rep_1.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_force_rep_1.focus() 
            saisie_force_rep_1.select_range(0,END)
            # main au dessus de la case
            saisie_force_rep_1.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_charge_parabo) 
            # lancement retour des touches
            saisie_force_rep_1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 2 :  index <",canva_tab3_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement2.get()) == 'Moment' :
            # messages des inputs
            label_moment = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer le Moment M sur votre poutre en N.mm :',bg=gris_5)
            label_a1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la distance a1 de votre poutre en mm :',bg=gris_5)
            # saisie des inputs
            saisie_moment = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            saisie_a1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            # Placement des items sur la grille
            label_moment.pack(fill='both')
            saisie_moment.pack(fill='both')
            label_a1.pack(fill='both')
            saisie_a1.pack(fill='both')
            # saisie affichage de départ
            saisie_moment.insert(0, "0.0") # saisie affichage de départ
            saisie_a1.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_moment.focus() 
            saisie_moment.select_range(0,END)
            # main au dessus de la case
            saisie_moment.config(cursor='hand1')
            saisie_a1.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_charge_moment_app_simple) 
            # lancement retour des touches
            saisie_moment.bind('<Return>',a1_next)
            saisie_a1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 2 :  index <",canva_tab3_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement2.get()) == 'Moment uniformément réparti' :    
            # messages des inputs
            label_moment = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer le Moment M sur votre poutre en N.mm :',bg=gris_5)
            # saisie des inputs
            saisie_moment = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            # Placement des items sur la grille
            label_moment.pack(fill='both')
            saisie_moment.pack(fill='both')
            # saisie affichage de départ
            saisie_moment.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_moment.focus() 
            saisie_moment.select_range(0,END)
            # main au dessus de la case
            saisie_moment.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_charge_moment_unfi) 
            # lancement retour des touches
            saisie_moment.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 2 :  index <",canva_tab3_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
    if str(chargement.get()) == '1 encastrement et 1 bord libre' : 
        if str(chargement3.get()) == 'Charge concentrée' :
            # messages des inputs
            label_force_conc_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Force concentrée P sur votre poutre en N :',bg=gris_5)
            label_a1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la distance a1 de votre poutre en mm :',bg=gris_5)
            # saisie des inputs
            saisie_force_conc_1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            saisie_a1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            # Placement des items sur la grille
            label_force_conc_1.pack(fill='both')
            saisie_force_conc_1.pack(fill='both')
            label_a1.pack(fill='both')
            saisie_a1.pack(fill='both')
            # saisie affichage de départ
            saisie_force_conc_1.insert(0, "0.0") # saisie affichage de départ
            saisie_a1.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_force_conc_1.focus() 
            saisie_force_conc_1.select_range(0,END)
            # main au dessus de la case
            saisie_force_conc_1.config(cursor='hand1')
            saisie_a1.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_charge_con_encas) 
            # lancement retour des touches
            saisie_force_conc_1.bind('<Return>',a1_next)
            saisie_a1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 3 :  index <",canva_tab3_labelframe1_Combobox3.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox3.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement3.get()) == 'Charge uniformément répartie' :
            # messages des inputs
            label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Force répartie q sur votre poutre en N/mm :',bg=gris_5)
            # saisie des inputs
            saisie_force_rep_1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            # Placement des items sur la grille
            label_force_rep_1.pack(fill='both')
            saisie_force_rep_1.pack(fill='both')
            # saisie affichage de départ
            saisie_force_rep_1.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_force_rep_1.focus() 
            saisie_force_rep_1.select_range(0,END)
            # main au dessus de la case
            saisie_force_rep_1.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_charge_rep_encas) 
            # lancement retour des touches
            saisie_force_rep_1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 3 :  index <",canva_tab3_labelframe1_Combobox3.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox3.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement3.get()) == 'Charge uniformément répartie partielle' :
            # messages des inputs
            label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Force répartie q sur votre poutre en N/mm :',bg=gris_5)
            label_I = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Distance sur laquelle la charge s’applique I sur votre \n poutre en mm :',bg=gris_5)        
            label_c1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Distance entre le noeud de base et l’endroit du début \n d’application de la charge c1 sur votre poutre en mm :',bg=gris_5)
            # saisie des inputs
            saisie_force_rep_1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            saisie_I = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            saisie_c1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            # Placement des items sur la grille
            label_force_rep_1.pack(fill='both')
            saisie_force_rep_1.pack(fill='both')
            label_I.pack(fill='both')
            saisie_I.pack(fill='both')
            label_c1.pack(fill='both')
            saisie_c1.pack(fill='both')
            # saisie affichage de départ
            saisie_force_rep_1.insert(0, "0.0") # saisie affichage de départ
            saisie_I.insert(0, "0.0") # saisie affichage de départ
            saisie_c1.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_force_rep_1.focus() 
            saisie_force_rep_1.select_range(0,END)
            # main au dessus de la case
            saisie_force_rep_1.config(cursor='hand1')
            saisie_I.config(cursor='hand1')
            saisie_c1.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_charge_rep_part) 
            # lancement retour des touches
            saisie_force_rep_1.bind('<Return>',I_next)
            saisie_I.bind('<Return>',c1_next)
            saisie_c1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 3 :  index <",canva_tab3_labelframe1_Combobox3.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox3.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement3.get()) == 'Charge triangulaire croissante' :
            # messages des inputs
            label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Force répartie q sur votre poutre en N :',bg=gris_5)
            # saisie des inputs
            saisie_force_rep_1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            # Placement des items sur la grille
            label_force_rep_1.pack(fill='both')
            saisie_force_rep_1.pack(fill='both')
            # saisie affichage de départ
            saisie_force_rep_1.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_force_rep_1.focus() 
            saisie_force_rep_1.select_range(0,END)
            # main au dessus de la case
            saisie_force_rep_1.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_charge_triang_croiss) 
            # lancement retour des touches
            saisie_force_rep_1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 3 :  index <",canva_tab3_labelframe1_Combobox3.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox3.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement3.get()) == 'Charge triangulaire décroissante' :
            # messages des inputs
            label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la Force répartie q sur votre poutre en N :',bg=gris_5)
            # saisie des inputs
            saisie_force_rep_1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            # Placement des items sur la grille
            label_force_rep_1.pack(fill='both')
            saisie_force_rep_1.pack(fill='both')
            # saisie affichage de départ
            saisie_force_rep_1.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_force_rep_1.focus() 
            saisie_force_rep_1.select_range(0,END)
            # main au dessus de la case
            saisie_force_rep_1.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_charge_triang_décroiss) 
            # lancement retour des touches
            saisie_force_rep_1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 3 :  index <",canva_tab3_labelframe1_Combobox3.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox3.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement3.get()) == 'Moment' :
            # messages des inputs
            label_moment = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer le Moment M sur votre poutre en N.mm :',bg=gris_5)
            label_a1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrer la distance a1 de votre poutre en mm :',bg=gris_5)
            # saisie des inputs
            saisie_moment = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            saisie_a1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            # Placement des items sur la grille
            label_moment.pack(fill='both')
            saisie_moment.pack(fill='both')
            label_a1.pack(fill='both')
            saisie_a1.pack(fill='both')
            # saisie affichage de départ
            saisie_moment.insert(0, "0.0") # saisie affichage de départ
            saisie_a1.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_moment.focus() 
            saisie_moment.select_range(0,END)
            # main au dessus de la case
            saisie_moment.config(cursor='hand1')
            saisie_a1.config(cursor='hand1')
            # la photo de la configuration            
            canva_tab4.create_image(700,500, image=img_charge_moment_encas) 
            # lancement retour des touches
            saisie_moment.bind('<Return>',a1_next)
            saisie_a1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 3 :  index <",canva_tab3_labelframe1_Combobox3.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox3.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
# Définition des listes pour la listbox 
Liste_listboxCharges = []
liste_charges = []
tabl_c_concentrée = []
tabl_c_répartie = []
tabl_c_répartie_partielle = []
tabl_c_triang = []
tabl_c_triangulaire_mon = []
tabl_c_triangulaire_antisy = []
tabl_c_trapézoïdale_sy = []
tabl_c_parabolique = []
tabl_couple = []
tabl_couple_réparti = []
tabl_c_décrois = []
tabl_c_crois = []
def ajout_charge_event(event):
    ajout_charge()
def ajout_charge():
    global label_force_conc_1,label_force_rep_1,label_a1,label_c1,label_I,label_moment,\
        saisie_force_conc_1,saisie_force_rep_1,saisie_a1,saisie_c1,saisie_I,saisie_moment,canva_tab3_labelframe2,liste_charges,Liste_listboxCharges
    if str(chargement.get()) == '2 appuis simples' : 
        if str(chargement2.get()) == 'Charge concentrée' :
            p = float(saisie_force_conc_1.get())
            a1 = float(saisie_a1.get())
            if p!= 0.0 and a1!= 0.0 :
                VarEcrase = classe.charge_concentrée(p, a1)
                tabl_c_concentrée.append(VarEcrase)  
                nbr = classe.charge_concentrée.nbr
                liste_charges.append(['Appuis Simple / Charge concentrée '+str(len(liste_charges)+1)+str(nbr),[ "[P = ", tabl_c_concentrée[nbr-1].P , " ; a = ", tabl_c_concentrée[nbr-1].a ,"]"]])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_conc_1.focus()
                saisie_force_conc_1.select_range(0,END)
            if float(saisie_force_conc_1.get())==0 or float(saisie_a1.get())==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide.')   
        elif str(chargement2.get()) == 'Charge uniformément répartie' :
            q = float(saisie_force_rep_1.get())
            if q!='' and q!= 0.0:
                VarEcrase = classe.charge_répartie(q)
                tabl_c_répartie.append(VarEcrase)  
                nbr = classe.charge_répartie.nbr
                liste_charges.append(['Appuis Simple / Charge répartie '+str(len(liste_charges)+1)+str(nbr),[ "[q = ", tabl_c_répartie[nbr-1].q ,"]"]])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_rep_1.focus()
                saisie_force_rep_1.select_range(0,END)
            if q==0 or q=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide.')    
        elif str(chargement2.get()) == 'Charge uniformément répartie partielle' :
            q = float(saisie_force_rep_1.get())
            I = float(saisie_I.get())
            c1 = float(saisie_c1.get())
            if q!='' and I!='' and c1!='' and q!= 0.0 and I!= 0.0 and c1!= 0.0:
                VarEcrase = classe.charge_répartie_partielle(q, c1, I)
                tabl_c_répartie_partielle.append(VarEcrase) 
                nbr = classe.charge_répartie_partielle.nbr
                liste_charges.append(['Appuis Simple / Charge répartie partielle '+str(len(liste_charges)+1)+str(nbr),[ "[q = ", tabl_c_répartie_partielle[nbr-1].q , " ; c1 = ", tabl_c_répartie_partielle[nbr-1].a , " ; l = ", tabl_c_répartie_partielle[nbr-1].l, "]"]])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_rep_1.focus()
                saisie_force_rep_1.select_range(0,END)
            if q==0 or I==0 or c1==0 or q=='' or I=='' or c1=='':
                showerror('Erreur', 'Un champ de coordonnées est vide.')
        elif str(chargement2.get()) == 'Charge triangulaire' :
            q = float(saisie_force_rep_1.get())
            a1 = float(saisie_a1.get())
            if q!='' and a1!=''and q!= 0.0 and a1!= 0.0 :
                VarEcrase = classe.charge_triangulaire(q, a1)
                tabl_c_triang.append(VarEcrase) 
                nbr = classe.charge_triangulaire.nbr
                liste_charges.append(['Appuis Simple / Charge triangulaire '+str(len(liste_charges)+1)+str(nbr),[ "[q = ", tabl_c_triang[nbr-1].q , " ; a1 = ", tabl_c_triang[nbr-1].a ,"]"]])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_rep_1.focus()
                saisie_force_rep_1.select_range(0,END)
            if q==0 or a1==0 or q=='' or a1=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide.')
        elif str(chargement2.get()) == 'Charge triangulaire monotone' :
            q = float(saisie_force_rep_1.get())
            if q!='' and q!=0.0:
                VarEcrase = classe.charge_triangulaire_monotone(q)
                tabl_c_triangulaire_mon.append(VarEcrase)
                nbr = classe.charge_triangulaire_monotone.nbr
                liste_charges.append(['Appuis Simple / Charge triangulaire monotone '+str(len(liste_charges)+1)+str(nbr),[ "[q = ", tabl_c_triangulaire_mon[nbr-1].q ,"]"]])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_rep_1.focus()
                saisie_force_rep_1.select_range(0,END)
            if q==0 or q=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide.')
        elif str(chargement2.get()) == 'Charge triangulaire antisymétrique' :
            q = float(saisie_force_rep_1.get())
            if q!='' and q!=0.0:
                VarEcrase = classe.charge_triangulaire_antisymétrique(q)
                tabl_c_triangulaire_antisy.append(VarEcrase)
                nbr = classe.charge_triangulaire_antisymétrique.nbr
                liste_charges.append(['Appuis Simple / Charge triangulaire antisymétrique '+str(len(liste_charges)+1)+str(nbr),[ "[q = ", tabl_c_triangulaire_antisy[nbr-1].q , "]"]])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_rep_1.focus()
                saisie_force_rep_1.select_range(0,END)
            if q==0 or q=='':
                showerror('Erreur', 'Un champ de coordonnées est vide.') 
        elif str(chargement2.get()) == 'Charge trapézoïdale' :
            q = float(saisie_force_rep_1.get())
            I = float(saisie_I.get())
            c1 = float(saisie_c1.get())
            if q!='' and I!='' and c1!='' and q!= 0.0 and I!= 0.0 and c1!= 0.0:
                VarEcrase = classe.charge_trapézoïdale_symétrique(q, c1, I)
                tabl_c_trapézoïdale_sy.append(VarEcrase)
                nbr = classe.charge_trapézoïdale_symétrique.nbr
                liste_charges.append(['Appuis Simple / Charge trapézoïdale '+str(len(liste_charges)+1)+str(nbr),[ "[q = ", tabl_c_trapézoïdale_sy[nbr-1].q , " ; c1 = ", tabl_c_trapézoïdale_sy[nbr-1].a , " ; l = ", tabl_c_trapézoïdale_sy[nbr-1].l ,"]"]])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_rep_1.focus()
                saisie_force_rep_1.select_range(0,END)
            if q==0 or I==0 or c1==0 or q=='' or I=='' or c1=='':
                showerror('Erreur', 'Un champ de coordonnées est vide.')
        elif str(chargement2.get()) == 'Charge parabolique' :
            q = float(saisie_force_rep_1.get())
            if q!='' and q!=0.0:
                VarEcrase = classe.charge_parabolique(q)
                tabl_c_parabolique.append(VarEcrase)
                nbr = classe.charge_parabolique.nbr
                liste_charges.append(['Appuis Simple / Charge parabolique '+str(len(liste_charges)+1)+str(nbr),[ "[q = ", tabl_c_parabolique[nbr-1].q ,"]"]])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_rep_1.focus()
                saisie_force_rep_1.select_range(0,END)
            if q==0 or q=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide.') 
        elif str(chargement2.get()) == 'Moment' :
            M = float(saisie_moment.get())
            a1 = float(saisie_a1.get())
            if M!='' and a1!=''and M!= 0.0 and a1!= 0.0 :
                VarEcrase = classe.couple(M, a1)
                tabl_couple.append(VarEcrase)
                nbr = classe.couple.nbr
                liste_charges.append(['Appuis Simple / couple '+str(len(liste_charges)+1)+str(nbr),[ "[M = ", tabl_couple[nbr-1].C , " ; a1 = ", tabl_couple[nbr-1].a ,"]"]])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_moment.focus()
                saisie_moment.select_range(0,END)
            if M==0 or a1==0 or M=='' or a1=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide.')
        elif str(chargement2.get()) == 'Moment uniformément réparti' :    
            M = float(saisie_moment.get())
            if M!='' and M!= 0.0 :
                VarEcrase = classe.couple_réparti(M)
                tabl_couple_réparti.append(VarEcrase)
                nbr = classe.couple_réparti.nbr
                liste_charges.append(['Appuis Simple / Couple réparti '+str(len(liste_charges)+1)+str(nbr),[ "[M = ", tabl_couple_réparti[nbr-1].C ,"]"]])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_moment.focus()
                saisie_moment.select_range(0,END)
            if M==0 or a1==0 or M=='' or a1=='':
                showerror('Erreur', 'Un champ de coordonnées est vide.')
    elif str(chargement.get()) == '1 encastrement et 1 bord libre' : 
        if str(chargement3.get()) == 'Charge concentrée' :
            p = float(saisie_force_conc_1.get())
            a1 = float(saisie_a1.get())
            if p!='' and a1!='' and p!= 0.0 and a1!= 0.0 :
                VarEcrase = classe.charge_concentrée(p, a1)
                tabl_c_concentrée.append(VarEcrase)  
                nbr = classe.charge_concentrée.nbr
                liste_charges.append(['Encastrement / Charge concentrée '+str(len(liste_charges)+1),[ "[P = ", tabl_c_concentrée[nbr-1].P , " ; a1 = ", tabl_c_concentrée[nbr-1].a ,"]"]])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_conc_1.focus()
                saisie_force_conc_1.select_range(0,END)
            if p==0 or a1==0 or p=='' or a1=='':
                showerror('Erreur', 'Un champ de coordonnées est vide.')   
        elif str(chargement3.get()) == 'Charge uniformément répartie' :
            q = float(saisie_force_rep_1.get())
            if q!='' and q!=0.0:
                VarEcrase = classe.charge_répartie(q)
                tabl_c_répartie.append(VarEcrase)  
                nbr = classe.charge_répartie.nbr
                liste_charges.append(['Encastrement / Charge répartie '+str(len(liste_charges)+1),[ "[q = ", tabl_c_répartie[nbr-1].q ,"]"]])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_rep_1.focus()
                saisie_force_rep_1.select_range(0,END)
            if q==0 or q=='':
                showerror('Erreur', 'Un champ de coordonnées est vide.')
        elif str(chargement3.get()) == 'Charge uniformément répartie partielle' :
            q = float(saisie_force_rep_1.get())
            I = float(saisie_I.get())
            c1 = float(saisie_c1.get())
            if q!='' and I!='' and c1!='' and q!= 0.0 and I!= 0.0 and c1!= 0.0:
                VarEcrase = classe.charge_répartie_partielle(q, c1, I)
                tabl_c_répartie_partielle.append(VarEcrase) 
                nbr = classe.charge_répartie_partielle.nbr
                liste_charges.append(['Encastrement / Charge répartie partielle '+str(len(liste_charges)+1),[ "[q = ", tabl_c_répartie_partielle[nbr-1].q , " ; c1 = ", tabl_c_répartie_partielle[nbr-1].a , " ; l = ", tabl_c_répartie_partielle[nbr-1].l, "]"]])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_rep_1.focus()
                saisie_force_rep_1.select_range(0,END)
            if q==0 or I==0 or c1==0 or q=='' or I=='' or c1=='':
                showerror('Erreur', 'Un champ de coordonnées est vide.')
        elif str(chargement3.get()) == 'Charge triangulaire croissante' :
            q = float(saisie_force_rep_1.get())
            if q!='' and q!=0.0:
                VarEcrase = classe.charge_croissante(q)
                tabl_c_crois.append(VarEcrase)
                nbr = classe.charge_croissante.nbr
                liste_charges.append(['Encastrement / Charge croissante '+str(len(liste_charges)+1),[ "[q = ", tabl_c_crois[nbr-1].q , "]"]])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_rep_1.focus()
                saisie_force_rep_1.select_range(0,END)
            if q==0 or q=='':
                showerror('Erreur', 'Un champ de coordonnées est vide.')       
        elif str(chargement3.get()) == 'Charge triangulaire décroissante' :
            q = float(saisie_force_rep_1.get())
            if q!='' and q!=0.0:
                VarEcrase = classe.charge_décroissante(q)
                tabl_c_décrois.append(VarEcrase)
                nbr = classe.charge_décroissante.nbr
                liste_charges.append(['Encastrement / Charge croissante '+str(len(liste_charges)+1),[ "[q = ", tabl_c_décrois[nbr-1].q , "]"]])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_rep_1.focus()
                saisie_force_rep_1.select_range(0,END)
            if q==0 or q=='':
                showerror('Erreur', 'Un champ de coordonnées est vide.')  
        elif str(chargement3.get()) == 'Moment' :
            M = float(saisie_moment.get())
            a1 = float(saisie_a1.get())
            if M!='' and a1!=''and M!= 0.0 and a1!= 0.0 :
                VarEcrase = classe.couple(M, a1)
                tabl_couple.append(VarEcrase)
                nbr = classe.couple.nbr
                liste_charges.append(['Appuis Simple / couple '+str(len(liste_charges)+1),[ "[M = ", tabl_couple[nbr-1].C , " ; a1 = ", tabl_couple[nbr-1].a ,"]"]])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_moment.focus()
                saisie_moment.select_range(0,END)
            if M==0 or a1==0 or M=='' or a1=='':
                showerror('Erreur', 'Un champ de coordonnées est vide.')          
def udapte_listbox_charge(index):    
    for i in Liste_listboxCharges:
        i.delete(index)
    if Liste_listboxCharges[0].size()!=len(liste_charges):
        for i in Liste_listboxCharges:
            i.insert(index,liste_charges[index][0]+" "+str(liste_charges[index][1]))
    Liste_listboxCharges[0].see(index)
def renommer_charge():
    if Liste_listboxCharges[2].curselection()!=():
        temp_nom_charges=simpledialog.askstring("Renommer ", 'Nouveau nom de la charges : "'+Liste_listboxCharges[0].get(Liste_listboxCharges[0].curselection()[0])+'" :')
        if temp_nom_charges!='':
            liste_charges[Liste_listboxCharges[0].curselection()[0]][0] = temp_nom_charges
            udapte_listbox_charge(Liste_listboxCharges[0].curselection()[0])
    else:
        showerror('Erreur', 'Aucune charge sélectionné.')
def supprimer_charge():
    if Liste_listboxCharges[0].curselection()!=():
        del liste_charges[Liste_listboxCharges[0].curselection()[0]]
        udapte_listbox_charge(Liste_listboxCharges[0].curselection()[0])
    else:
        showerror('Erreur', 'Aucune charge sélectionné.')
def a1_next(event): #fct pour passer à a1
    saisie_a1.focus()
    saisie_a1.select_range(0,END)
def I_next(event): #fct pour passer à I
    saisie_I.focus()
    saisie_I.select_range(0,END)
def c1_next(event): #fct pour passer à c1
    saisie_c1.focus()
    saisie_c1.select_range(0,END)
# Passage d'une combobox à l'autre   
canva_tab3_labelframe1_Combobox1.bind("<<ComboboxSelected>>", ajout_combobox_chargement)      
"""
Fin
"""

### left_canvas_2 ###
### Fonction vérif conditions de la rdm ###
def verification_hypotheses_de_la_rdm_section_rectangulaire(): 
    #Vérifie le rapport de x4 pour la géométrie
    if (valeurs_geometriques[0])/(valeurs_geometriques[1])<=4:
        showwarning(title="ATTENTION", message="Le calcul va se faire mais les conditions de la RDM ne sont pas respectés \n Pour plus d'informations, rendez vous dans la rubrique Autres / Conditions de fonctionnement")

def calcul(): # Effectue le calcul sur le bouton calcul
    # [L,b,b1,b2,h,h1,R,R1,D1,D2] = valeurs_geometriques
    global tabl_c_concentrée, tabl_c_répartie, tabl_c_répartie_partielle, tabl_c_triang, tabl_c_triangulaire_mon, \
    tabl_c_triangulaire_antisy, tabl_c_trapézoïdale_sy, tabl_c_parabolique, tabl_couple, tabl_couple_réparti, tabl_c_décrois, tabl_c_crois
    if str(chargement.get()) == '2 appuis simples' :
        if len(tabl_c_concentrée) != 0:
            Appuis_simples.charge_concentrée()
            print(tabl_c_concentrée[0].P, tabl_c_concentrée[0].a)
        if len(tabl_c_répartie) != 0:
            print(tabl_c_répartie)
        if len(tabl_c_répartie_partielle) != 0:
            print(tabl_c_répartie_partielle)
        if len(tabl_c_triang) != 0:
            print(tabl_c_triang)
        if len(tabl_c_triangulaire_mon) != 0:
            print(tabl_c_triangulaire_mon)
        if len(tabl_c_triangulaire_antisy) != 0:
            print(tabl_c_triangulaire_antisy)
        if len(tabl_c_trapézoïdale_sy) != 0:
            print(tabl_c_trapézoïdale_sy)
        if len(tabl_c_parabolique) != 0:
            print(tabl_c_parabolique)
        if len(tabl_couple) != 0:
            print(tabl_couple)
        if len(tabl_couple_réparti) != 0:
            print(tabl_couple_réparti)
    elif str(chargement.get()) == '1 encastrement et 1 bord libre' : 
        if len(tabl_c_concentrée) != 0:
            
            print(tabl_c_concentrée[0].P, tabl_c_concentrée[0].a)
        if len(tabl_c_répartie) != 0:
            print(tabl_c_répartie)
        if len(tabl_c_crois) != 0:
            print(tabl_c_crois)
        if len(tabl_couple) != 0:
            print(tabl_couple)
"""
    #Vérifier si les conditions de la RDM sont respectées
    if valeurs_geometriques[0] != None and valeurs_geometriques[1] != None :
        verification_hypotheses_de_la_rdm_section_rectangulaire()
on travaille sur la copie d'une liste : 
--> 1 CAS : s'il n'y a qu'une seule charge, on distingue la quelle c'est, on lance le calcul et on lance la fonction tracer le graphe
--> 2 CAS : s'il y a plus de 2 charges, on fait un while pour faie les calculs de chacunes de ces sous listes, on suprime leurs traces \ 
    et quand la liste copie des charges est finalement vide, on les additonnes par principe de superposition et on lance la fct lancer_graph
"""



    # valeurs_geometriques=[geometrie.get(),geometrie2à7.get(),L,b,b1,b2,h,h1,R,R1,D1,D2]
    # valeurs_materiau = [E,Mv,m,Re,nu]
    # liste_charges_bis=[]
    # liste_charges=liste_charges_bis 
    # if len(liste_charges_bis) == 1 : # 1 CAS : la liste à 1
    #     [p,q,a1,c1,I,M] = liste_charges_bis[0][2]
    #     # plusieurs auquel cas il y a des sous listes et il faut les distingé dans le prochains cas
    #     if liste_charges_bis[0][0]=='2 appuis simples':
    #         if liste_charges_bis[0][1]=="Charge concentrée":  
    #             # le calcul de Clara et Agnès
    #               plotun, plotdeux = CalculerPortique(liste_noeuds, liste_poutres)
    #             # lancer_le_graph()
    #         if liste_charges[0][1]=="Charge uniformément répartie":
                
    #         if liste_charges_bis[0][1]=="Charge uniformément répartie partielle":   
                
    #         if liste_charges_bis[0][1]=="Charge triangulaire":
                
    #         if liste_charges_bis[0][1]=="Charge triangulaire monotone":
                
    #         if liste_charges_bis[0][1]=="Charge triangulaire antisymétrique": 
                
    #         if liste_charges_bis[0][1]=="Charge trapézoïdale":
                
    #         if liste_charges_bis[0][1]=="Charge parabolique":
                
    #         if liste_charges_bis[0][1]=="Moment":
                
    #         if liste_charges_bis[0][1]=="Moment uniformément réparti":
                
    #     if liste_charges_bis[0][1]=='1 encastrement et 1 bord libre':
    #         if liste_charges_bis[0][1]=="Charge concentrée":
                
    #         if liste_charges_bis[0][1]=="Charge uniformément répartie":                
                
    #         if liste_charges_bis[0][1]=="Charge uniformément répartie partielle":           
                
    #         if liste_charges_bis[0][1]=="Charge triangulaire croissante":                  
                
    #         if liste_charges_bis[0][1]=="Charge triangulaire décroissante":
                
    #         if liste_charges_bis[0][1]=="Moment":
                    
        # elif len(liste_charges_bis) > 1 :
        # donothing() 
    
    
    #     while liste_charges_bis != [] :
    #         if liste_charges_bis[i][0]=='2 appuis simples':
    #             if liste_charges_bis[i][1]=="Charge concentrée":
    #                 # ajout de la charge au calcul par principe de superposition 
    #                 del liste_charges_bis[i]
    #             if liste_charges_bis[i][1]=="Charge uniformément répartie":
                    
    #             if liste_charges_bis[i][1]=="Charge uniformément répartie partielle":     
                    
    #             if liste_charges_bis[i][1]=="Charge triangulaire":
                    
    #             if liste_charges_bis[i][1]=="Charge triangulaire monotone":
                    
    #             if liste_charges_bis[i][1]=="Charge triangulaire antisymétrique":   
                    
    #             if liste_charges_bis[i][1]=="Charge trapézoïdale":
                    
    #             if liste_charges_bis[i][1]=="Charge parabolique":
                    
    #             if liste_charges_bis[i][1]=="Moment":
                    
    #             if liste_charges_bis[i][1]=="Moment uniformément réparti":
                    
    #         if liste_charges_bis[i][1]=='1 encastrement et 1 bord libre':
    #             if liste_charges_bis[i][1]=="Charge concentrée":
                    
    #             if liste_charges_bis[i][1]=="Charge uniformément répartie":       
                    
    #             if liste_charges_bis[i][1]=="Charge uniformément répartie partielle":     
                    
    #             if liste_charges_bis[i][1]=="Charge triangulaire croissante":             
                    
    #             if liste_charges_bis[i][1]=="Charge triangulaire décroissante":
                    
    #             if liste_charges_bis[i][1]=="Moment":
    #     lancer_le_graph()
    #   else :
    #     showerror(title='ERREUR',message='Aucune force n'a été ajoutée.')    
                    
### Lancer le Graphique ###
def lancer_le_graph():
    donothing()
# matplotlib.use('TkAgg')
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure
# f = Figure(figsize=(16, 9), dpi=80)
# a = f.add_subplot(111)
# for i in plotun:
#     a.plot(i[0],i[1],'-.', c="red", marker='o')
# for j in plotdeux:
#     a.plot(j[0],j[1])
# a.set_xlabel('x')
# a.set_ylabel('y')

# graph = FigureCanvasTkAgg(f, master=canvasgraph)
# graph.get_tk_widget().grid(row = 0)
# canvas._tkcanvas.grid(row = 0)
# canvasgraph.pack(side=CENTER)
# canva_tab5.add(canvasgraph)

# Bouton Calculer #
bouton_calculer= Button(left_canvas2, text="Calculer",textvariable="Re-Calculer",relief="raised",overrelief="groove", font=("Tahoma", 20,"bold"), bg=gris_3, fg ="white", command=calcul)
bouton_calculer.place(relx=0.5,rely=0.5,relwidth=0.5, relheight=0.5,anchor='center') # afficher le bouton
"""
Fin
"""

### right frame ###
### NoteBook - right_canvas1 ###
notebook2 = ttk.Notebook(right_frame, style='TNotebook') # Creation du Notebook
notebook2.enable_traversal() # permet de swtich avec le clavier d'un tab à l'autre [Ctl+tab,Ctrl+shift+tab,Alt+K]
notebook2.pack(expand=1, fill='both') # on place le notebook
"""
Fin
"""

### Barre 1 : Schémas ###
tab4 = ttk.Frame(notebook2, style='TFrame') # Creation de la barre 4
img4 = PhotoImage(file='images/picture.png')
notebook2.add(tab4, text='Schémas',image=img4, compound=LEFT) # Ajout de la barre 1 au notebook
canva_tab4 = Canvas(tab4, bg="white")
canva_tab4.place(relx=0.003,rely=0.003,relwidth=0.995, relheight=0.995)
"""
Fin
"""

### Barre 2 : Graphiques Globaux ###
tab5 = ttk.Frame(notebook2, style='TFrame') # Creation de la barre 5
img5 = PhotoImage(file='images/statistics.png')
notebook2.add(tab5, text='Graphiques Globaux',image=img5, compound=LEFT) # Ajout de la barre 1 au notebook
canva_tab5 = Canvas(tab5, bg="blue")
canva_tab5.place(relx=0.003,rely=0.003,relwidth=0.995, relheight=0.995)

"""
Fin
"""

### Barre 3 : Graphiques détaillés ###
tab6 = ttk.Frame(notebook2, style='TFrame') # Creation de la barre 6
img6 = PhotoImage(file='images/analysis (1).png')
notebook2.add(tab6, text='Graphiques détaillés',image=img6, compound=LEFT) # Ajout de la barre 1 au notebook
canva_tab6 = Canvas(tab6, bg="green")
canva_tab6.place(relx=0.003,rely=0.003,relwidth=0.995, relheight=0.995)
"""
Fin
"""

### Barre 4 : Analyse ###
tab7 = ttk.Frame(notebook2, style='TFrame') # Creation de la barre 7
img7 = PhotoImage(file='images/analysis.png')
notebook2.add(tab7, text='Analyse',image=img7, compound=LEFT) # Ajout de la barre 1 au notebook
canva_tab7 = Canvas(tab7, bg="red")
canva_tab7.place(relx=0.003,rely=0.003,relwidth=0.995, relheight=0.995)
"""
Fin
"""

### Lancement du rendu général ###
# Fenetre de bienvenue #
# fenetre_bienvenue()
#lancer le main
main.mainloop()
"""
Fin
"""