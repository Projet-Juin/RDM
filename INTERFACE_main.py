# -*- coding: utf-8 -*-
"""
@author: Forjot Henri et Ferru Clara 

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
main.title("Solve Structure V1.0 --- Écran principal") #Titre de l'encadré
main.config(bg=gris_7)
main.call('wm', 'iconphoto', main._w, PhotoImage(file='images/petitlogo.png'))
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
fichier_menu.add_command(label='Ouvrir',command=ouvrir,state=DISABLED) # ajout de l'item ouvrir
fichier_menu.add_command(label='Sauvegarder            (Ctrl+S)',command=sauvegarder,state=DISABLED) # ajout de l'item sauvegarder
fichier_menu.add_command(label='Sauvegarder Sous   (Shift+Ctrl+S)',command=sauvegarder_sous,state=DISABLED) # ajout de l'item sauvegarder sous
fichier_menu.add_command(label='Redémarrer',command=reboot_programme) # ajout de l'item redémarrer
fichier_menu.add_separator() #ajout d'un separateur
fichier_menu.add_command(label='Quitter',command=main.destroy) # ajout de l'item quitter (ou sys.exit)
# Création d'un menu éléments finis et ajout d'items
elts_finis_menu = Menu(barre_de_menu,activebackground=gris_5, tearoff=0) # Création d'un menu élts finis
elts_finis_menu.add_command(label='Switch vers Éléments finis',command=switch_elts_finis,state=DISABLED) # ajout de l'item permettant d'aller en élément finis
elts_finis_menu.add_separator() #ajout d'un separateur
elts_finis_menu.add_command(label='Importer les Inputs d\'Éléments finis',command=import_elts_finis,state=DISABLED) # ajout de l'item permettant d'importer les données d'éléments finis
elts_finis_menu.add_command(label='Exporter les Inputs d\'Éléments finis',command=export_elts_finis,state=DISABLED) # ajout de l'item permettant d'exporter les données d'éléments finis
# Création d'un menu autres et ajout d'items
autres_menu = Menu(barre_de_menu,activebackground=gris_5, tearoff=0) # Création d'un menu autres
autres_menu.add_command(label='Aide',command=aide) # ajout de l'item aide
autres_menu.add_command(label='Conditions de fonctionnement',command=ctds_de_fct) # ajout de l'item conditions de la rdm
autres_menu.add_separator() #ajout d'un separateur
autres_menu.add_command(label='Crédits',command=credit) # ajout de l'item crédit
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
img_charge_rep_part_proche = PhotoImage(file='images/charge partiellement répartie appuis simples proche des appuis.PNG')
img_charge_rep_part_proche_encast = PhotoImage(file='images/charge partiellement répartie encastrement proche des appuis.PNG')
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
left_canvas1.place(relx=0,rely=0,relwidth=1, relheight=0.92)
left_canvas2.place(relx=0,rely=0.92,relwidth=1, relheight=0.1)
"""
Fin
"""

### NoteBook - left_canvas1 ###
notebook = ttk.Notebook(left_canvas1, style='TNotebook') # Creation du Notebook
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
canva_tab1_labelframe1.place(relx=0.01,rely=0.01,relwidth=0.98, relheight=0.16) # affiche le labelframe type de section    
# Choisir quelle est la géométrie du problème
canva_tab1_labelframe1_label = Label(canva_tab1_labelframe1,text = "Choisissez le type de géométrie de votre poutre :",bg=gris_5,font = ("Arial",10,"bold"))
canva_tab1_labelframe1_label.place(relx=0.01,rely=0.02,relwidth=0.98, relheight=0.25)
geometrie = StringVar()
canva_tab1_labelframe1_Combobox1 = ttk.Combobox(canva_tab1_labelframe1, textvariable = geometrie , state = "readonly",justify='center')
canva_tab1_labelframe1_Combobox1['values'] = ["","Rectangle", "Carré", "Forme", "Triangle", "Cercle", "Losange"]
canva_tab1_labelframe1_Combobox1.place(relx=0.01,rely=0.35,relwidth=0.98, relheight=0.28) # affichage de la combobox
canva_tab1_labelframe1_Combobox1.current(0) # onglet actif dans la combobox quand on démarre 
def ajout_combobox(event):
    global geometrie2,geometrie3,geometrie4,geometrie5,geometrie6,geometrie7,\
        canva_tab1_labelframe1_Combobox2,canva_tab1_labelframe1_Combobox3,canva_tab1_labelframe1_Combobox4,\
            canva_tab1_labelframe1_Combobox5,canva_tab1_labelframe1_Combobox6,canva_tab1_labelframe1_Combobox7
    print("Sélection en cours du Combobox 1 :  index <",canva_tab1_labelframe1_Combobox1.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox1.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
    if str(geometrie.get()) == 'Rectangle':
        geometrie2 = StringVar()
        canva_tab1_labelframe1_Combobox2 = ttk.Combobox(canva_tab1_labelframe1, textvariable = geometrie2 , state = "readonly",justify='center')
        canva_tab1_labelframe1_Combobox2['values'] = ["","Normal","Creux"]
        canva_tab1_labelframe1_Combobox2.place(relx=0.01,rely=0.66,relwidth=0.98, relheight=0.28) # affichage de la combobox
        canva_tab1_labelframe1_Combobox2.current(0) # onglet actif dans la combobox quand on démarre
        # Passage d'une combobox à l'autre   
        canva_tab1_labelframe1_Combobox2.bind("<<ComboboxSelected>>", nouveau_labelframe)
    if str(geometrie.get()) == 'Carré':
        geometrie3 = StringVar()
        canva_tab1_labelframe1_Combobox3 = ttk.Combobox(canva_tab1_labelframe1, textvariable = geometrie3 , state = "readonly",justify='center')
        canva_tab1_labelframe1_Combobox3['values'] = ["","Normal","Creux"]
        canva_tab1_labelframe1_Combobox3.place(relx=0.01,rely=0.66,relwidth=0.98, relheight=0.28) # affichage de la combobox
        canva_tab1_labelframe1_Combobox3.current(0) # onglet actif dans la combobox quand on démarre
        # Passage d'une combobox à l'autre   
        canva_tab1_labelframe1_Combobox3.bind("<<ComboboxSelected>>", nouveau_labelframe) 
    if str(geometrie.get()) == 'Forme':
        geometrie4 = StringVar()
        canva_tab1_labelframe1_Combobox4 = ttk.Combobox(canva_tab1_labelframe1, textvariable = geometrie4 , state = "readonly",justify='center')
        canva_tab1_labelframe1_Combobox4['values'] = ["","I","Z","Croix"]
        canva_tab1_labelframe1_Combobox4.place(relx=0.01,rely=0.66,relwidth=0.98, relheight=0.28) # affichage de la combobox
        canva_tab1_labelframe1_Combobox4.current(0) # onglet actif dans la combobox quand on démarre
        # Passage d'une combobox à l'autre   
        canva_tab1_labelframe1_Combobox4.bind("<<ComboboxSelected>>", nouveau_labelframe)
    if str(geometrie.get()) == 'Triangle':
        geometrie5 = StringVar()
        canva_tab1_labelframe1_Combobox5 = ttk.Combobox(canva_tab1_labelframe1, textvariable = geometrie5 , state = "readonly",justify='center')
        canva_tab1_labelframe1_Combobox5['values'] = ["","Rectangle"]
        canva_tab1_labelframe1_Combobox5.place(relx=0.01,rely=0.66,relwidth=0.98, relheight=0.28) # affichage de la combobox
        canva_tab1_labelframe1_Combobox5.current(0) # onglet actif dans la combobox quand on démarre
        # Passage d'une combobox à l'autre   
        canva_tab1_labelframe1_Combobox5.bind("<<ComboboxSelected>>", nouveau_labelframe)
    if str(geometrie.get()) == 'Cercle':
        geometrie6 = StringVar()
        canva_tab1_labelframe1_Combobox6 = ttk.Combobox(canva_tab1_labelframe1, textvariable = geometrie6 , state = "readonly",justify='center')
        canva_tab1_labelframe1_Combobox6['values'] = ["","Normal","Creux","Demi Cercle","Quart de Cercle","Ovale"]
        canva_tab1_labelframe1_Combobox6.place(relx=0.01,rely=0.66,relwidth=0.98, relheight=0.28) # affichage de la combobox
        canva_tab1_labelframe1_Combobox6.current(0) # onglet actif dans la combobox quand on démarre
        # Passage d'une combobox à l'autre   
        canva_tab1_labelframe1_Combobox6.bind("<<ComboboxSelected>>", nouveau_labelframe)
    if str(geometrie.get()) == 'Losange': 
        geometrie7 = StringVar()
        canva_tab1_labelframe1_Combobox7 = ttk.Combobox(canva_tab1_labelframe1, textvariable = geometrie7 , state = "readonly",justify='center')
        canva_tab1_labelframe1_Combobox7['values'] = ["","Normal"]
        canva_tab1_labelframe1_Combobox7.place(relx=0.01,rely=0.66,relwidth=0.98, relheight=0.28) # affichage de la combobox
        canva_tab1_labelframe1_Combobox7.current(0) # onglet actif dans la combobox quand on démarre
        # Passage d'une combobox à l'autre   
        canva_tab1_labelframe1_Combobox7.bind("<<ComboboxSelected>>", nouveau_labelframe)
def nouveau_labelframe(event): # nouvelle frame où on rentre les données
    global label_longueur,label_largeur,label_largeur1,label_largeur2,label_rayon,label_rayon1\
        ,label_hauteur,label_hauteur1,label_diagonale1,label_diagonale2\
            ,saisie_longueur,saisie_largeur, saisie_largeur1 , saisie_largeur2 ,saisie_rayon,saisie_rayon1\
                ,saisie_hauteur,saisie_hauteur1,saisie_diagonale1,saisie_diagonale2\
                    ,canva_tab1_labelframe2,valeurs_geometriques, canva_tab4
    # Création labelframe 2
    canva_tab1_labelframe2 = LabelFrame(canva_tab1,font = ("Arial",14 , "bold"),text = 'Données',bg = gris_5) #définit le message 2
    canva_tab1_labelframe2.place(relx=0.01,rely=0.17,relwidth=0.98, relheight=0.74) # affiche le labelframe type de section   
    # Bouton pour valider l'entrée des données de géométrie pour rassurer l'utilisateur
    Button(canva_tab1,relief="raised",overrelief="groove", text='Valider la géométrie', font=("Tahoma", 14,"bold"), command=valider_la_géométrie, bg=gris_3,fg ="white").place(relx=0.01,rely=0.92,relwidth=0.98, relheight=0.07) # affiche le bouton valider  
    if str(geometrie.get()) == 'Rectangle':
        if str(geometrie2.get()) == 'Normal':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Longueur L de votre poutre en mm :',bg=gris_5)
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Largeur b de votre poutre en mm :',bg=gris_5)
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Hauteur h de votre poutre en mm :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_geo_rectangle)
            labelimg.image = img_geo_rectangle
            labelimg.pack(fill=BOTH, expand=1)
            # lancement retour des touches
            saisie_longueur.bind('<Return>',largeur_next)
            saisie_largeur.bind('<Return>',hauteur_next)
            saisie_hauteur.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 2 :  index <",canva_tab1_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(geometrie2.get()) == 'Creux':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Longueur L de votre poutre en mm :',bg=gris_5)
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Largeur b de votre poutre en mm :',bg=gris_5)
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Hauteur h de votre poutre en mm :',bg=gris_5)
            label_largeur1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Largeur b1 de votre poutre en mm :',bg=gris_5)
            label_hauteur1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Hauteur h1 de votre poutre en mm :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_geo_rectangle_t)
            labelimg.image = img_geo_rectangle_t
            labelimg.pack(fill=BOTH, expand=1)
            # canva_tab4.create_image(700,500, image=img_geo_rectangle_t)
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
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Longueur L de votre poutre en mm :',bg=gris_5)
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Largeur b de votre poutre en mm :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_geo_carre)
            labelimg.image = img_geo_carre
            labelimg.pack(fill=BOTH, expand=1)
            # lancement retour des touches
            saisie_longueur.bind('<Return>',largeur_next)
            saisie_largeur.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 3 :  index <",canva_tab1_labelframe1_Combobox3.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox3.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(geometrie3.get()) == 'Creux':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Longueur L de votre poutre en mm :',bg=gris_5)
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Largeur b de votre poutre en mm :',bg=gris_5)
            label_largeur1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Largeur b1 de votre poutre en mm :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_geo_carre_t)
            labelimg.image = img_geo_carre_t
            labelimg.pack(fill=BOTH, expand=1)
            # lancement retour des touches
            saisie_longueur.bind('<Return>',largeur_next)
            saisie_largeur.bind('<Return>',largeur1_next)
            saisie_largeur1.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 3 :  index <",canva_tab1_labelframe1_Combobox3.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox3.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
    if str(geometrie.get()) == 'Forme':
        if str(geometrie4.get()) == 'I':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Longueur L de votre poutre en mm :',bg=gris_5)
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Largeur b de votre poutre en mm :',bg=gris_5)
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Hauteur h de votre poutre en mm :',bg=gris_5)
            label_largeur1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Largeur de l’aile supérieure b1 de votre poutre \nen mm :',bg=gris_5)
            label_largeur2 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Largeur de l’aile inférieure b2 de votre poutre \nen mm :',bg=gris_5)
            label_hauteur1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Hauteur du tronc h1 de votre poutre en mm :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_geo_forme_i)
            labelimg.image = img_geo_forme_i
            labelimg.pack(fill=BOTH, expand=1)                     
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
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Longueur L de votre poutre en mm :',bg=gris_5)
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Largeur b de votre poutre en mm :',bg=gris_5)
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Hauteur h de votre poutre en mm :',bg=gris_5)
            label_largeur1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Largeur de l’aile b1 de votre poutre en mm :',bg=gris_5)
            label_hauteur1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Hauteur du tronc h1 de votre poutre en mm :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_geo_forme_t)
            labelimg.image = img_geo_forme_t
            labelimg.pack(fill=BOTH, expand=1) 
            # lancement retour des touches
            saisie_longueur.bind('<Return>',largeur_next)
            saisie_largeur.bind('<Return>',hauteur_next)
            saisie_hauteur.bind('<Return>',largeur1_next)
            saisie_largeur1.bind('<Return>',hauteur1_next)
            saisie_hauteur1.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 4 :  index <",canva_tab1_labelframe1_Combobox4.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox4.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(geometrie4.get()) == 'L':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Longueur L de votre poutre en mm :',bg=gris_5)
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Largeur b de votre poutre en mm :',bg=gris_5)
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Hauteur h de votre poutre en mm :',bg=gris_5)
            label_largeur1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Largeur de l’aile b1 de votre poutre en mm :',bg=gris_5)
            label_hauteur1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Hauteur du tronc h1 de votre poutre en mm :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_geo_forme_l)
            labelimg.image = img_geo_forme_l
            labelimg.pack(fill=BOTH, expand=1) 
            # lancement retour des touches
            saisie_longueur.bind('<Return>',largeur_next)
            saisie_largeur.bind('<Return>',hauteur_next)
            saisie_hauteur.bind('<Return>',largeur1_next)
            saisie_largeur1.bind('<Return>',hauteur1_next)
            saisie_hauteur1.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 4 :  index <",canva_tab1_labelframe1_Combobox4.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox4.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(geometrie4.get()) == 'Z':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Longueur L de votre poutre en mm :',bg=gris_5)
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Largeur b de votre poutre en mm :',bg=gris_5)
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Hauteur h de votre poutre en mm :',bg=gris_5)
            label_largeur1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Largeur de l’aile b1 de votre poutre en mm :',bg=gris_5)
            label_largeur2 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Largeur de l’aile inférieure b2 de votre poutre \nen mm :',bg=gris_5)
            label_hauteur1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Hauteur du tronc h1 de votre poutre en mm :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_geo_forme_z)
            labelimg.image = img_geo_forme_z
            labelimg.pack(fill=BOTH, expand=1) 
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
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Longueur L de votre poutre en mm :',bg=gris_5)
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Largeur b de votre poutre en mm :',bg=gris_5)
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Hauteur h de votre poutre en mm :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_geo_forme_croix)
            labelimg.image = img_geo_forme_croix
            labelimg.pack(fill=BOTH, expand=1)         
            # lancement retour des touches            
            saisie_longueur.bind('<Return>',largeur_next)
            saisie_largeur.bind('<Return>',hauteur_next)
            saisie_hauteur.bind('<Return>',valider_la_géométrie_auto) 
            print("Sélection en cours du Combobox 4 :  index <",canva_tab1_labelframe1_Combobox4.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox4.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
    if str(geometrie.get()) == 'Triangle':
        if str(geometrie5.get()) == 'Rectangle':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Longueur L de votre poutre en mm :',bg=gris_5)
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Largeur b de votre poutre en mm :',bg=gris_5)
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Hauteur h de votre poutre en mm :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_geo_triangle_rec)
            labelimg.image = img_geo_triangle_rec
            labelimg.pack(fill=BOTH, expand=1)            
            # lancement retour des touches
            saisie_longueur.bind('<Return>',largeur_next)
            saisie_largeur.bind('<Return>',hauteur_next)
            saisie_hauteur.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 5 :  index <",canva_tab1_labelframe1_Combobox5.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox5.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
    if str(geometrie.get()) == 'Cercle':
        if str(geometrie6.get()) == 'Normal':
            # messages des inputs L,R
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Longueur L de votre poutre en mm :',bg=gris_5)
            label_rayon = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez le Rayon R de votre poutre en mm :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_geo_cercle)
            labelimg.image = img_geo_cercle
            labelimg.pack(fill=BOTH, expand=1)    
            # lancement retour des touches
            saisie_longueur.bind('<Return>',rayon_next)
            saisie_rayon.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 6 :  index <",canva_tab1_labelframe1_Combobox6.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox6.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(geometrie6.get()) == 'Creux':
            # messages des inputs L,R
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Longueur L de votre poutre en mm :',bg=gris_5)
            label_rayon = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez le Rayon R de votre poutre en mm :',bg=gris_5)
            label_rayon1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez le Rayon R1 de votre poutre en mm :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_geo_cercle_t)
            labelimg.image = img_geo_cercle_t
            labelimg.pack(fill=BOTH, expand=1)    
            # lancement retour des touches
            saisie_longueur.bind('<Return>',rayon_next)
            saisie_rayon.bind('<Return>',rayon1_next)
            saisie_rayon1.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 6 :  index <",canva_tab1_labelframe1_Combobox6.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox6.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(geometrie6.get()) == 'Demi Cercle':
            # messages des inputs L,R
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Longueur L de votre poutre en mm :',bg=gris_5)
            label_rayon = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez le Rayon R de votre poutre en mm :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_geo_demi_cercle)
            labelimg.image = img_geo_demi_cercle
            labelimg.pack(fill=BOTH, expand=1)    
            # lancement retour des touches
            saisie_longueur.bind('<Return>',rayon_next)
            saisie_rayon.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 6 :  index <",canva_tab1_labelframe1_Combobox6.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox6.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(geometrie6.get()) == 'Quart de Cercle':
            # messages des inputs L,R
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Longueur L de votre poutre en mm :',bg=gris_5)
            label_rayon = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez le Rayon R de votre poutre en mm :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_geo_quart_de_cercle)
            labelimg.image = img_geo_quart_de_cercle
            labelimg.pack(fill=BOTH, expand=1)    
            # lancement retour des touches
            saisie_longueur.bind('<Return>',rayon_next)
            saisie_rayon.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 6 :  index <",canva_tab1_labelframe1_Combobox6.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox6.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(geometrie6.get()) == 'Ovale':
            # messages des inputs L,R
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Longueur L de votre poutre en mm :',bg=gris_5)
            label_diagonale1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la grande diagonale D1 de votre poutre \nen mm :',bg=gris_5)
            label_diagonale2 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la petite diagonale D2 de votre poutre \nen mm :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_geo_ovale)
            labelimg.image = img_geo_ovale
            labelimg.pack(fill=BOTH, expand=1)          
            # lancement retour des touches
            saisie_longueur.bind('<Return>',diagonale1_next)
            saisie_diagonale1.bind('<Return>',diagonale2_next)
            saisie_diagonale2.bind('<Return>',valider_la_géométrie_auto)
            print("Sélection en cours du Combobox 6 :  index <",canva_tab1_labelframe1_Combobox6.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox6.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
    if str(geometrie.get()) == 'Losange':
        if str(geometrie7.get()) == 'Normal':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Longueur L de votre poutre en mm :',bg=gris_5)
            label_diagonale1 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la grande diagonale D1 de votre \npoutre en mm :',bg=gris_5)
            label_diagonale2 = Label(canva_tab1_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la petite diagonale D2 de votre \npoutre en mm :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_geo_losange)
            labelimg.image = img_geo_losange
            labelimg.pack(fill=BOTH, expand=1)           
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
                    ,canva_tab1_labelframe2,valeurs_geometriques , L, b, h, b1, b2, h, h1, R, R1, D1, D2,géométrie_poutre
    if str(geometrie.get()) == 'Rectangle':  
        L = float(saisie_longueur.get())
        if str(geometrie2.get()) == 'Normal':
            b = float(saisie_largeur.get())
            h = float(saisie_hauteur.get())
            if L!='' and b!='' and h!='' and L!=0.0 and b!=0.0 and h!=0.0 :
                [Igz, L, h, volume] = géométrie_poutre.rectangle(L, b, h)
                valeurs_geometriques = [Igz, L, h, volume]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or h==0 or L=='' or b=='' or h=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Igz calculé = ", valeurs_geometriques[0], "L = ", valeurs_geometriques[1], "hauteur = ", valeurs_geometriques[2], "volume = ", valeurs_geometriques[3])
        if str(geometrie2.get()) == 'Creux':
            L = float(saisie_longueur.get())
            b = float(saisie_largeur.get())
            b1 = float(saisie_largeur1.get())
            h = float(saisie_hauteur.get())    
            h1 = float(saisie_hauteur1.get())
            if L!='' and b!='' and b1!='' and h!='' and h1!='' and L!=0.0 and b!=0.0 and b1!=0.0 and h!=0.0 and h1!=0.0 :
                [Igz, L, h, volume] = géométrie_poutre.rectangle_creux(L, b, h, b1, h1) 
                valeurs_geometriques = [Igz, L, h, volume]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or b1==0 or h==0 or h1==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or b1=='' or h=='' or h1=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Igz calculé = ", valeurs_geometriques[0], "L = ", valeurs_geometriques[1], "hauteur = ", valeurs_geometriques[2], "volume = ", valeurs_geometriques[3])
    if str(geometrie.get()) == 'Carré':
        if str(geometrie3.get()) == 'Normal':
            L = float(saisie_longueur.get())
            b = float(saisie_largeur.get())            
            if L!='' and b!='' and L!=0.0 and b!=0.0:
                [Igz, L, h, volume] = géométrie_poutre.carré(L, b)
                valeurs_geometriques = [Igz, L, h, volume]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Igz calculé = ", valeurs_geometriques[0], "L = ", valeurs_geometriques[1], "hauteur = ", valeurs_geometriques[2], "volume = ", valeurs_geometriques[3])
        if str(geometrie3.get()) == 'Creux':
            L = float(saisie_longueur.get())
            b = float(saisie_largeur.get())
            b1 = float(saisie_largeur1.get())            
            if L!='' and b!='' and b1!='' and L!=0.0 and b!=0.0 and b1!=0.0 :
                [Igz, L, h, volume] = géométrie_poutre.carré_creux(L, b, b1)
                valeurs_geometriques = [Igz, L, h, volume]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or b1==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or b1=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Igz calculé = ", valeurs_geometriques[0], "L = ", valeurs_geometriques[1], "hauteur = ", valeurs_geometriques[2], "volume = ", valeurs_geometriques[3])            
    if str(geometrie.get()) == 'Forme':
        if str(geometrie4.get()) == 'I':
            L = float(saisie_longueur.get())
            b = float(saisie_largeur.get())
            b1 = float(saisie_largeur1.get())
            b2 = float(saisie_largeur2.get())
            h = float(saisie_hauteur.get())
            h1 = float(saisie_hauteur1.get())
            if L!='' and b!='' and b1!='' and h!='' and h1!='' and b2!='' and L!=0.0 and b!=0.0 and b1!=0.0 and h!=0.0 and h1!=0.0 and b2!=0.0:
                [Igz, L, h, volume] = géométrie_poutre.I(L, b, h, b1, b2, h1) 
                valeurs_geometriques = [Igz, L, h, volume]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or b1==0 or h==0 or h1==0 or b2==0:
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or b1=='' or h=='' or h1=='' or b2=='':
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Igz calculé = ", valeurs_geometriques[0], "L = ", valeurs_geometriques[1], "hauteur = ", valeurs_geometriques[2], "volume = ", valeurs_geometriques[3])
        if str(geometrie4.get()) == 'T':
            L = float(saisie_longueur.get())
            b = float(saisie_largeur.get())
            b1 = float(saisie_largeur1.get())
            h = float(saisie_hauteur.get())
            h1 = float(saisie_hauteur1.get())            
            if L!='' and b!='' and b1!='' and h!='' and h1!='' and L!=0.0 and b!=0.0 and b1!=0.0 and h!=0.0 and h1!=0.0 :
                [Igz, L, h, volume] = géométrie_poutre.T(L, b, h, b1, h1)
                valeurs_geometriques = [Igz, L, h, volume]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or b1==0 or h==0 or h1==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or b1=='' or h=='' or h1=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Igz calculé = ", valeurs_geometriques[0], "L = ", valeurs_geometriques[1], "hauteur = ", valeurs_geometriques[2], "volume = ", valeurs_geometriques[3])
        if str(geometrie4.get()) == 'L':
            L = float(saisie_longueur.get())
            b = float(saisie_largeur.get())
            b1 = float(saisie_largeur1.get())
            h = float(saisie_hauteur.get())
            h1 = float(saisie_hauteur1.get())
            if L!='' and b!='' and b1!='' and h!='' and h1!='' and L!=0.0 and b!=0.0 and b1!=0.0 and h!=0.0 and h1!=0.0:
                [Igz, L, h, volume] = géométrie_poutre.L(L, b, h, b1, h1)
                valeurs_geometriques = [Igz, L, h, volume]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or b1==0 or h==0 or h1==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or b1=='' or h=='' or h1=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Igz calculé = ", valeurs_geometriques[0], "L = ", valeurs_geometriques[1], "hauteur = ", valeurs_geometriques[2], "volume = ", valeurs_geometriques[3])
        if str(geometrie4.get()) == 'Z':
            L = float(saisie_longueur.get())
            b = float(saisie_largeur.get())
            b1 = float(saisie_largeur1.get())
            b2 = float(saisie_largeur2.get())
            h = float(saisie_hauteur.get())
            h1 = float(saisie_hauteur1.get())
            if L!='' and b!='' and b1!='' and h!='' and h1!='' and b2!=''and L!=0.0 and b!=0.0 and b1!=0.0 and h!=0.0 and h1!=0.0 and b2!=0.0:
                [Igz, L, h, volume] = géométrie_poutre.Z(L, b, h, b1, b2, h1)
                valeurs_geometriques = [Igz, L, h, volume]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or b1==0 or h==0 or h1==0 or b2==0:
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or b1=='' or h=='' or h1=='' or b2=='':
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Igz calculé = ", valeurs_geometriques[0], "L = ", valeurs_geometriques[1], "hauteur = ", valeurs_geometriques[2], "volume = ", valeurs_geometriques[3])
        if str(geometrie4.get()) == 'Croix':
            L = float(saisie_longueur.get())
            b = float(saisie_largeur.get())
            h = float(saisie_hauteur.get())
            if L!='' and b!='' and h!='' and L!=0.0 and b!=0.0 and h!=0.0 :
                [Igz, L, h, volume] = géométrie_poutre.croix(L, b, h)
                valeurs_geometriques = [Igz, L, h, volume]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or h==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or h=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Igz calculé = ", valeurs_geometriques[0], "L = ", valeurs_geometriques[1], "hauteur = ", valeurs_geometriques[2], "volume = ", valeurs_geometriques[3])
    if str(geometrie.get()) == 'Triangle':
        if str(geometrie5.get()) == 'Rectangle':
            L = float(saisie_longueur.get())
            b = float(saisie_largeur.get())
            h = float(saisie_hauteur.get())
            if L!='' and b!='' and h!='' and L!=0.0 and b!=0.0 and h!=0.0 :
                [Igz, L, h, volume] = géométrie_poutre.triangle_rectangle(L, b, h)
                valeurs_geometriques = [Igz, L, h, volume]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or h==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or h=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Igz calculé = ", valeurs_geometriques[0], "L = ", valeurs_geometriques[1], "hauteur = ", valeurs_geometriques[2], "volume = ", valeurs_geometriques[3])
    if str(geometrie.get()) == 'Cercle':
        if str(geometrie6.get()) == 'Normal':
            L = float(saisie_longueur.get())
            R = float(saisie_rayon.get())
            if L!='' and R!='' and L!=0.0 and R!=0.0 :
                [Igz, L, h, volume] = géométrie_poutre.cercle(L, R) 
                valeurs_geometriques = [Igz, L, h, volume]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or R==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or R=='':
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Igz calculé = ", valeurs_geometriques[0], "L = ", valeurs_geometriques[1], "hauteur = ", valeurs_geometriques[2], "volume = ", valeurs_geometriques[3])
        if str(geometrie6.get()) == 'Creux':
            L = float(saisie_longueur.get())
            R = float(saisie_rayon.get())
            R1 = float(saisie_rayon1.get())
            if L!='' and R!='' and R1!='' and L!=0.0 and R!=0.0 and R1!=0.0:
                [Igz, L, h, volume] = géométrie_poutre.cercle_creux(L, R, R1)
                valeurs_geometriques = [Igz, L, h, volume]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or R==0 or R1==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or R=='' or R1=='':
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Igz calculé = ", valeurs_geometriques[0], "L = ", valeurs_geometriques[1], "hauteur = ", valeurs_geometriques[2], "volume = ", valeurs_geometriques[3])
        if str(geometrie6.get()) == 'Demi Cercle':
            L = float(saisie_longueur.get())
            R = float(saisie_rayon.get())
            if L!='' and R!='' and L!=0.0 and R!=0.0 :
                [Igz, L, h, volume] = géométrie_poutre.demi_cercle(L, R)
                valeurs_geometriques = [Igz, L, h, volume]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or R==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or R=='':
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Igz calculé = ", valeurs_geometriques[0], "L = ", valeurs_geometriques[1], "hauteur = ", valeurs_geometriques[2], "volume = ", valeurs_geometriques[3])
        if str(geometrie6.get()) == 'Quart de Cercle':
            L = float(saisie_longueur.get())
            R = float(saisie_rayon.get())
            if L!='' and R!='' and L!=0.0 and R!=0.0 :
                [Igz, L, h, volume] = géométrie_poutre.quart_cercle(L, R)
                valeurs_geometriques = [Igz, L, h, volume]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or R==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or R=='':
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Igz calculé = ", valeurs_geometriques[0], "L = ", valeurs_geometriques[1], "hauteur = ", valeurs_geometriques[2], "volume = ", valeurs_geometriques[3])
        if str(geometrie6.get()) == 'Ovale':
            L = float(saisie_longueur.get())
            D1 = float(saisie_diagonale1.get())
            D2 = float(saisie_diagonale2.get())
            if L!='' and D1!='' and D2!='' and L!=0.0 and D1!=0.0 and D2!=0.0 :
                [Igz, L, h, volume] = géométrie_poutre.ovale(L, D2, D1)
                valeurs_geometriques = [Igz, L, h, volume]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or D1==0 or D2==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or D1=='' or D2=='':
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Igz calculé = ", valeurs_geometriques[0], "L = ", valeurs_geometriques[1], "hauteur = ", valeurs_geometriques[2], "volume = ", valeurs_geometriques[3])
    if str(geometrie.get()) == 'Losange':
        if str(geometrie7.get()) == 'Normal':
            L = float(saisie_longueur.get())
            D1 = float(saisie_diagonale1.get())
            D2 = float(saisie_diagonale2.get())
            if L!='' and D1!='' and D2!='' and L!=0.0 and D1!=0.0 and D2!=0.0 :
                [Igz, L, h, volume] = géométrie_poutre.losange(L, D2, D1) 
                valeurs_geometriques = [Igz, L, h, volume]
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or D1==0 or D2==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or D1=='' or D2=='':
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Igz calculé = ", valeurs_geometriques[0], "L = ", valeurs_geometriques[1], "hauteur = ", valeurs_geometriques[2], "volume = ", valeurs_geometriques[3])
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
def recreer_le_canva():
    global canva_tab4
    canva_tab4.destroy()
    canva_tab4 = Canvas(tab4, bg="white")
    canva_tab4.place(relx=0.003,rely=0.003,relwidth=0.995, relheight=0.995)
# Passage d'une combobox à l'autre   
canva_tab1_labelframe1_Combobox1.bind("<<ComboboxSelected>>", ajout_combobox)      
"""
Fin
"""

### Barre 2 : Matériau ###
tab2 = ttk.Frame(notebook) # Creation de la barre 1 de Notebook
# notebook.add(tab2, text='Matériau') # Ajout de la barre 1 au notebook
img2 = PhotoImage(file='images/program (1).png')
notebook.add(tab2,text='Matériau\n& Précision',image=img2, compound=LEFT) # Ajout de la barre 1 au notebook
canva_tab2=Canvas(tab2, bg=gris_5)
canva_tab2.pack(expand=1, fill='both')
#Création labelframe
canva_tab2_labelframe = LabelFrame(canva_tab2,font=("Arial",14 , "bold"),text = 'Données matériau',bg=gris_5) #définit le message 1
canva_tab2_labelframe.place(relx=0.01,rely=0.01,relwidth=0.98, relheight=0.45) # affiche le labelframe type de section
#messages des inputs E,Mv,m,m,Re,nu
label_young = Label(canva_tab2_labelframe,justify='center',font = ("Arial",10,"bold"),text = 'Entrez le Module de Young E de votre poutre \n en N/mm² ou MPa :',bg=gris_5)
label_massevol = Label(canva_tab2_labelframe,font = ("Arial",10,"bold"),text = 'Entrez la Masse volumique Mv de votre poutre \n en kg/mm3 : ',bg=gris_5)
label_limiteel = Label(canva_tab2_labelframe,font = ("Arial",10,"bold"),text = 'Entrez la Limite élastique Re de votre poutre en MPa :',bg=gris_5)
#saisie des inputs E,Mv,m,m,Re,nu
saisie_young = Entry(canva_tab2_labelframe,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
saisie_massevol = Entry(canva_tab2_labelframe,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
saisie_limiteel = Entry(canva_tab2_labelframe,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
#saisie affichage de départ
saisie_young.insert(0, "0.0")
saisie_massevol.insert(0, "0.0")
saisie_limiteel.insert(0, "0.0")
#Placement des items sur la grille
label_young.pack(fill='both')
saisie_young.pack(fill='both',pady=5)
label_massevol.pack(fill='both')
saisie_massevol.pack(fill='both',pady=5)
label_limiteel.pack(fill='both')
saisie_limiteel.pack(fill='both',pady=5)
# Gestion du stockage des valeurs
def valider_le_materiau_event(event):
    valider_le_materiau()
def valider_le_materiau():
    global valeurs_materiau,Re
    #Gestion du stockage des valeurs
    E = float(saisie_young.get())
    Mv = float(saisie_massevol.get())
    Re = float(saisie_limiteel.get())
    if E!='' and Re!='' :
        valeurs_materiau = [E,Mv,Re]
        saisie_young.focus()
        saisie_young.select_range(0,END)
    if E==0 or Re==0 :
        showerror('Erreur', 'Un champ de coordonnées est vide')
    if E=='' or Re=='' :
        showerror('Erreur', 'Un champ de coordonnées est vide')
    print("Les valeurs de E,Mv et Re sont :",valeurs_materiau)
# définition de fcts pour les lignes ci-dessous ou on gestionne le passage d'une case à l'autre et la désactivation de certains
def massevol_next(): #fct pour passer à Mv
    saisie_massevol.focus()
    saisie_massevol.select_range(0,END)
def limiteel_next(evt): #fct pour passer à Re
    saisie_limiteel.focus()
    saisie_limiteel.select_range(0,END)
def detection_passage2(evt): # détecte quand on doit passer d'une case à l'autre
    massevol_next() # switch de E à Mv quand on tape sur entrée
    saisie_massevol.bind('<Return>', limiteel_next) # switch de Mv à m quand on tape sur entrée
    saisie_limiteel.bind('<Return>', valider_le_materiau_event) # switch de Re à nu quand on tape sur entrée  
# initialisation sélection
saisie_young.focus()
saisie_young.select_range(0,END)
saisie_young.bind('<Return>', detection_passage2)         
# Bouton pour valider l'entrée des données de matériau pour rassurer l'utilisateur
Button(canva_tab2,relief="raised",overrelief="groove", text='Valider le matériau', command=valider_le_materiau, bg=gris_3,fg ="white", font=("Tahoma", 14,"bold")).place(relx=0.01,rely=0.47,relwidth=0.98, relheight=0.06)
### Barre 2_bis : Précision ###
canva_tab2_labelframe2 = LabelFrame(canva_tab2,font=("Arial",14 , "bold"),text = 'Précision',bg=gris_5) #définit le message 1
canva_tab2_labelframe2.place(relx=0.01,rely=0.70,relwidth=0.98, relheight=0.15) # affiche le labelframe type de section
# Gestion de la précision
NbrePointsX_bis = IntVar()
scale = Scale(canva_tab2_labelframe2,variable=NbrePointsX_bis,cursor='arrow',bd=0, orient='horizontal',font = ("Arial",10,"bold"), from_=100, to=1000,resolution=1,troughcolor=gris_7, tickinterval=100, length=1001, bg=gris_5,label='Discrétisation de la longueur de la poutre (Nombre de points) :')
scale.pack(fill='both',anchor=CENTER)
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
canva_tab3_labelframe1.place(relx=0.01,rely=0.01,relwidth=0.98, relheight=0.16) # affiche le labelframe type de chargement    
# Choisir quelle est la charge 1 du problème
canva_tab3_labelframe1_label = Label(canva_tab3_labelframe1,text = "Choisissez le type de charge sur votre poutre :",bg = gris_5,font = ("Arial",10,"bold"))
canva_tab3_labelframe1_label.place(relx=0.01,rely=0.02,relwidth=0.98, relheight=0.25)
chargement = StringVar()
canva_tab3_labelframe1_Combobox1 = ttk.Combobox(canva_tab3_labelframe1, textvariable = chargement , state = "readonly",justify='center')
canva_tab3_labelframe1_Combobox1['values'] = ["","2 appuis simples", "1 encastrement et 1 bord libre"]
canva_tab3_labelframe1_Combobox1.place(relx=0.01,rely=0.35,relwidth=0.98, relheight=0.28) # affichage de la combobox
canva_tab3_labelframe1_Combobox1.current(0) # onglet actif dans la combobox quand on démarre 
# Choisir quelle est la charge 2 du problème
def ajout_combobox_chargement():
    global chargement,chargement2,chargement3,canva_tab3_labelframe1_Combobox2,canva_tab3_labelframe1_Combobox3
    print("Sélection en cours du Combobox 1 :  index <",canva_tab3_labelframe1_Combobox1.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox1.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
    if str(chargement.get()) == '2 appuis simples':
        tabl_c_concentrée = tabl_c_répartie = tabl_c_répartie_partielle = tabl_c_répartie_partielle_proche = tabl_c_triang = []
        tabl_c_triangulaire_mon = tabl_c_triangulaire_antisy = tabl_c_trapézoïdale_sy = tabl_c_parabolique = tabl_couple = tabl_couple_réparti = tabl_c_décrois = tabl_c_crois = []
        print("changement d'appuis, suppression des charges")
        chargement2 = StringVar()
        canva_tab3_labelframe1_Combobox2 = ttk.Combobox(canva_tab3_labelframe1, textvariable = chargement2 , state = "readonly",justify='center')
        canva_tab3_labelframe1_Combobox2['values'] = ["","Charge concentrée", "Charge uniformément répartie", "Charge uniformément répartie partielle",\
                                "Charge uniformément répartie partielle proche des appuis","Charge triangulaire", "Charge triangulaire monotone",\
                                    "Charge triangulaire antisymétrique","Charge trapézoïdale","Charge parabolique","Moment"]
        canva_tab3_labelframe1_Combobox2.place(relx=0.01,rely=0.66,relwidth=0.98, relheight=0.28) # affichage de la combobox
        canva_tab3_labelframe1_Combobox2.current(0) # onglet actif dans la combobox quand on démarre
        # Passage d'une combobox à l'autre   
        canva_tab3_labelframe1_Combobox2.bind("<<ComboboxSelected>>", ajout_données_chargement)
    if str(chargement.get()) == '1 encastrement et 1 bord libre':
        tabl_c_concentrée = tabl_c_répartie = tabl_c_répartie_partielle = tabl_c_répartie_partielle_proche = tabl_c_triang = []
        tabl_c_triangulaire_mon = tabl_c_triangulaire_antisy = tabl_c_trapézoïdale_sy = tabl_c_parabolique = tabl_couple = tabl_couple_réparti = tabl_c_décrois = tabl_c_crois = []
        print("changement d'appuis, suppression des charges")
        chargement3 = StringVar()
        canva_tab3_labelframe1_Combobox3 = ttk.Combobox(canva_tab3_labelframe1, textvariable = chargement3 , state = "readonly",justify='center')
        canva_tab3_labelframe1_Combobox3['values'] = ["","Charge concentrée", "Charge uniformément répartie", "Charge uniformément répartie partielle",\
                                "Charge triangulaire croissante", "Charge triangulaire décroissante","Moment"]
        canva_tab3_labelframe1_Combobox3.place(relx=0.01,rely=0.66,relwidth=0.98, relheight=0.28) # affichage de la combobox
        canva_tab3_labelframe1_Combobox3.current(0) # onglet actif dans la combobox quand on démarre
        # Passage d'une combobox à l'autre   
        canva_tab3_labelframe1_Combobox3.bind("<<ComboboxSelected>>", ajout_données_chargement) 
def ajout_données_chargement(event): # nouvelle frame où on rentre les données du chargement
    global label_force_conc_1,label_force_rep_1,label_a1,label_c1,label_l,label_moment,\
        saisie_force_conc_1,saisie_force_rep_1,saisie_a1,saisie_c1,saisie_l,saisie_moment,canva_tab3_labelframe2,Listbox_tab3
    # nouveau_labelframe_chargement
    canva_tab3_labelframe2 = LabelFrame(canva_tab3,font=("Arial",14 , "bold"),text = "Chargement",bg=gris_5) #définit le message 1
    canva_tab3_labelframe2.place(relx=0.01,rely=0.17,relwidth=0.98, relheight=0.31) # affiche le labelframe type de section
    # Apparition du list box
    yDefilB = Scrollbar(canva_tab3, orient='vertical')
    yDefilB.place(relx=0.94,rely=0.49,relwidth=0.05, relheight=0.40)
    Listbox_tab3 = Listbox(canva_tab3,activestyle= 'dotbox',selectmode=SINGLE,yscrollcommand=yDefilB.set)
    Liste_listboxCharges.append(Listbox_tab3)
    Liste_listboxCharges[0].place(relx=0.01,rely=0.49,relwidth=0.93, relheight=0.40)
    yDefilB['command'] = Listbox_tab3.yview
    # Apparition bouton ajouter/supprimer/renommer charge
    Button(canva_tab3,relief="raised",overrelief="groove", text='Ajouter la charge', command=ajout_charge, bg=gris_3,fg ="white", font=("Tahoma", 12,"bold")).place(relx=0.01,rely=0.90,relwidth=0.49, relheight=0.04)
    Button(canva_tab3,relief="raised",overrelief="groove", text='Renommer la charge', command=renommer_charge, bg=gris_3,fg ="white", font=("Tahoma", 12,"bold")).place(relx=0.51,rely=0.90,relwidth=0.48, relheight=0.04)
    Button(canva_tab3,relief="raised",overrelief="groove", text='Supprimer la charge', command=supprimer_charge, bg=gris_3,fg ="white", font=("Tahoma", 13,"bold")).place(relx=0.01,rely=0.95,relwidth=0.98, relheight=0.04)
    if str(chargement.get()) == '2 appuis simples' : 
        if str(chargement2.get()) == 'Charge concentrée' :
            # messages des inputs
            label_force_conc_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Force concentrée P sur votre poutre en N :',bg=gris_5)
            label_a1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la distance a1 de votre poutre en mm :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_charge_con_app_simple)
            labelimg.image = img_charge_con_app_simple
            labelimg.pack(fill=BOTH, expand=1)            
            # canva_tab4.create_image(700,500, image=img_charge_con_app_simple)               
            # lancement retour des touches
            saisie_force_conc_1.bind('<Return>',a1_next)
            saisie_a1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 2 :  index <",canva_tab3_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement2.get()) == 'Charge uniformément répartie' :
            # messages des inputs
            label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Force répartie q sur votre poutre en N/mm :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_charge_rep_app_simple)
            labelimg.image = img_charge_rep_app_simple
            labelimg.pack(fill=BOTH, expand=1)                            
            # lancement retour des touches
            saisie_force_rep_1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 2 :  index <",canva_tab3_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement2.get()) == 'Charge uniformément répartie partielle' :
            # messages des inputs
            label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Force répartie q sur votre poutre en N/mm :',bg=gris_5)
            label_l = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Distance sur laquelle la charge s’applique I \nsur votre poutre en mm :',bg=gris_5)        
            label_c1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Distance entre le noeud de base et l’endroit \ndu début d’application de la charge c1 sur votre poutre \nen mm :',bg=gris_5)
            # saisie des inputs
            saisie_force_rep_1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            saisie_l = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            saisie_c1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            # Placement des items sur la grille
            label_force_rep_1.pack(fill='both')
            saisie_force_rep_1.pack(fill='both')
            label_l.pack(fill='both')
            saisie_l.pack(fill='both')
            label_c1.pack(fill='both')
            saisie_c1.pack(fill='both')
            # saisie affichage de départ
            saisie_force_rep_1.insert(0, "0.0") # saisie affichage de départ
            saisie_l.insert(0, "0.0") # saisie affichage de départ
            saisie_c1.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_force_rep_1.focus() 
            saisie_force_rep_1.select_range(0,END)
            # main au dessus de la case
            saisie_force_rep_1.config(cursor='hand1')
            saisie_l.config(cursor='hand1')
            saisie_c1.config(cursor='hand1')
            # la photo de la configuration  
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_charge_rep_part)
            labelimg.image = img_charge_rep_part
            labelimg.pack(fill=BOTH, expand=1)             
            # lancement retour des touches
            saisie_force_rep_1.bind('<Return>',I_next)
            saisie_l.bind('<Return>',c1_next)
            saisie_c1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 2 :  index <",canva_tab3_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement2.get()) == 'Charge uniformément répartie partielle proche des appuis' :
            # messages des inputs
            label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Force répartie q sur votre poutre en N/mm :',bg=gris_5)
            label_l = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Distance sur laquelle la charge s’applique a \nsur votre  poutre en mm :',bg=gris_5)        
            # saisie des inputs
            saisie_force_rep_1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            saisie_l = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            # Placement des items sur la grille
            label_force_rep_1.pack(fill='both')
            saisie_force_rep_1.pack(fill='both')
            label_l.pack(fill='both')
            saisie_l.pack(fill='both')
            # saisie affichage de départ
            saisie_force_rep_1.insert(0, "0.0") # saisie affichage de départ
            saisie_l.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_force_rep_1.focus() 
            saisie_force_rep_1.select_range(0,END)
            # main au dessus de la case
            saisie_force_rep_1.config(cursor='hand1')
            saisie_l.config(cursor='hand1')
            # la photo de la configuration  
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_charge_rep_part_proche)
            labelimg.image = img_charge_rep_part_proche
            labelimg.pack(fill=BOTH, expand=1)             
            # lancement retour des touches
            saisie_force_rep_1.bind('<Return>',I_next)
            saisie_l.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 2 :  index <",canva_tab3_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement2.get()) == 'Charge triangulaire' :
            # messages des inputs
            label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Force répartie q sur votre poutre en N :',bg=gris_5)
            label_a1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la distance a1 de votre poutre en mm :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_charge_triang)
            labelimg.image = img_charge_triang
            labelimg.pack(fill=BOTH, expand=1)
            # lancement retour des touches
            saisie_force_rep_1.bind('<Return>',a1_next)
            saisie_a1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 2 :  index <",canva_tab3_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement2.get()) == 'Charge triangulaire monotone' :
            # messages des inputs
            label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Force répartie q sur votre poutre en N :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_charge_triang_monotone)
            labelimg.image = img_charge_triang_monotone
            labelimg.pack(fill=BOTH, expand=1)
            # lancement retour des touches
            saisie_force_rep_1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 2 :  index <",canva_tab3_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement2.get()) == 'Charge triangulaire antisymétrique' :
            # messages des inputs
            label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Force répartie q sur votre poutre en N :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_charge_triang_anti)
            labelimg.image = img_charge_triang_anti
            labelimg.pack(fill=BOTH, expand=1)
            # lancement retour des touches
            saisie_force_rep_1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 2 :  index <",canva_tab3_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement2.get()) == 'Charge trapézoïdale' :
            # messages des inputs
            label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Force répartie q sur votre poutre en N/mm :',bg=gris_5)
            label_l = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Distance sur laquelle la charge s’applique I \nsur votre  poutre en mm :',bg=gris_5)        
            label_c1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Distance entre le noeud de base et l’endroit \ndu début d’application de la charge c1 sur votre poutre \nen mm :',bg=gris_5)
            # saisie des inputs
            saisie_force_rep_1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            saisie_l = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            saisie_c1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            # Placement des items sur la grille
            label_force_rep_1.pack(fill='both')
            saisie_force_rep_1.pack(fill='both')
            label_l.pack(fill='both')
            saisie_l.pack(fill='both')
            label_c1.pack(fill='both')
            saisie_c1.pack(fill='both')
            # saisie affichage de départ
            saisie_force_rep_1.insert(0, "0.0") # saisie affichage de départ
            saisie_l.insert(0, "0.0") # saisie affichage de départ
            saisie_c1.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_force_rep_1.focus() 
            saisie_force_rep_1.select_range(0,END)
            # main au dessus de la case
            saisie_force_rep_1.config(cursor='hand1')
            saisie_l.config(cursor='hand1')
            saisie_c1.config(cursor='hand1')
            # la photo de la configuration  
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_charge_trapèze)
            labelimg.image = img_charge_trapèze
            labelimg.pack(fill=BOTH, expand=1)
            # lancement retour des touches
            saisie_force_rep_1.bind('<Return>',I_next)
            saisie_l.bind('<Return>',c1_next)
            saisie_c1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 2 :  index <",canva_tab3_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement2.get()) == 'Charge parabolique' :
            # messages des inputs
            label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Force répartie q sur votre poutre en N :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_charge_parabo)
            labelimg.image = img_charge_parabo
            labelimg.pack(fill=BOTH, expand=1)
            # lancement retour des touches
            saisie_force_rep_1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 2 :  index <",canva_tab3_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement2.get()) == 'Moment' :
            # messages des inputs
            label_moment = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez le Moment M sur votre poutre en N.mm :',bg=gris_5)
            label_a1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la distance a1 de votre poutre en mm :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_charge_moment_app_simple)
            labelimg.image = img_charge_moment_app_simple
            labelimg.pack(fill=BOTH, expand=1)
            # lancement retour des touches
            saisie_moment.bind('<Return>',a1_next)
            saisie_a1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 2 :  index <",canva_tab3_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
    if str(chargement.get()) == '1 encastrement et 1 bord libre' : 
        if str(chargement3.get()) == 'Charge concentrée' :
            # messages des inputs
            label_force_conc_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Force concentrée P sur votre poutre en N :',bg=gris_5)
            label_a1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la distance a1 de votre poutre en mm :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_charge_con_encas)
            labelimg.image = img_charge_con_encas
            labelimg.pack(fill=BOTH, expand=1)
            # lancement retour des touches
            saisie_force_conc_1.bind('<Return>',a1_next)
            saisie_a1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 3 :  index <",canva_tab3_labelframe1_Combobox3.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox3.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement3.get()) == 'Charge uniformément répartie' :
            # messages des inputs
            label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Force répartie q sur votre poutre en N/mm :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_charge_rep_encas)
            labelimg.image = img_charge_rep_encas
            labelimg.pack(fill=BOTH, expand=1)
            # lancement retour des touches
            saisie_force_rep_1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 3 :  index <",canva_tab3_labelframe1_Combobox3.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox3.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement3.get()) == 'Charge uniformément répartie partielle' :
            # messages des inputs
            label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Force répartie q sur votre poutre en N/mm :',bg=gris_5)
            label_l = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Distance sur laquelle la charge s’applique I \nsur votre poutre en mm :',bg=gris_5)        
            label_c1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Distance entre le noeud de base et l’endroit \ndu début d’application de la charge c1 sur votre poutre \nen mm :',bg=gris_5)
            # saisie des inputs
            saisie_force_rep_1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            saisie_l = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            saisie_c1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_4,font = ("Arial",11),justify='center',bg=gris_2)
            # Placement des items sur la grille
            label_force_rep_1.pack(fill='both')
            saisie_force_rep_1.pack(fill='both')
            label_l.pack(fill='both')
            saisie_l.pack(fill='both')
            label_c1.pack(fill='both')
            saisie_c1.pack(fill='both')
            # saisie affichage de départ
            saisie_force_rep_1.insert(0, "0.0") # saisie affichage de départ
            saisie_l.insert(0, "0.0") # saisie affichage de départ
            saisie_c1.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_force_rep_1.focus() 
            saisie_force_rep_1.select_range(0,END)
            # main au dessus de la case
            saisie_force_rep_1.config(cursor='hand1')
            saisie_l.config(cursor='hand1')
            saisie_c1.config(cursor='hand1')
            # la photo de la configuration 
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_charge_rep_part)
            labelimg.image = img_charge_rep_part
            labelimg.pack(fill=BOTH, expand=1)
            # lancement retour des touches
            saisie_force_rep_1.bind('<Return>',I_next)
            saisie_l.bind('<Return>',c1_next)
            saisie_c1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 3 :  index <",canva_tab3_labelframe1_Combobox3.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox3.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement3.get()) == 'Charge triangulaire croissante' :
            # messages des inputs
            label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Force répartie q sur votre poutre en N :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_charge_triang_croiss)
            labelimg.image = img_charge_triang_croiss
            labelimg.pack(fill=BOTH, expand=1)
            # lancement retour des touches
            saisie_force_rep_1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 3 :  index <",canva_tab3_labelframe1_Combobox3.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox3.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement3.get()) == 'Charge triangulaire décroissante' :
            # messages des inputs
            label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la Force répartie q sur votre poutre en N :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_charge_triang_décroiss)
            labelimg.image = img_charge_triang_décroiss
            labelimg.pack(fill=BOTH, expand=1)
            # lancement retour des touches
            saisie_force_rep_1.bind('<Return>',ajout_charge_event)
            print("Sélection en cours du Combobox 3 :  index <",canva_tab3_labelframe1_Combobox3.current(),"> et intitulé <", canva_tab3_labelframe1_Combobox3.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
        if str(chargement3.get()) == 'Moment' :
            # messages des inputs
            label_moment = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez le Moment M sur votre poutre en N.mm :',bg=gris_5)
            label_a1 = Label(canva_tab3_labelframe2,font = ("Arial",10,"bold"),text = 'Entrez la distance a1 de votre poutre en mm :',bg=gris_5)
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
            recreer_le_canva()
            labelimg=Label(canva_tab4,image=img_charge_moment_encas)
            labelimg.image = img_charge_moment_encas
            labelimg.pack(fill=BOTH, expand=1)
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
tabl_c_répartie_partielle_proche = []
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
    global label_force_conc_1,label_force_rep_1,label_a1,label_c1,label_l,label_moment,\
        saisie_force_conc_1,saisie_force_rep_1,saisie_a1,saisie_c1,saisie_l,saisie_moment,canva_tab3_labelframe2,liste_charges,Liste_listboxCharges
    bouton_calculer.configure(state=NORMAL)
    if str(chargement.get()) == '2 appuis simples' : 
        if str(chargement2.get()) == 'Charge concentrée' :
            p = float(saisie_force_conc_1.get())
            a1 = float(saisie_a1.get())
            if p!= 0.0 and a1!= 0.0 :
                VarEcrase = classe.charge_concentrée(p, a1)
                tabl_c_concentrée.append(VarEcrase)  
                nbr = classe.charge_concentrée.nbr
                liste_charges.append(['Charge concentrée ',str(nbr)+' [p = '+str(tabl_c_concentrée[nbr-1].P) + " ; a = "+ str(tabl_c_concentrée[nbr-1].a) +"]", nbr])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_conc_1.focus()
                saisie_force_conc_1.select_range(0,END)
            if float(saisie_force_conc_1.get())==0 or float(saisie_a1.get())==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide.')   
            print('Stockage charge : ',chargement.get()," - ",chargement2.get())
            for i in range(len(tabl_c_concentrée)):
                print(tabl_c_concentrée[i].P," - ",tabl_c_concentrée[i].a)
        elif str(chargement2.get()) == 'Charge uniformément répartie' :
            q = float(saisie_force_rep_1.get())
            if q!='' and q!= 0.0:
                VarEcrase = classe.charge_répartie(q)
                tabl_c_répartie.append(VarEcrase)  
                nbr = classe.charge_répartie.nbr
                liste_charges.append(['Charge répartie ',str(nbr)+" [q = "+ str(tabl_c_répartie[nbr-1].q) +"]", nbr])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_rep_1.focus()
                saisie_force_rep_1.select_range(0,END)
            if q==0 or q=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide.') 
            print('Stockage charge : ',chargement.get()," - ",chargement2.get())
            for i in range(len(tabl_c_répartie)):
                print(tabl_c_répartie[i].q)
        elif str(chargement2.get()) == 'Charge uniformément répartie partielle' :
            q = float(saisie_force_rep_1.get())
            l = float(saisie_l.get())
            c1 = float(saisie_c1.get())
            if q!='' and l!='' and c1!='' and q!= 0.0 and l!= 0.0 and c1!= 0.0:
                VarEcrase = classe.charge_répartie_partielle(q, c1, l)
                tabl_c_répartie_partielle.append(VarEcrase) 
                nbr = classe.charge_répartie_partielle.nbr
                liste_charges.append(['Charge répartie partielle ',str(nbr)+ "[q = "+ str(tabl_c_répartie_partielle[nbr-1].q) + " ; c1 = "+ str(tabl_c_répartie_partielle[nbr-1].a) + " ; l = "+ str(tabl_c_répartie_partielle[nbr-1].b)+ "]", nbr])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_rep_1.focus()
                saisie_force_rep_1.select_range(0,END)
            if q==0 or l==0 or c1==0 or q=='' or l=='' or c1=='':
                showerror('Erreur', 'Un champ de coordonnées est vide.')
            print('Stockage charge : ',chargement.get()," - ",chargement2.get())
            for i in range(len(tabl_c_répartie_partielle)):
                print(tabl_c_répartie_partielle[i].q," - ",tabl_c_répartie_partielle[i].a," - ",tabl_c_répartie_partielle[i].b)
        elif str(chargement2.get()) == 'Charge uniformément répartie partielle proche des appuis' :
            q = float(saisie_force_rep_1.get())
            l = float(saisie_l.get())
            if q!='' and l!='' and q!= 0.0 and l!= 0.0 :
                VarEcrase = classe.charge_répartie_partielle_proche(q, l)
                tabl_c_répartie_partielle_proche.append(VarEcrase) 
                nbr = classe.charge_répartie_partielle_proche.nbr
                liste_charges.append(['Charge répartie partielle proche ',str(nbr)+ "[q = "+ str(tabl_c_répartie_partielle_proche[nbr-1].q) + " ; l = "+ str(tabl_c_répartie_partielle_proche[nbr-1].l) +  "]", nbr])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_rep_1.focus()
                saisie_force_rep_1.select_range(0,END)
            if q==0 or l==0 or q=='' or l=='':
                showerror('Erreur', 'Un champ de coordonnées est vide.')
            print('Stockage charge : ',chargement.get()," - ",chargement2.get())
            for i in range(len(tabl_c_répartie_partielle_proche)):
                print(tabl_c_répartie_partielle_proche[i].q," - ",tabl_c_répartie_partielle_proche[i].l)       
        elif str(chargement2.get()) == 'Charge triangulaire' :
            q = float(saisie_force_rep_1.get())
            a1 = float(saisie_a1.get())
            if q!='' and a1!=''and q!= 0.0 and a1!= 0.0 :
                VarEcrase = classe.charge_triangulaire(q, a1)
                tabl_c_triang.append(VarEcrase) 
                nbr = classe.charge_triangulaire.nbr
                liste_charges.append(['Charge triangulaire ',str(nbr)+ "[q = "+ str(tabl_c_triang[nbr-1].q) + " ; a1 = "+ str(tabl_c_triang[nbr-1].a) +"]", nbr])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_rep_1.focus()
                saisie_force_rep_1.select_range(0,END)
            if q==0 or a1==0 or q=='' or a1=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide.')
            print('Stockage charge : ',chargement.get()," - ",chargement2.get())
            for i in range(len(tabl_c_triang)):
                print(tabl_c_triang[i].q," - ",tabl_c_triang[i].a)
        elif str(chargement2.get()) == 'Charge triangulaire monotone' :
            q = float(saisie_force_rep_1.get())
            if q!='' and q!=0.0:
                VarEcrase = classe.charge_triangulaire_monotone(q)
                tabl_c_triangulaire_mon.append(VarEcrase)
                nbr = classe.charge_triangulaire_monotone.nbr
                liste_charges.append(['Charge triangulaire monotone ',str(nbr)+ "[q = "+ str(tabl_c_triangulaire_mon[nbr-1].q) +"]", nbr])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_rep_1.focus()
                saisie_force_rep_1.select_range(0,END)
            if q==0 or q=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide.')
            print('Stockage charge : ',chargement.get()," - ",chargement2.get())
            for i in range(len(tabl_c_triangulaire_mon)):
                print(tabl_c_triangulaire_mon[i].q)
        elif str(chargement2.get()) == 'Charge triangulaire antisymétrique' :
            q = float(saisie_force_rep_1.get())
            if q!='' and q!=0.0:
                VarEcrase = classe.charge_triangulaire_antisymétrique(q)
                tabl_c_triangulaire_antisy.append(VarEcrase)
                nbr = classe.charge_triangulaire_antisymétrique.nbr
                liste_charges.append(['Charge triangulaire antisymétrique ',str(nbr)+ "[q = "+ str(tabl_c_triangulaire_antisy[nbr-1].q) + "]", nbr])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_rep_1.focus()
                saisie_force_rep_1.select_range(0,END)
            if q==0 or q=='':
                showerror('Erreur', 'Un champ de coordonnées est vide.') 
            print('Stockage charge : ',chargement.get()," - ",chargement2.get())
            for i in range(len(tabl_c_triangulaire_antisy)):
                print(tabl_c_triangulaire_antisy[i].q)
        elif str(chargement2.get()) == 'Charge trapézoïdale' :
            q = float(saisie_force_rep_1.get())
            l = float(saisie_l.get())
            c1 = float(saisie_c1.get())
            if q!='' and l!='' and c1!='' and q!= 0.0 and l!= 0.0 and c1!= 0.0:
                VarEcrase = classe.charge_trapézoïdale_symétrique(q, c1, l)
                tabl_c_trapézoïdale_sy.append(VarEcrase)
                nbr = classe.charge_trapézoïdale_symétrique.nbr
                liste_charges.append(['Charge trapézoïdale ',str(nbr)+ "[q = "+ str(tabl_c_trapézoïdale_sy[nbr-1].q) + " ; c1 = "+ str(tabl_c_trapézoïdale_sy[nbr-1].a) + " ; l = "+ str(tabl_c_trapézoïdale_sy[nbr-1].l) +"]", nbr])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_rep_1.focus()
                saisie_force_rep_1.select_range(0,END)
            if q==0 or l==0 or c1==0 or q=='' or l=='' or c1=='':
                showerror('Erreur', 'Un champ de coordonnées est vide.')
            print('Stockage charge : ',chargement.get()," - ",chargement2.get())
            for i in range(len(tabl_c_trapézoïdale_sy)):
                print(tabl_c_trapézoïdale_sy[i].q," - ",tabl_c_trapézoïdale_sy[i].a," - ",tabl_c_trapézoïdale_sy[i].b)
        elif str(chargement2.get()) == 'Charge parabolique' :
            q = float(saisie_force_rep_1.get())
            if q!='' and q!=0.0:
                VarEcrase = classe.charge_parabolique(q)
                tabl_c_parabolique.append(VarEcrase)
                nbr = classe.charge_parabolique.nbr
                liste_charges.append(['Charge parabolique ',str(nbr)+ "[q = "+ str(tabl_c_parabolique[nbr-1].q) +"]", nbr])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_rep_1.focus()
                saisie_force_rep_1.select_range(0,END)
            if q==0 or q=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide.') 
            print('Stockage charge : ',chargement.get()," - ",chargement2.get())
            for i in range(len(tabl_c_trapézoïdale_sy)):
                print(tabl_c_parabolique[i].q)
        elif str(chargement2.get()) == 'Moment' :
            M = float(saisie_moment.get())
            a1 = float(saisie_a1.get())
            if M!='' and a1!=''and M!= 0.0 and a1!= 0.0 :
                VarEcrase = classe.couple(M, a1)
                tabl_couple.append(VarEcrase)
                nbr = classe.couple.nbr
                liste_charges.append(['Couple ',str(nbr)+ "[M = "+ str(tabl_couple[nbr-1].C) + " ; a1 = "+ str(tabl_couple[nbr-1].a) +"]", nbr])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_moment.focus()
                saisie_moment.select_range(0,END)
            if M==0 or a1==0 or M=='' or a1=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide.')
            print('Stockage charge : ',chargement.get()," - ",chargement2.get())
            for i in range(len(tabl_couple)):
                print(tabl_couple[i].C," - ",tabl_couple[i].a)
    elif str(chargement.get()) == '1 encastrement et 1 bord libre' : 
        if str(chargement3.get()) == 'Charge concentrée' :
            p = float(saisie_force_conc_1.get())
            a1 = float(saisie_a1.get())
            if p!='' and a1!='' and p!= 0.0 and a1!= 0.0 :
                VarEcrase = classe.charge_concentrée(p, a1)
                tabl_c_concentrée.append(VarEcrase)  
                nbr = classe.charge_concentrée.nbr
                liste_charges.append(['Charge concentrée ',str(nbr)+ "[P = "+ str(tabl_c_concentrée[nbr-1].P) + " ; a1 = "+ str(tabl_c_concentrée[nbr-1].a) +"]", nbr])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_conc_1.focus()
                saisie_force_conc_1.select_range(0,END)
            if p==0 or a1==0 or p=='' or a1=='':
                showerror('Erreur', 'Un champ de coordonnées est vide.')
            print('Stockage charge : ',chargement.get()," - ",chargement3.get())
            for i in range(len(tabl_c_concentrée)):
                print(tabl_c_concentrée[i].P," - ",tabl_c_concentrée[i].a)                
        elif str(chargement3.get()) == 'Charge uniformément répartie' :
            q = float(saisie_force_rep_1.get())
            if q!='' and q!=0.0:
                VarEcrase = classe.charge_répartie(q)
                tabl_c_répartie.append(VarEcrase)  
                nbr = classe.charge_répartie.nbr
                liste_charges.append(['Charge répartie ',str(nbr)+ "[q = "+ str(tabl_c_répartie[nbr-1].q) +"]", nbr])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_rep_1.focus()
                saisie_force_rep_1.select_range(0,END)
            if q==0 or q=='':
                showerror('Erreur', 'Un champ de coordonnées est vide.')
            print('Stockage charge : ',chargement.get()," - ",chargement3.get())
            for i in range(len(tabl_c_répartie)):
                print(tabl_c_répartie[i].q) 
        elif str(chargement3.get()) == 'Charge uniformément répartie partielle' :
            q = float(saisie_force_rep_1.get())
            l = float(saisie_l.get())
            c1 = float(saisie_c1.get())
            if q!='' and l!='' and c1!='' and q!= 0.0 and l!= 0.0 and c1!= 0.0:
                VarEcrase = classe.charge_répartie_partielle(q, c1, l)
                tabl_c_répartie_partielle.append(VarEcrase) 
                nbr = classe.charge_répartie_partielle.nbr
                liste_charges.append(['Charge répartie partielle ',str(nbr)+ "[q = "+ str(tabl_c_répartie_partielle[nbr-1].q) + " ; c1 = "+ str(tabl_c_répartie_partielle[nbr-1].a) + " ; l = "+ str(tabl_c_répartie_partielle[nbr-1].b)+ "]", nbr])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_rep_1.focus()
                saisie_force_rep_1.select_range(0,END)
            if q==0 or l==0 or c1==0 or q=='' or l=='' or c1=='':
                showerror('Erreur', 'Un champ de coordonnées est vide.')
            print('Stockage charge : ',chargement.get()," - ",chargement3.get())
            for i in range(len(tabl_c_répartie_partielle)):
                print(tabl_c_répartie_partielle[i].q," - ",tabl_c_répartie_partielle[i].a," - ",tabl_c_répartie_partielle[i].b)
        elif str(chargement3.get()) == 'Charge triangulaire croissante' :
            q = float(saisie_force_rep_1.get())
            if q!='' and q!=0.0:
                VarEcrase = classe.charge_croissante(q)
                tabl_c_crois.append(VarEcrase)
                nbr = classe.charge_croissante.nbr
                liste_charges.append(['Charge croissante ',str(nbr)+"[q = "+ str(tabl_c_crois[nbr-1].q) + "]", nbr])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_rep_1.focus()
                saisie_force_rep_1.select_range(0,END)
            if q==0 or q=='':
                showerror('Erreur', 'Un champ de coordonnées est vide.')     
            print('Stockage charge : ',chargement.get()," - ",chargement3.get())
            for i in range(len(tabl_c_crois)):
                print(tabl_c_crois[i].q)
        elif str(chargement3.get()) == 'Charge triangulaire décroissante' :
            q = float(saisie_force_rep_1.get())
            if q!='' and q!=0.0:
                VarEcrase = classe.charge_décroissante(q)
                tabl_c_décrois.append(VarEcrase)
                nbr = classe.charge_décroissante.nbr
                liste_charges.append(['Charge décroissante ',str(nbr)+"[q = "+ str(tabl_c_décrois[nbr-1].q) + "]", nbr])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_force_rep_1.focus()
                saisie_force_rep_1.select_range(0,END)
            if q==0 or q=='':
                showerror('Erreur', 'Un champ de coordonnées est vide.')
            print('Stockage charge : ',chargement.get()," - ",chargement3.get())
            for i in range(len(tabl_c_décrois)):
                print(tabl_c_décrois[i].q)
        elif str(chargement3.get()) == 'Moment' :
            M = float(saisie_moment.get())
            a1 = float(saisie_a1.get())
            if M!='' and a1!=''and M!= 0.0 and a1!= 0.0 :
                VarEcrase = classe.couple(M, a1)
                tabl_couple.append(VarEcrase)
                nbr = classe.couple.nbr
                liste_charges.append(['Couple ',str(nbr)+ "[M = "+ str(tabl_couple[nbr-1].C) + " ; a1 = "+ str(tabl_couple[nbr-1].a) +"]", nbr])
                udapte_listbox_charge(len(liste_charges)-1)
                saisie_moment.focus()
                saisie_moment.select_range(0,END)
            if M==0 or a1==0 or M=='' or a1=='':
                showerror('Erreur', 'Un champ de coordonnées est vide.')  
            print('Stockage charge : ',chargement.get()," - ",chargement3.get())
            for i in range(len(tabl_couple)):
                print(tabl_couple[i].C," - ",tabl_couple[i].a)
def udapte_listbox_charge(index):    
    for i in Liste_listboxCharges:
        i.delete(index)
    if Liste_listboxCharges[0].size()!=len(liste_charges):
        for i in Liste_listboxCharges:
            i.insert(index,liste_charges[index][0]+" "+liste_charges[index][1])
    Liste_listboxCharges[0].see(index)
def renommer_charge():
    if Liste_listboxCharges[0].curselection()!=():
        temp_nom_charges=simpledialog.askstring("Renommer ", 'Nouveau nom de la charges : "'+Liste_listboxCharges[0].get(Liste_listboxCharges[0].curselection()[0])+'" :')
        if temp_nom_charges!='':
            liste_charges[Liste_listboxCharges[0].curselection()[0]][0] = temp_nom_charges
            udapte_listbox_charge(Liste_listboxCharges[0].curselection()[0])
    else:
        showerror('Erreur', 'Aucune charge sélectionné.')
def supprimer_charge():
    if Liste_listboxCharges[0].curselection()!=():
        print("suppression de ", liste_charges[Liste_listboxCharges[0].curselection()[0]][0])
        if liste_charges[Liste_listboxCharges[0].curselection()[0]][0] == 'Charge concentrée ' :
            IndiceSuppr = liste_charges[Liste_listboxCharges[0].curselection()[0]][2] - 1
            del tabl_c_concentrée[IndiceSuppr]
            classe.charge_concentrée.nbr -= 1
            print("il n'y a maintenant plus que ", classe.charge_concentrée.nbr, "Charge concentrée d'attributs : ")
            for k in range(len(tabl_c_concentrée)): print(tabl_c_concentrée[k].P, tabl_c_concentrée[k].a)   
        if liste_charges[Liste_listboxCharges[0].curselection()[0]][0] == 'Charge répartie ' :
            IndiceSuppr = liste_charges[Liste_listboxCharges[0].curselection()[0]][2] - 1
            del tabl_c_répartie[IndiceSuppr]
            classe.charge_répartie.nbr -= 1
            print("il n'y a maintenant plus que ", classe.charge_répartie.nbr, "Charge répartie d'attributs : ")
            for k in range(len(tabl_c_répartie)): print(tabl_c_répartie[k].q)   
        if liste_charges[Liste_listboxCharges[0].curselection()[0]][0] == 'Charge répartie partielle ' :
            IndiceSuppr = liste_charges[Liste_listboxCharges[0].curselection()[0]][2] - 1
            del tabl_c_répartie_partielle[IndiceSuppr]
            classe.charge_répartie_partielle.nbr -= 1
            print("il n'y a maintenant plus que ", classe.charge_répartie_partielle.nbr, "Charge répartie partielle d'attributs : ")
            for k in range(len(tabl_c_répartie_partielle)): print(tabl_c_répartie_partielle[k].q, tabl_c_répartie_partielle[k].a, tabl_c_répartie_partielle[k].b)   
        if liste_charges[Liste_listboxCharges[0].curselection()[0]][0] == 'Charge répartie partielle proche ' :
            IndiceSuppr = liste_charges[Liste_listboxCharges[0].curselection()[0]][2] - 1
            del tabl_c_répartie_partielle_proche[IndiceSuppr]
            classe.charge_répartie_partielle_proche.nbr -= 1
            print("il n'y a maintenant plus que ", classe.charge_répartie_partielle_proche.nbr, "Charge répartie partielle proche d'attributs : ")
            for k in range(len(tabl_c_répartie_partielle_proche)): print(tabl_c_répartie_partielle_proche[k].q, tabl_c_répartie_partielle_proche[k].l)   
        if liste_charges[Liste_listboxCharges[0].curselection()[0]][0] == 'Charge triangulaire ' :
            IndiceSuppr = liste_charges[Liste_listboxCharges[0].curselection()[0]][2] - 1
            del tabl_c_triang[IndiceSuppr]
            classe.charge_triangulaire.nbr -= 1
            print("il n'y a maintenant plus que ", classe.charge_triangulaire.nbr, "Charge triangulaire d'attributs : ")
            for k in range(len(tabl_c_triang)): print(tabl_c_triang[k].q, tabl_c_triang[k].a)   
        if liste_charges[Liste_listboxCharges[0].curselection()[0]][0] == 'Charge triangulaire monotone ' :
            IndiceSuppr = liste_charges[Liste_listboxCharges[0].curselection()[0]][2] - 1
            del tabl_c_triangulaire_mon[IndiceSuppr]
            classe.charge_triangulaire_monotone.nbr -= 1
            print("il n'y a maintenant plus que ", classe.charge_triangulaire_monotone.nbr, "Charge triangulaire monotone d'attributs : ")
            for k in range(len(tabl_c_triangulaire_mon)): print(tabl_c_triangulaire_mon[k].q)   
        if liste_charges[Liste_listboxCharges[0].curselection()[0]][0] == 'Charge triangulaire antisymétrique ' :
            IndiceSuppr = liste_charges[Liste_listboxCharges[0].curselection()[0]][2] - 1
            del tabl_c_triangulaire_antisy[IndiceSuppr]
            classe.charge_triangulaire_antisymétrique.nbr -= 1
            print("il n'y a maintenant plus que ", classe.charge_triangulaire_antisymétrique.nbr, "Charge triangulaire antisymétrique d'attributs : ")
            for k in range(len(tabl_c_triangulaire_antisy)): print(tabl_c_triangulaire_antisy[k].q)   
        if liste_charges[Liste_listboxCharges[0].curselection()[0]][0] == 'Charge trapézoïdale ' :
            IndiceSuppr = liste_charges[Liste_listboxCharges[0].curselection()[0]][2] - 1
            del tabl_c_trapézoïdale_sy[IndiceSuppr]
            classe.charge_trapézoïdale_symétrique.nbr -= 1
            print("il n'y a maintenant plus que ", classe.charge_trapézoïdale_symétrique.nbr, "Charge trapézoïdale d'attributs : ")
            for k in range(len(tabl_c_trapézoïdale_sy)): print(tabl_c_trapézoïdale_sy[k].q)   
        if liste_charges[Liste_listboxCharges[0].curselection()[0]][0] == 'Charge parabolique ' :
            IndiceSuppr = liste_charges[Liste_listboxCharges[0].curselection()[0]][2] - 1
            del tabl_c_parabolique[IndiceSuppr]
            classe.charge_parabolique.nbr -= 1
            print("il n'y a maintenant plus que ", classe.charge_parabolique.nbr, "Charge parabolique d'attributs : ")
            for k in range(len(tabl_c_parabolique)): print(tabl_c_parabolique[k].q) 
        if liste_charges[Liste_listboxCharges[0].curselection()[0]][0] == 'Couple ' :
            IndiceSuppr = liste_charges[Liste_listboxCharges[0].curselection()[0]][2] - 1
            del tabl_couple[IndiceSuppr]
            classe.couple.nbr -= 1
            print("il n'y a maintenant plus que ", classe.couple.nbr, "Couple d'attributs : ")
            for k in range(len(tabl_couple)): print(tabl_couple[k].C) 
        if liste_charges[Liste_listboxCharges[0].curselection()[0]][0] == 'Couple réparti ' :
            IndiceSuppr = liste_charges[Liste_listboxCharges[0].curselection()[0]][2] - 1
            del tabl_couple_réparti[IndiceSuppr]
            classe.couple_réparti.nbr -= 1
            print("il n'y a maintenant plus que ", classe.couple_réparti.nbr, "Couple réparti d'attributs : ")
            for k in range(len(tabl_couple_réparti)): print(tabl_couple_réparti[k].C) 
        if liste_charges[Liste_listboxCharges[0].curselection()[0]][0] == 'Charge croissante ' :
            IndiceSuppr = liste_charges[Liste_listboxCharges[0].curselection()[0]][2] - 1
            del tabl_c_crois[IndiceSuppr]
            classe.charge_croissante.nbr -= 1
            print("il n'y a maintenant plus que ", classe.charge_croissante.nbr, "Charge croissante d'attributs : ")
            for k in range(len(tabl_c_crois)): print(tabl_c_crois[k].q) 
        if liste_charges[Liste_listboxCharges[0].curselection()[0]][0] == 'Charge décroissante ' :
            IndiceSuppr = liste_charges[Liste_listboxCharges[0].curselection()[0]][2] - 1
            del tabl_c_décrois[IndiceSuppr]
            classe.charge_décroissante.nbr -= 1
            print("il n'y a maintenant plus que ", classe.charge_décroissante.nbr, "Charge décroissante d'attributs : ")
            for k in range(len(tabl_c_décrois)): print(tabl_c_décrois[k].q) 
        del liste_charges[Liste_listboxCharges[0].curselection()[0]]
        udapte_listbox_charge(Liste_listboxCharges[0].curselection()[0])
    else:
        showerror('Erreur', 'Aucune charge sélectionné.')
def a1_next(event): #fct pour passer à a1
    saisie_a1.focus()
    saisie_a1.select_range(0,END)
def I_next(event): #fct pour passer à I
    saisie_l.focus()
    saisie_l.select_range(0,END)
def c1_next(event): #fct pour passer à c1
    saisie_c1.focus()
    saisie_c1.select_range(0,END)
# Passage d'une combobox à l'autre  
def update(event):
    global Liste_listboxCharges,Listbox_tab3,liste_charges
    if liste_charges !=[]:
        Listbox_tab3.delete(0,'end')
        ajout_combobox_chargement()
    else:
        ajout_combobox_chargement()
canva_tab3_labelframe1_Combobox1.bind("<<ComboboxSelected>>", update)      
"""
Fin
"""

### left_canvas_2 ###
### Fonction vérif conditions de la rdm ###
def verification_hypotheses_de_la_rdm_section_rectangulaire(hauteur):
    #Vérifie le rapport de x4 pour la géométrie
    if L/hauteur <= 4 :
        showwarning(title="ATTENTION", message="Le calcul va se faire mais les conditions de la RDM ne sont pas respectées ! \nPour plus d'informations, rendez vous dans la rubrique Autres / Conditions de fonctionnement")

def calcul(): # Effectue le calcul sur le bouton calcul
    # valeurs_materiau = [E,Mv,m,Re,nu]
    global tabl_c_concentrée, tabl_c_répartie, tabl_c_répartie_partielle, tabl_c_répartie_partielle_proche, tabl_c_triang, tabl_c_triangulaire_mon,\
        tabl_c_triangulaire_antisy, tabl_c_trapézoïdale_sy, tabl_c_parabolique, tabl_couple, tabl_couple_réparti, \
            tabl_c_décrois, tabl_c_crois, x, Masse, RATotal, RBTota, EffortTranchTotal, MfTotal, ContrainteYMaxTotal,\
                ContrainteMaxTotal,  DefYMaxTotal, DefMaxTotal, flècheTotale, FlècheMaxTotale, valeurs_geometriques, valeurs_materiau
    Igz = valeurs_geometriques[0]
    longueur = valeurs_geometriques[1]
    hauteur = valeurs_geometriques[2]
    volume = valeurs_geometriques[3]
    verification_hypotheses_de_la_rdm_section_rectangulaire(hauteur)
    E = valeurs_materiau[0]
    MasseVol = valeurs_materiau[1]
    # Discrétisations (pour l'instant le pas ne peut pas être choisis mais il pourra l'être plus tard)
    NbrePointsX = int(NbrePointsX_bis.get())
    print('Nombre de points sur les graphes : ', NbrePointsX)
    x = np.linspace(0, longueur, NbrePointsX)
    Somme_c_concentrée = Somme_c_répartie = Somme_c_répartie_partielle = Somme_c_répartie_partielle_proche = Somme_c_triang = Somme_c_triangulaire_mon = Somme_c_triangulaire_antisy = Somme_c_trapézoïdale_sy = Somme_c_parabolique = Somme_couple = Somme_couple_réparti = Somme_c_crois = Somme_c_décrois = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    if str(chargement.get()) == '2 appuis simples' :
        if len(tabl_c_concentrée) != 0 :
            for j in range(classe.charge_concentrée.nbr):
                [RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche] = tabl_c_concentrée[j].charge_concentrée_appuis_simples(hauteur, longueur, Igz, E, x, NbrePointsX)
                conversion = np.array([RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche])
                Somme_c_concentrée = Somme_c_concentrée + conversion
        if len(tabl_c_répartie) != 0:
            for j in range(classe.charge_répartie.nbr):
                [RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche] = tabl_c_répartie[j].charge_répartie_appuis_simples(hauteur, longueur, Igz, E, x)
                conversion = np.array([RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche])
                Somme_c_répartie = Somme_c_répartie + conversion
        if len(tabl_c_répartie_partielle) != 0:
            for j in range(classe.charge_répartie_partielle.nbr):
                [RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche] = tabl_c_répartie_partielle[j].charge_répartie_partielle_appuis_simples(hauteur, longueur, Igz, E, x, NbrePointsX)
                conversion = np.array([RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche])
                Somme_c_répartie_partielle = Somme_c_répartie_partielle + conversion
        if len(tabl_c_répartie_partielle_proche) != 0:
            for j in range(classe.charge_répartie_partielle_proche.nbr):
                [RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche] = tabl_c_répartie_partielle_proche[j].charge_répartie_partielle_proche_appuis_simples(hauteur, longueur, Igz, E, x, NbrePointsX)
                conversion = np.array([RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche])
                Somme_c_répartie_partielle_proche = Somme_c_répartie_partielle_proche + conversion
        if len(tabl_c_triang) != 0:
            for j in range(classe.charge_triangulaire.nbr):
                [RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche] = tabl_c_triang[j].charge_triangulaire_appuis_simples(hauteur, longueur, Igz, E, x, NbrePointsX)
                conversion = np.array([RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche])
                Somme_c_triang = Somme_c_triang + conversion
        if len(tabl_c_triangulaire_mon) != 0:
            for j in range(classe.charge_triangulaire_monotone.nbr):
                [RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche] = tabl_c_triangulaire_mon[j].charge_triangulaire_monotone_appuis_simples(hauteur, longueur, Igz, E, x, NbrePointsX)
                conversion = np.array([RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche])
                Somme_c_triangulaire_mon = Somme_c_triangulaire_mon + conversion
        if len(tabl_c_triangulaire_antisy) != 0:
            for j in range(classe.charge_triangulaire_antisymétrique.nbr):
                [RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche] = tabl_c_triangulaire_antisy[j].charge_triangulaire_antisymétrique_appuis_simples(hauteur, longueur, Igz, E, x, NbrePointsX)
                conversion = np.array([RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche])
                Somme_c_triangulaire_antisy = Somme_c_triangulaire_antisy + conversion
        if len(tabl_c_trapézoïdale_sy) != 0:
            for j in range(classe.charge_trapézoïdale_symétrique.nbr):
                [RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche] = tabl_c_trapézoïdale_sy[j].charge_trapézoïdale_symétrique_appuis_simples(hauteur, longueur, Igz, E, x, NbrePointsX)
                conversion = np.array([RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche])
                Somme_c_trapézoïdale_sy = Somme_c_trapézoïdale_sy + conversion
        if len(tabl_c_parabolique) != 0:
            for j in range(classe.charge_parabolique.nbr):
                [RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche] = tabl_c_parabolique[j].charge_parabolique_appuis_simples(hauteur, longueur, Igz, E, x, NbrePointsX)
                conversion = np.array([RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche])
                Somme_c_parabolique = Somme_c_parabolique + conversion
        if len(tabl_couple) != 0:
            for j in range(classe.couple.nbr):
                [RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche] = tabl_couple[j].couple_appuis_simples(hauteur, longueur, Igz, E, x, NbrePointsX)
                conversion = np.array([RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche])
                Somme_couple = Somme_couple + conversion
        if len(tabl_couple_réparti) != 0:
            for j in range(classe.couple_réparti.nbr):
                [RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche] = tabl_couple_réparti[j].couple_réparti_appuis_simples(hauteur, longueur, Igz, E, x, NbrePointsX)
                conversion = np.array([RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche])
                Somme_couple_réparti = Somme_couple_réparti + conversion
             # SOMME TOTALE :
        RATotal = Somme_c_concentrée[0] + Somme_c_répartie[0] + Somme_c_répartie_partielle[0] + Somme_c_répartie_partielle_proche[0] + Somme_c_triang[0] + Somme_c_triangulaire_mon[0] + Somme_c_triangulaire_antisy[0] + Somme_c_trapézoïdale_sy[0] + Somme_c_parabolique[0] + Somme_couple[0] + Somme_couple_réparti[0]
        RBTotal = Somme_c_concentrée[1] + Somme_c_répartie[1] + Somme_c_répartie_partielle[1] + Somme_c_répartie_partielle_proche[1] + Somme_c_triang[1] + Somme_c_triangulaire_mon[1] + Somme_c_triangulaire_antisy[1] + Somme_c_trapézoïdale_sy[1] + Somme_c_parabolique[1] + Somme_couple[1] + Somme_couple_réparti[1]
        EffortTranchTotal = Somme_c_concentrée[2] + Somme_c_répartie[2] + Somme_c_répartie_partielle[2] + Somme_c_répartie_partielle_proche[2] + Somme_c_triang[2] + Somme_c_triangulaire_mon[2] + Somme_c_triangulaire_antisy[2] + Somme_c_trapézoïdale_sy[2] + Somme_c_parabolique[2] + Somme_couple[2] + Somme_couple_réparti[2]
        MfTotal = Somme_c_concentrée[3] + Somme_c_répartie[3] + Somme_c_répartie_partielle[3] + Somme_c_répartie_partielle_proche[3] + Somme_c_triang[3] + Somme_c_triangulaire_mon[3] + Somme_c_triangulaire_antisy[3] + Somme_c_trapézoïdale_sy[3] + Somme_c_parabolique[3] + Somme_couple[3] + Somme_couple_réparti[3]
        ContrainteYMaxTotal = Somme_c_concentrée[4] + Somme_c_répartie[4] + Somme_c_répartie_partielle[4] + Somme_c_répartie_partielle_proche[4] + Somme_c_triang[4] + Somme_c_triangulaire_mon[4] + Somme_c_triangulaire_antisy[4] + Somme_c_trapézoïdale_sy[4] + Somme_c_parabolique[4] + Somme_couple[4] + Somme_couple_réparti[4]
        ContrainteMaxTotal = np.amax(abs(ContrainteYMaxTotal))
        DefYMaxTotal = Somme_c_concentrée[5] + Somme_c_répartie[5] + Somme_c_répartie_partielle[5] + Somme_c_répartie_partielle_proche[5] + Somme_c_triang[5] + Somme_c_triangulaire_mon[5] + Somme_c_triangulaire_antisy[5] + Somme_c_trapézoïdale_sy[5] + Somme_c_parabolique[5] + Somme_couple[5] + Somme_couple_réparti[5]
        DefMaxTotal = np.amax(abs(DefYMaxTotal))
        flècheTotale = Somme_c_concentrée[6] + Somme_c_répartie[6] + Somme_c_répartie_partielle[6] + Somme_c_répartie_partielle_proche[6] + Somme_c_triang[6] + Somme_c_triangulaire_mon[6] + Somme_c_triangulaire_antisy[6] + Somme_c_trapézoïdale_sy[6] + Somme_c_parabolique[6] + Somme_couple[6] + Somme_couple_réparti[6]
        FlècheMaxTotale = np.amax(abs(flècheTotale))      
        # Dire dans la console calculs lancées        
        print('Calculs appuis simple lancés')
        # Lancer les graphs
        rafraichir()
    elif str(chargement.get()) == '1 encastrement et 1 bord libre' : 
        if len(tabl_c_concentrée) != 0:
            for j in range(classe.charge_concentrée.nbr):
                [RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche] = tabl_c_concentrée[j].charge_concentrée_encastrement(hauteur, longueur, Igz, E, x, NbrePointsX)
                conversion = np.array([RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche])
                Somme_c_concentrée = Somme_c_concentrée + conversion
        if len(tabl_c_répartie) != 0:
            for j in range(classe.charge_répartie.nbr):
                [RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche] = tabl_c_répartie[j].charge_répartie_encastrement(hauteur, longueur, Igz, E, x)
                conversion = np.array([RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche])
                Somme_c_répartie = Somme_c_répartie + conversion
        if len(tabl_c_répartie_partielle) != 0:
            for j in range(classe.charge_répartie_partielle.nbr):
                [RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche] = tabl_c_répartie_partielle[j].charge_répartie_partielle_encastrement(hauteur, longueur, Igz, E, x, NbrePointsX)
                conversion = np.array([RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche])
                Somme_c_répartie_partielle = Somme_c_répartie_partielle_proche + conversion
        if len(tabl_c_crois) != 0:
            for j in range(classe.charge_croissante.nbr):
                [RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche] = tabl_c_crois[j].charge_croissante_encastrement(hauteur, longueur, Igz, E, x)
                conversion = np.array([RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche])
                Somme_c_crois = Somme_c_crois + conversion
        if len(tabl_c_décrois) != 0:
            for j in range(classe.charge_décroissante.nbr):
                [RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche] = tabl_c_décrois[j].charge_décroissante_encastrement(hauteur, longueur, Igz, E, x)
                conversion = np.array([RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche])
                Somme_c_décrois = Somme_c_décrois + conversion
        if len(tabl_couple) != 0:
            for j in range(classe.couple.nbr):
                [RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche] = tabl_couple[j].couple_encastrement(hauteur, longueur, Igz, E, x, NbrePointsX)
                conversion = np.array([RA, RB, EffortTranch, Mf, ContrainteYMax, DefYMax, flèche])
                Somme_couple = Somme_couple + conversion
             # SOMME TOTALE :
        RATotal = Somme_c_concentrée[0] + Somme_c_répartie[0] + Somme_c_répartie_partielle[0] + Somme_c_crois[0] + Somme_c_décrois[0] + Somme_couple[0] 
        RBTotal = Somme_c_concentrée[1] + Somme_c_répartie[1] + Somme_c_répartie_partielle[1]  + Somme_c_crois[1] + Somme_c_décrois[1]  + Somme_couple[1] 
        EffortTranchTotal = Somme_c_concentrée[2] + Somme_c_répartie[2] + Somme_c_répartie_partielle[2]  + Somme_c_crois[2] + Somme_c_décrois[2]  + Somme_couple[2] 
        MfTotal = Somme_c_concentrée[3] + Somme_c_répartie[3] + Somme_c_répartie_partielle[3]  + Somme_c_crois[3] + Somme_c_décrois[3]  + Somme_couple[3] 
        ContrainteYMaxTotal = Somme_c_concentrée[4] + Somme_c_répartie[4] + Somme_c_répartie_partielle[4]  + Somme_c_crois[4] + Somme_c_décrois[4]  + Somme_couple[4] 
        ContrainteMaxTotal = np.amax(abs(ContrainteYMaxTotal))
        DefYMaxTotal = Somme_c_concentrée[5] + Somme_c_répartie[5] + Somme_c_répartie_partielle[5]  + Somme_c_crois[5] + Somme_c_décrois[5]  + Somme_couple[5] 
        DefMaxTotal = np.amax(abs(DefYMaxTotal))
        flècheTotale = Somme_c_concentrée[6] + Somme_c_répartie[6] + Somme_c_répartie_partielle[6] + Somme_c_crois[6] + Somme_c_décrois[6]  + Somme_couple[6] 
        FlècheMaxTotale = np.amax(abs(flècheTotale))  
        # Dire dans la console calculs lancées
        print('Calculs encastrement lancés')
        # Lancer les graphs
        rafraichir()          
### Lancer les Graphiques ###
import matplotlib
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
def rafraichir():
    global canva_tab5, canva_tab6, canva_tab7, canva_tab8, canva_tab9, canva_tab10,canva_tab11,right_canvas1,right_canvas2
    canva_tab5.destroy()
    canva_tab5 = Canvas(tab5, bg=gris_5)
    canva_tab5.place(relx=0.003,rely=0.003,relwidth=0.995, relheight=0.995)
    canva_tab6.destroy()
    canva_tab6 = Canvas(tab6, bg=gris_5)
    canva_tab6.place(relx=0.003,rely=0.003,relwidth=0.995, relheight=0.995)
    canva_tab7.destroy()
    canva_tab7 = Canvas(tab7, bg=gris_5)
    canva_tab7.place(relx=0.003,rely=0.003,relwidth=0.995, relheight=0.995)
    canva_tab8.destroy()
    canva_tab8 = Canvas(tab8, bg=gris_5)
    canva_tab8.place(relx=0.003,rely=0.003,relwidth=0.995, relheight=0.995)
    canva_tab9.destroy()
    canva_tab9 = Canvas(tab9, bg=gris_5)
    canva_tab9.place(relx=0.003,rely=0.003,relwidth=0.995, relheight=0.995)
    canva_tab10.destroy()
    canva_tab10 = Canvas(tab10, bg=gris_5)
    canva_tab10.place(relx=0.003,rely=0.003,relwidth=0.995, relheight=0.995)
    right_canvas1.destroy()
    right_canvas2.destroy()
    right_canvas1=Canvas(canva_tab11, bg=gris_5) # encadré gauche haut
    right_canvas2=Canvas(canva_tab11, bg=gris_5) # encadré gauche bas
    right_canvas1.place(relx=0,rely=0,relwidth=1, relheight=1)
    right_canvas2.place(relx=0,rely=0.5,relwidth=1, relheight=1)
    lancer_le_graph_globaux()
    lancer_le_graph_Effort()
    lancer_le_graph_Mf()
    lancer_le_graph_Contrainte()
    lancer_le_graph_Déformation()
    lancer_le_graph_Flèche()    
    Analyse()
def lancer_le_graph_globaux():
    global tabl_c_trapézoïdale_sy
    ## Effort tranchant graphique  ###
    f = Figure(figsize=(16, 9), dpi=80)
    a = f.add_subplot(231)
    a.plot(x,EffortTranchTotal)
    a.set_xlabel('x [mm]')
    a.set_ylabel('Effort Tranchant T [N]')
    # a.plt.title("Effort Tranchant le long de la poutre") #Titre de la courbe
    b = f.add_subplot(232)
    b.plot(x,MfTotal)
    b.set_xlabel('x [mm]')
    b.set_ylabel('Moment fléchissant Mf [N.mm]')
    # b.plt.title("Tracé du Moment Fléchissant") 
    c = f.add_subplot(233)
    c.plot(x,ContrainteYMaxTotal)
    c.set_xlabel('x [mm]')
    c.set_ylabel('Contrainte Maximale [MPa]')  
    d = f.add_subplot(234)
    d.plot(x,DefYMaxTotal)
    d.set_xlabel('x [mm]')
    d.set_ylabel('Déformation Maximale')
    if len(tabl_c_trapézoïdale_sy) != 0:
        print("pas de flèche disponible pour le moment, car la poutre subit une charge trapézoïdale")
    else :
        e = f.add_subplot(235)
        e.plot(x,flècheTotale)
        e.set_xlabel('x [mm]')
        e.set_ylabel('Flèche Maximale [mm]')
    # tanbouille tkinter pour afficher #
    canvas = FigureCanvasTkAgg(f, master=canva_tab5)
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, canva_tab5)
    toolbar.update()
    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)
    canvas.mpl_connect("key_press_event", on_key_press)
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
def lancer_le_graph_Effort():
    ## Effort tranchant graphique  ###
    f = Figure(figsize=(16, 9), dpi=80)
    a = f.add_subplot(111)
    a.plot(x,EffortTranchTotal)
    # a.plt.title("Effort Tranchant le long de la poutre") #Titre de la courbe
    a.set_xlabel('x [mm]')
    a.set_ylabel('Effort Tranchant T [N]')
    # tanbouille tkinter pour afficher #
    canvas = FigureCanvasTkAgg(f, master=canva_tab6)
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, canva_tab6)
    toolbar.update()
    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)
    canvas.mpl_connect("key_press_event", on_key_press)
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
def lancer_le_graph_Mf():
    ### Mf graphique  ###
    f = Figure(figsize=(16, 9), dpi=80)
    a = f.add_subplot(111)
    a.plot(x,MfTotal)
    # a.plt.title("Tracé du Moment Fléchissant") 
    a.set_xlabel('x [mm]')
    a.set_ylabel('Moment fléchissant Mf [N.mm]')
    # tanbouille tkinter pour afficher #
    canvas = FigureCanvasTkAgg(f, master=canva_tab7)
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, canva_tab7)
    toolbar.update()
    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)
    canvas.mpl_connect("key_press_event", on_key_press)
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)    
def lancer_le_graph_Contrainte():
    ### Contrainte graphique  ###
    f = Figure(figsize=(16, 9), dpi=80)
    a = f.add_subplot(111)
    a.plot(x,ContrainteYMaxTotal)
    a.set_xlabel('x [mm]')
    a.set_ylabel('Contrainte Maximale [MPa]')
    # tanbouille tkinter pour afficher #
    canvas = FigureCanvasTkAgg(f, master=canva_tab8)
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, canva_tab8)
    toolbar.update()
    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)
    canvas.mpl_connect("key_press_event", on_key_press)
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)    
def lancer_le_graph_Déformation():
    ### Déformations graphique  ###
    f = Figure(figsize=(16, 9), dpi=80)
    a = f.add_subplot(111)
    a.plot(x,DefYMaxTotal)
    a.set_xlabel('x [mm]')
    a.set_ylabel('Déformation Maximale')
    # tanbouille tkinter pour afficher #
    canvas = FigureCanvasTkAgg(f, master=canva_tab9)
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, canva_tab9)
    toolbar.update()
    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)
    canvas.mpl_connect("key_press_event", on_key_press)
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)    
def lancer_le_graph_Flèche():
    global tabl_c_trapézoïdale_sy
    if len(tabl_c_trapézoïdale_sy) != 0:
        print("pas de flèche disponible pour le moment, car la poutre subit une charge trapézoïdale")
    else :
        ### Flèche graphique  ###
        f = Figure(figsize=(16, 9), dpi=80)
        a = f.add_subplot(111)
        a.plot(x,flècheTotale)
        a.set_xlabel('x [mm]')
        a.set_ylabel('Flèche [mm]')
         # tanbouille tkinter pour afficher #
        canvas = FigureCanvasTkAgg(f, master=canva_tab10)
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, canva_tab10)
        toolbar.update()
        def on_key_press(event):
            print("you pressed {}".format(event.key))
            key_press_handler(event, canvas, toolbar)
        canvas.mpl_connect("key_press_event", on_key_press)
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)   
### Bouton Calculer ####
bouton_calculer= Button(left_canvas2, justify='center',text="Calculer",textvariable="Re-Calculer",relief="raised",overrelief="groove", font=("Tahoma", 20,"bold"),activebackground=gris_1,cursor='spraycan', bg=gris_3, fg ="white", command=calcul)
bouton_calculer.place(relx=0.5,rely=0.45,relwidth=0.5, relheight=0.5,anchor='center') # afficher le bouton
bouton_calculer.configure(state=DISABLED, background=gris_5)
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
canva_tab4 = Canvas(tab4, bg=gris_7)
canva_tab4.place(relx=0.003,rely=0.003,relwidth=0.995, relheight=0.995)
bienvenue_message1=Label(canva_tab4,fg="red",font=font_titre1,text='Bienvenue sur Solve Structure',bg=gris_7) #définit le message 1
bienvenue_message1.place(relx=0.13,rely=0.24)
logo_1 = PhotoImage(file='images/105286100_1375318509324214_8360492095536146396_n.png')
logo_2 = PhotoImage(file='images/EPF-couleur.png')
labellogo_1=Label(canva_tab4,image=logo_1)
labellogo_1.image = img_charge_moment_encas
labellogo_1.place(relx=0.51,rely=0.35)
labellogo_2=Label(canva_tab4,image=logo_2)
labellogo_2.image = img_charge_moment_encas
labellogo_2.place(relx=0.10,rely=0.40)
bienvenue_message2=Label(canva_tab4,fg="black",font=font_titre2,text='A la demande de l\'EPF, une equipe d\'étudiants a mis en place le logiciel Solve Structure qui est un programme ayant pour intérêt d\'étudier les effets d\'une ou plusieurs charges sur une structure.',wraplength=800,bg=gris_7) #définit le message 2
bienvenue_message2.place(relx=0.15,rely=0.70)
"""
Fin
"""
### Barre 2 : Graphiques Globaux ###
tab5 = ttk.Frame(notebook2, style='TFrame') # Creation de la barre 5
img5 = PhotoImage(file='images/statistics.png')
notebook2.add(tab5, text='Graphiques Globaux',image=img5, compound=LEFT) # Ajout de la barre 1 au notebook
canva_tab5 = Canvas(tab5, bg=gris_5)
canva_tab5.place(relx=0.003,rely=0.003,relwidth=0.995, relheight=0.995)
"""
Fin
"""

### Barre 3 : Effort Tranchant ###
# , MfTotal, ContrainteYMaxTotal, ContrainteMaxTotal,  DefYMaxTotal, DefMaxTotal, flècheTotale, FlècheMaxTotale
tab6 = ttk.Frame(notebook2, style='TFrame') # Creation de la barre 6
img6 = PhotoImage(file='images/analysis (1).png')
notebook2.add(tab6, text='Effort Tranchant',image=img6, compound=LEFT) # Ajout de la barre 1 au notebook
canva_tab6 = Canvas(tab6, bg=gris_5)
canva_tab6.place(relx=0.003,rely=0.003,relwidth=0.995, relheight=0.995)
### Barre 4 : Moment fléchissant ###
tab7 = ttk.Frame(notebook2, style='TFrame') # Creation de la barre 6
img7 = PhotoImage(file='images/analysis (1).png')
notebook2.add(tab7, text='Moment fléchissant',image=img7, compound=LEFT) # Ajout de la barre 1 au notebook
canva_tab7 = Canvas(tab7, bg=gris_5)
canva_tab7.place(relx=0.003,rely=0.003,relwidth=0.995, relheight=0.995)
### Barre 5 : Contrainte pour y=h/2 ###
tab8 = ttk.Frame(notebook2, style='TFrame') # Creation de la barre 6
img8 = PhotoImage(file='images/analysis (1).png')
notebook2.add(tab8, text='Contrainte Maximale',image=img8, compound=LEFT) # Ajout de la barre 1 au notebook
canva_tab8 = Canvas(tab8, bg=gris_5)
canva_tab8.place(relx=0.003,rely=0.003,relwidth=0.995, relheight=0.995)
### Barre 6 : Déformations ###
tab9 = ttk.Frame(notebook2, style='TFrame') # Creation de la barre 6
img9 = PhotoImage(file='images/analysis (1).png')
notebook2.add(tab9, text='Déformation Maximale',image=img9, compound=LEFT) # Ajout de la barre 1 au notebook
canva_tab9 = Canvas(tab9, bg=gris_5)
canva_tab9.place(relx=0.003,rely=0.003,relwidth=0.995, relheight=0.995)
### Barre 7 : Flèche ###
tab10 = ttk.Frame(notebook2, style='TFrame') # Creation de la barre 6
img10 = PhotoImage(file='images/analysis (1).png')
notebook2.add(tab10, text='Flèche',image=img10, compound=LEFT) # Ajout de la barre 1 au notebook
canva_tab10 = Canvas(tab10, bg=gris_5)
canva_tab10.place(relx=0.003,rely=0.003,relwidth=0.995, relheight=0.995)
"""
Fin
"""

### Barre 8 : Analyse ###
tab11 = ttk.Frame(notebook2, style='TFrame') # Creation de la barre 7
img11 = PhotoImage(file='images/analysis.png')
notebook2.add(tab11, text='Analyse',image=img11, compound=LEFT) # Ajout de la barre 1 au notebook
canva_tab11 = Canvas(tab11, bg=gris_5)
canva_tab11.place(relx=0,rely=0,relwidth=1, relheight=1)
# left frame en 2 canvas
right_canvas1=Canvas(canva_tab11, bg=gris_5) # encadré gauche haut
right_canvas2=Canvas(canva_tab11, bg=gris_5) # encadré gauche bas
# placement des deux 2 canvas de left_frame
right_canvas1.place(relx=0,rely=0,relwidth=1, relheight=1)
right_canvas2.place(relx=0,rely=0.5,relwidth=1, relheight=1)  
poucerouge = PhotoImage(file='images/feedback (1).png')
poucevert = PhotoImage(file='images/feedback.png')
def Analyse():
    lancer_le_graph_Contrainte_analyse()     
    if ContrainteMaxTotal>=Re or ContrainteMaxTotal<=(-Re):
        Label1 = Label(right_canvas2,text="La poutre ne supporte pas la charge qui lui est contraint",bg=gris_5,fg="red",font = ("Arial",11,"bold"))
        labelpouce=Label(right_canvas2,image=poucerouge,bg=gris_5)
        labelpouce.image = poucerouge
        Label2= Label(right_canvas2,text="Contrainte totale Maximale [MPa] = ",bg=gris_5,fg="red",font = ("Arial",11,"bold"))
        Label2_bis= Label(right_canvas2,text=ContrainteMaxTotal,bg=gris_5,fg="red",font = ("Arial",11,"bold"))
        Label3= Label(right_canvas2,text="Déformation totale Maximale = ",bg=gris_5,fg="red",font = ("Arial",11,"bold"))
        Label3_bis= Label(right_canvas2,text=DefMaxTotal,bg=gris_5,fg="red",font = ("Arial",11,"bold"))
        Label4= Label(right_canvas2,text="Flèche totale Maximale [mm] = ",bg=gris_5,fg="red",font = ("Arial",11,"bold"))
        Label4_bis= Label(right_canvas2,text=FlècheMaxTotale,bg=gris_5,fg="red",font = ("Arial",11,"bold"))
    elif ContrainteMaxTotal<=Re or ContrainteMaxTotal>=(-Re):
        Label1 = Label(right_canvas2,text="La poutre supporte la charge qui lui est contraint",bg=gris_5,fg="red",font = ("Arial",11,"bold"))
        labelpouce=Label(right_canvas2,image=poucevert,bg=gris_5)
        labelpouce.image = poucevert
        Label2= Label(right_canvas2,text="Contrainte totale Maximale [MPa] = ",bg=gris_5,fg="red",font = ("Arial",11,"bold"))
        Label2_bis= Label(right_canvas2,text=ContrainteMaxTotal,bg=gris_5,fg="red",font = ("Arial",11,"bold"))
        Label3= Label(right_canvas2,text="Déformation totale Maximale = ",bg=gris_5,fg="red",font = ("Arial",11,"bold"))
        Label3_bis= Label(right_canvas2,text=DefMaxTotal,bg=gris_5,fg="red",font = ("Arial",11,"bold"))
        Label4= Label(right_canvas2,text="Flèche totale Maximale [mm] = ",bg=gris_5,fg="red",font = ("Arial",11,"bold"))
        Label4_bis= Label(right_canvas2,text=FlècheMaxTotale,bg=gris_5,fg="red",font = ("Arial",11,"bold"))
    labelpouce.pack(anchor='center')
    Label1.pack(anchor='w')
    Label2.pack(anchor='w')
    Label2_bis.pack(anchor='w')
    Label3.pack(anchor='w')
    Label3_bis.pack(anchor='w')
    Label4.pack(anchor='w')
    Label4_bis.pack(anchor='w')
def lancer_le_graph_Contrainte_analyse():
     ### Contrainte graphique Analyse ###
     f = Figure(figsize=(10, 4), dpi=80)
     a = f.add_subplot(111)
     a.plot(x,ContrainteYMaxTotal)
     a.axhline(y=Re)
     a.axhline(y=-Re)
     a.set_xlabel('x [mm]')
     a.set_ylabel('Contrainte Maximale [MPa]')
     # tanbouille tkinter pour afficher #
     canvas = FigureCanvasTkAgg(f, master=right_canvas1)
     canvas.draw()
     toolbar = NavigationToolbar2Tk(canvas, right_canvas1)
     toolbar.update()
     def on_key_press(event):
         print("you pressed {}".format(event.key))
         key_press_handler(event, canvas, toolbar)
     canvas.mpl_connect("key_press_event", on_key_press)
     canvas.get_tk_widget().place(relx=0,rely=0,relwidth=1, relheight=0.5) 

"""
Fin
"""

### Démarrage ###
main.mainloop()
"""
Fin
"""