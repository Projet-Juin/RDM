# -*- coding: utf-8 -*-
"""
@author: Forjot Henri

Création du main

"""
### IMPORTATIONS ###
from tkinter import *
from appel_fonctions_annexes import *
from gestion_des_entrees import *
from gestion_des_calculs import *
from tkinter import ttk
from tkinter.messagebox import *

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
main.geometry("%dx%d" % (width,height))
# main.resizable(width=FALSE, height=FALSE) #empêche de déformer la fenetre
"""
Fin
"""

### Creation d'une Barre de menu ###
barre_de_menu = Menu(main, tearoff=0)
main.config(menu=barre_de_menu)
# Création d'un menu fichier et ajout d'items
fichier_menu = Menu(barre_de_menu,activebackground=gris_clair, tearoff=0) # Création d'un menu fichier
fichier_menu.add_command(label='Ouvrir',command=ouvrir) # ajout de l'item ouvrir
fichier_menu.add_command(label='Sauvegarder            (Ctrl+S)',command=sauvegarder) # ajout de l'item sauvegarder
fichier_menu.add_command(label='Sauvegarder Sous   (Shift+Ctrl+S)',command=sauvegarder_sous) # ajout de l'item sauvegarder sous
fichier_menu.add_command(label='Redémarrer',command=reboot_programme) # ajout de l'item redémarrer
fichier_menu.add_separator() #ajout d'un separateur
fichier_menu.add_command(label='Quitter',command=main.destroy) # ajout de l'item quitter (ou sys.exit)
# Création d'un menu éléments finis et ajout d'items
elts_finis_menu = Menu(barre_de_menu,activebackground=gris_clair, tearoff=0) # Création d'un menu élts finis
elts_finis_menu.add_command(label='Switch vers Éléments finis',command=switch_elts_finis) # ajout de l'item permettant d'aller en élément finis
elts_finis_menu.add_separator() #ajout d'un separateur
elts_finis_menu.add_command(label='Importer les Inputs d\'Éléments finis',command=import_elts_finis) # ajout de l'item permettant d'importer les données d'éléments finis
elts_finis_menu.add_command(label='Exporter les Inputs d\'Éléments finis',command=export_elts_finis) # ajout de l'item permettant d'exporter les données d'éléments finis
# Création d'un menu autres et ajout d'items
autres_menu = Menu(barre_de_menu,activebackground=gris_clair, tearoff=0) # Création d'un menu autres
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

### Création de 2 frames principales ###
# Fenetre principale en 2 frames
left_frame= Frame(main, bg="blue") # encadré gauche
right_frame = Frame(main, bg='green') #encadré droite
# left frame en 2 canvas
left_canvas1=Canvas(left_frame, bg="purple") # encadré gauche haut
left_canvas2=Canvas(left_frame, bg="red") # encadré gauche bas
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
notebook = ttk.Notebook(left_canvas1,height=900,width=500) # Creation du Notebook
notebook.enable_traversal() # permet de swtich avec le clavier d'un tab à l'autre [Ctl+tab,Ctrl+shift+tab,Alt+K]
notebook.pack(expand=1, fill='both') # on place le notebook
"""
Fin
"""

### Barre 1 : Géométrie ###
tab1 = ttk.Frame(notebook) # Creation de la barre 1
notebook.add(tab1, text='Géométrie') # Ajout de la barre 1 au notebook
canva_tab1 = Canvas(tab1, bg="yellow")
canva_tab1.pack(expand=1, fill='both')
# Création labelframe 1
canva_tab1_labelframe1 = LabelFrame(canva_tab1,font = ("Arial",14 , "bold"),text = 'Type de section',bg = gris_fonce) #définit le message 1
canva_tab1_labelframe1.place(relx=0.01,rely=0.01,relwidth=0.98, relheight=0.10) # affiche le labelframe type de section    
# Choisir quelle est la géométrie du problème
canva_tab1_labelframe1_label = Label(canva_tab1_labelframe1,text = "Choissiez le type de géométrie de votre poutre :")
canva_tab1_labelframe1_label.grid(row=0)
geometrie = StringVar()
canva_tab1_labelframe1_Combobox1 = ttk.Combobox(canva_tab1_labelframe1, textvariable = geometrie , state = "readonly")
canva_tab1_labelframe1_Combobox1['values'] = ("","Rectangle", "Carré", "Forme", "Triangle", "Cercle", "Losange")
canva_tab1_labelframe1_Combobox1.grid(row=1) # affichage de la combobox
canva_tab1_labelframe1_Combobox1.current(0) # onglet actif dans la combobox quand on démarre 
def ajout_combobox(event):
    global geometrie2,geometrie3,geometrie4,geometrie5,geometrie6
    print("Sélection en cours du Combobox 1 :  index <",canva_tab1_labelframe1_Combobox1.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox1.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
    if str(geometrie.get()) == 'Rectangle':
        geometrie2 = StringVar()
        canva_tab1_labelframe1_Combobox2 = ttk.Combobox(canva_tab1_labelframe1, textvariable = geometrie2 , state = "readonly")
        canva_tab1_labelframe1_Combobox2['values'] = ("","Normal","Troué")
        canva_tab1_labelframe1_Combobox2.grid(row=3) # affichage de la combobox
        canva_tab1_labelframe1_Combobox2.current(0) # onglet actif dans la combobox quand on démarre
        # Passage d'une combobox à l'autre   
        canva_tab1_labelframe1_Combobox2.bind("<<ComboboxSelected>>", nouveau_labelframe)
        print("Sélection en cours du Combobox 2 :  index <",canva_tab1_labelframe1_Combobox2.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox2.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
    if str(geometrie.get()) == 'Carré':
        geometrie3 = StringVar()
        canva_tab1_labelframe1_Combobox3 = ttk.Combobox(canva_tab1_labelframe1, textvariable = geometrie3 , state = "readonly")
        canva_tab1_labelframe1_Combobox3['values'] = ("","Normal","Troué")
        canva_tab1_labelframe1_Combobox3.grid(row=3) # affichage de la combobox
        canva_tab1_labelframe1_Combobox3.current(0) # onglet actif dans la combobox quand on démarre
        # Passage d'une combobox à l'autre   
        canva_tab1_labelframe1_Combobox3.bind("<<ComboboxSelected>>", nouveau_labelframe) 
        print("Sélection en cours du Combobox 3 :  index <",canva_tab1_labelframe1_Combobox3.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox3.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
    if str(geometrie.get()) == 'Forme':
        geometrie4 = StringVar()
        canva_tab1_labelframe1_Combobox4 = ttk.Combobox(canva_tab1_labelframe1, textvariable = geometrie4 , state = "readonly")
        canva_tab1_labelframe1_Combobox4['values'] = ("","I","T","L","Z","Croix")
        canva_tab1_labelframe1_Combobox4.grid(row=3) # affichage de la combobox
        canva_tab1_labelframe1_Combobox4.current(0) # onglet actif dans la combobox quand on démarre
        # Passage d'une combobox à l'autre   
        canva_tab1_labelframe1_Combobox4.bind("<<ComboboxSelected>>", nouveau_labelframe)
        print("Sélection en cours du Combobox 4 :  index <",canva_tab1_labelframe1_Combobox4.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox4.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
    if str(geometrie.get()) == 'Triangle':
        geometrie5 = StringVar()
        canva_tab1_labelframe1_Combobox5 = ttk.Combobox(canva_tab1_labelframe1, textvariable = geometrie5 , state = "readonly")
        canva_tab1_labelframe1_Combobox5['values'] = ("","Rectangle")
        canva_tab1_labelframe1_Combobox5.grid(row=3) # affichage de la combobox
        canva_tab1_labelframe1_Combobox5.current(0) # onglet actif dans la combobox quand on démarre
        # Passage d'une combobox à l'autre   
        canva_tab1_labelframe1_Combobox5.bind("<<ComboboxSelected>>", nouveau_labelframe)
        print("Sélection en cours du Combobox 5 :  index <",canva_tab1_labelframe1_Combobox5.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox5.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
    if str(geometrie.get()) == 'Cercle':
        geometrie6 = StringVar()
        canva_tab1_labelframe1_Combobox6 = ttk.Combobox(canva_tab1_labelframe1, textvariable = geometrie6 , state = "readonly")
        canva_tab1_labelframe1_Combobox6['values'] = ("","Normal","Troué","Demi Cercle","Quart de Cercle","Ovale")
        canva_tab1_labelframe1_Combobox6.grid(row=3) # affichage de la combobox
        canva_tab1_labelframe1_Combobox6.current(0) # onglet actif dans la combobox quand on démarre
        # Passage d'une combobox à l'autre   
        canva_tab1_labelframe1_Combobox6.bind("<<ComboboxSelected>>", nouveau_labelframe)
        print("Sélection en cours du Combobox 6 :  index <",canva_tab1_labelframe1_Combobox6.current(),"> et intitulé <", canva_tab1_labelframe1_Combobox6.get(),">") # afficher index et valeur du choix du comboxbox dans le cmd
    if str(geometrie.get()) == 'Losange': 
        canva_tab1_labelframe1_Combobox1.bind("<<ComboboxSelected>>", nouveau_labelframe)
def nouveau_labelframe(event): # nouvelle frame où on rentre les données
    global label_longueur,label_largeur,label_largeur1,label_largeur2,label_rayon,label_rayon1\
        ,label_hauteur,label_hauteur1,label_diagonale1,label_diagonale2\
            ,saisie_longueur,saisie_largeur,saisie_largeur1,saisie_largeur2,saisie_rayon,saisie_rayon1\
                ,saisie_hauteur,saisie_hauteur1,saisie_diagonale1,saisie_diagonale2\
                    ,canva_tab1_labelframe2
    # Création labelframe 1
    canva_tab1_labelframe2 = LabelFrame(canva_tab1,font = ("Arial",14 , "bold"),text = 'Données',bg = gris_fonce) #définit le message 2
    canva_tab1_labelframe2.place(relx=0.01,rely=0.15,relwidth=0.98, relheight=0.35) # affiche le labelframe type de section   
    if str(geometrie.get()) == 'Rectangle':
        if str(geometrie2.get()) == 'Normal':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Longueur L de votre poutre en mm :')
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Largeur b de votre poutre en mm :')
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Hauteur h de votre poutre en mm :')
            # saisie des inputs L,b,h
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_largeur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_hauteur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            # Placement des items sur une grille
            label_longueur.grid(row=0)
            saisie_longueur.grid(row=1)
            label_largeur.grid(row=2)
            saisie_largeur.grid(row=3)
            label_hauteur.grid(row=4)
            saisie_hauteur.grid(row=5)
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
            # lancement retour des touches
            saisie_longueur.bind('<Return>', detection_passage)
        if str(geometrie2.get()) == 'Troué':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Longueur L de votre poutre en mm :')
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Largeur b de votre poutre en mm :')
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Hauteur h de votre poutre en mm :')
            label_largeur1 = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Largeur b1 de votre poutre en mm :')
            label_hauteur1 = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Hauteur h1 de votre poutre en mm :')
            # saisie des inputs L,b,h
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_largeur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_hauteur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_largeur1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_hauteur1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            # Placement des items sur une grille
            label_longueur.grid(row=0)
            saisie_longueur.grid(row=1)
            label_largeur.grid(row=2)
            saisie_largeur.grid(row=3)
            label_hauteur.grid(row=4)
            saisie_hauteur.grid(row=5)
            label_largeur1.grid(row=6)
            saisie_largeur1.grid(row=7)
            label_hauteur1.grid(row=8)
            saisie_hauteur1.grid(row=9)
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
            # lancement retour des touches
            saisie_longueur.bind('<Return>', detection_passage)
    if str(geometrie.get()) == 'Carré':
        if str(geometrie3.get()) == 'Normal':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Longueur L de votre poutre en mm :')
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Largeur b de votre poutre en mm :')
            # saisie des inputs L,b,h
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_largeur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            # Placement des items sur une grille
            label_longueur.grid(row=0)
            saisie_longueur.grid(row=1)
            label_largeur.grid(row=2)
            saisie_largeur.grid(row=3)
            # saisie affichage de départ
            saisie_longueur.insert(0, "0.0")
            saisie_largeur.insert(0, "0.0")  
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_longueur.focus() 
            saisie_longueur.select_range(0,END)
            # main au dessus de la case
            saisie_longueur.config(cursor='hand1')
            saisie_largeur.config(cursor='hand1')
            # lancement retour des touches
            saisie_longueur.bind('<Return>', detection_passage)
        if str(geometrie3.get()) == 'Troué':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Longueur L de votre poutre en mm :')
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Largeur b de votre poutre en mm :')
            label_largeur1 = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Largeur b1 de votre poutre en mm :')
            # saisie des inputs L,b,h
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_largeur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_largeur1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            # Placement des items sur une grille
            label_longueur.grid(row=0)
            saisie_longueur.grid(row=1)
            label_largeur.grid(row=2)
            saisie_largeur.grid(row=3)
            label_largeur1.grid(row=4)
            saisie_largeur1.grid(row=5)
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
            # lancement retour des touches
            saisie_longueur.bind('<Return>', detection_passage)
    if str(geometrie.get()) == 'Forme':
        if str(geometrie4.get()) == 'I':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Longueur L de votre poutre en mm :')
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Largeur b de votre poutre en mm :')
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Hauteur h de votre poutre en mm :')
            label_largeur1 = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Largeur de l’aile supérieure b1 de votre poutre en mm :')
            label_largeur2 = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Largeur de l’aile inférieure b2 de votre poutre en mm :')
            label_hauteur1 = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Hauteur du tronc h1 de votre poutre en mm :')
            # saisie des inputs L,b,h
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_largeur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_hauteur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_largeur1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_largeur2 = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_hauteur1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            # Placement des items sur une grille
            label_longueur.grid(row=0)
            saisie_longueur.grid(row=1)
            label_largeur.grid(row=2)
            saisie_largeur.grid(row=3)
            label_hauteur.grid(row=4)
            saisie_hauteur.grid(row=5)
            label_largeur1.grid(row=6)
            saisie_largeur1.grid(row=7)
            label_largeur2.grid(row=8)
            saisie_largeur2.grid(row=9)
            label_hauteur1.grid(row=10)
            saisie_hauteur1.grid(row=11)
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
            # lancement retour des touches
            saisie_longueur.bind('<Return>', detection_passage)
        if str(geometrie4.get()) == 'T':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Longueur L de votre poutre en mm :')
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Largeur b de votre poutre en mm :')
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Hauteur h de votre poutre en mm :')
            label_largeur1 = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Largeur de l’aile b1 de votre poutre en mm :')
            label_hauteur1 = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Hauteur du tronc h1 de votre poutre en mm :')
            # saisie des inputs L,b,h
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_largeur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_hauteur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_largeur1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_hauteur1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            # Placement des items sur une grille
            label_longueur.grid(row=0)
            saisie_longueur.grid(row=1)
            label_largeur.grid(row=2)
            saisie_largeur.grid(row=3)
            label_hauteur.grid(row=4)
            saisie_hauteur.grid(row=5)
            label_largeur1.grid(row=6)
            saisie_largeur1.grid(row=7)
            label_hauteur1.grid(row=8)
            saisie_hauteur1.grid(row=9)
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
            # lancement retour des touches
            saisie_longueur.bind('<Return>', detection_passage)
        if str(geometrie4.get()) == 'L':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Longueur L de votre poutre en mm :')
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Largeur b de votre poutre en mm :')
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Hauteur h de votre poutre en mm :')
            label_largeur1 = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Largeur de l’aile b1 de votre poutre en mm :')
            label_hauteur1 = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Hauteur du tronc h1 de votre poutre en mm :')
            # saisie des inputs L,b,h
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_largeur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_hauteur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_largeur1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_hauteur1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            # Placement des items sur une grille
            label_longueur.grid(row=0)
            saisie_longueur.grid(row=1)
            label_largeur.grid(row=2)
            saisie_largeur.grid(row=3)
            label_hauteur.grid(row=4)
            saisie_hauteur.grid(row=5)
            label_largeur1.grid(row=6)
            saisie_largeur1.grid(row=7)
            label_hauteur1.grid(row=8)
            saisie_hauteur1.grid(row=9)
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
            # lancement retour des touches
            saisie_longueur.bind('<Return>', detection_passage)
        if str(geometrie4.get()) == 'Z':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Longueur L de votre poutre en mm :')
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Largeur b de votre poutre en mm :')
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Hauteur h de votre poutre en mm :')
            label_largeur1 = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Largeur de l’aile b1 de votre poutre en mm :')
            label_largeur2 = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Largeur de l’aile inférieure b2 de votre poutre en mm :')
            label_hauteur1 = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Hauteur du tronc h1 de votre poutre en mm :')
            # saisie des inputs L,b,h
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_largeur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_hauteur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_largeur1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_largeur2 = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_hauteur1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            # Placement des items sur une grille
            label_longueur.grid(row=0)
            saisie_longueur.grid(row=1)
            label_largeur.grid(row=2)
            saisie_largeur.grid(row=3)
            label_hauteur.grid(row=4)
            saisie_hauteur.grid(row=5)
            label_largeur1.grid(row=6)
            saisie_largeur1.grid(row=7)
            label_largeur2.grid(row=8)
            saisie_largeur2.grid(row=9)
            label_hauteur1.grid(row=10)
            saisie_hauteur1.grid(row=11)
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
            # lancement retour des touches
            saisie_longueur.bind('<Return>', detection_passage)
        if str(geometrie4.get()) == 'Croix':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Longueur L de votre poutre en mm :')
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Largeur b de votre poutre en mm :')
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Hauteur h de votre poutre en mm :')
            # saisie des inputs L,b,h
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_largeur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_hauteur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            # Placement des items sur une grille
            label_longueur.grid(row=0)
            saisie_longueur.grid(row=1)
            label_largeur.grid(row=2)
            saisie_largeur.grid(row=3)
            label_hauteur.grid(row=4)
            saisie_hauteur.grid(row=5)
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
            # lancement retour des touches
            saisie_longueur.bind('<Return>', detection_passage)  
    if str(geometrie.get()) == 'Triangle':
        if str(geometrie5.get()) == 'Rectangle':
            # messages des inputs L,b,h
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Longueur L de votre poutre en mm :')
            label_largeur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Largeur b de votre poutre en mm :')
            label_hauteur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Hauteur h de votre poutre en mm :')
            # saisie des inputs L,b,h
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_largeur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_hauteur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            # Placement des items sur une grille
            label_longueur.grid(row=0)
            saisie_longueur.grid(row=1)
            label_largeur.grid(row=2)
            saisie_largeur.grid(row=3)
            label_hauteur.grid(row=4)
            saisie_hauteur.grid(row=5)
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
            # lancement retour des touches
            saisie_longueur.bind('<Return>', detection_passage)
    if str(geometrie.get()) == 'Cercle':
        if str(geometrie6.get()) == 'Normal':
            # messages des inputs L,R
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Longueur L de votre poutre en mm :')
            label_rayon = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer le Rayon R de votre poutre en mm :')
            # saisie des inputs L,R
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_rayon = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            # Placement des items sur une grille
            label_longueur.grid(row=0)
            saisie_longueur.grid(row=1)
            label_rayon.grid(row=2)
            saisie_rayon.grid(row=3)
            # saisie affichage de départ        
            saisie_longueur.insert(0, "0.0") # saisie affichage de départ
            saisie_rayon.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_longueur.focus() 
            saisie_longueur.select_range(0,END)
            # main au dessus de la case
            saisie_longueur.config(cursor='hand1')
            saisie_rayon.config(cursor='hand1')
            # lancement retour des touches
            saisie_longueur.bind('<Return>', detection_passage)
        if str(geometrie6.get()) == 'Troué':
            # messages des inputs L,R
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Longueur L de votre poutre en mm :')
            label_rayon = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer le Rayon R de votre poutre en mm :')
            label_rayon1 = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer le Rayon R1 de votre poutre en mm :')
            # saisie des inputs L,R
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_rayon = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_rayon1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            # Placement des items sur une grille
            label_longueur.grid(row=0)
            saisie_longueur.grid(row=1)
            label_rayon.grid(row=2)
            saisie_rayon.grid(row=3)
            label_rayon1.grid(row=4)
            saisie_rayon1.grid(row=5)
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
            # lancement retour des touches
            saisie_longueur.bind('<Return>', detection_passage)
        if str(geometrie6.get()) == 'Demi Cercle':
            # messages des inputs L,R
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Longueur L de votre poutre en mm :')
            label_rayon = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer le Rayon R de votre poutre en mm :')
            # saisie des inputs L,R
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_rayon = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            # Placement des items sur une grille
            label_longueur.grid(row=0)
            saisie_longueur.grid(row=1)
            label_rayon.grid(row=2)
            saisie_rayon.grid(row=3)
            # saisie affichage de départ        
            saisie_longueur.insert(0, "0.0") # saisie affichage de départ
            saisie_rayon.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_longueur.focus() 
            saisie_longueur.select_range(0,END)
            # main au dessus de la case
            saisie_longueur.config(cursor='hand1')
            saisie_rayon.config(cursor='hand1')
            # lancement retour des touches
            saisie_longueur.bind('<Return>', detection_passage)
        if str(geometrie6.get()) == 'Quart de Cercle':
            # messages des inputs L,R
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Longueur L de votre poutre en mm :')
            label_rayon = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer le Rayon R de votre poutre en mm :')
            # saisie des inputs L,R
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_rayon = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            # Placement des items sur une grille
            label_longueur.grid(row=0)
            saisie_longueur.grid(row=1)
            label_rayon.grid(row=2)
            saisie_rayon.grid(row=3)
            # saisie affichage de départ        
            saisie_longueur.insert(0, "0.0") # saisie affichage de départ
            saisie_rayon.insert(0, "0.0") # saisie affichage de départ
            # refait le focus automatique sur la première case dès qu'on change le choix du combobox et sélection entière
            saisie_longueur.focus() 
            saisie_longueur.select_range(0,END)
            # main au dessus de la case
            saisie_longueur.config(cursor='hand1')
            saisie_rayon.config(cursor='hand1')
            # lancement retour des touches
            saisie_longueur.bind('<Return>', detection_passage)
        if str(geometrie6.get()) == 'Ovale':
            # messages des inputs L,R
            label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Longueur L de votre poutre en mm :')
            label_diagonale1 = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la grande diagonale D1 de votre poutre en mm :')
            label_diagonale2 = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la petite diagonale D2 de votre poutre en mm :')
            # saisie des inputs L,R
            saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_diagonale1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            saisie_diagonale2 = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
            # Placement des items sur une grille
            label_longueur.grid(row=0)
            saisie_longueur.grid(row=1)
            label_diagonale1.grid(row=2)
            saisie_diagonale1.grid(row=3)
            label_diagonale2.grid(row=4)
            saisie_diagonale2.grid(row=5)
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
            # lancement retour des touches
            saisie_longueur.bind('<Return>', detection_passage)
    if str(geometrie.get()) == 'Losange':
        # messages des inputs L,b,h
        label_longueur = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la Longueur L de votre poutre en mm :')
        label_diagonale1 = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la grande diagonale D1 de votre poutre en mm :')
        label_diagonale2 = Label(canva_tab1_labelframe2,font = ("Arial",10),text = 'Entrer la petite diagonale D2 de votre poutre en mm :')
        # saisie des inputs L,b,h
        saisie_longueur = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
        saisie_diagonale1 = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
        saisie_diagonale2 = Entry(canva_tab1_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
        # Placement des items sur une grille
        label_longueur.grid(row=0)
        saisie_longueur.grid(row=1)
        label_diagonale1.grid(row=2)
        saisie_diagonale1.grid(row=3)
        label_diagonale2.grid(row=4)
        saisie_diagonale2.grid(row=5)
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
        # lancement retour des touches
        saisie_longueur.bind('<Return>', detection_passage)
# Gestion du stockage des valeurs pour le bouton
def valider_la_géométrie():
    global label_longueur,label_largeur,label_largeur1,label_largeur2,label_rayon,label_rayon1\
        ,label_hauteur,label_hauteur1,label_diagonale1,label_diagonale2\
            ,saisie_longueur,saisie_largeur,saisie_largeur1,saisie_largeur2,saisie_rayon,saisie_rayon1\
                ,saisie_hauteur,saisie_hauteur1,saisie_diagonale1,saisie_diagonale2\
                    ,canva_tab1_labelframe2,valeurs_geometriques
    L = float(saisie_longueur.get())
    b = float(saisie_largeur.get())
    b1 = float(saisie_largeur1.get())
    b2 = float(saisie_largeur2.get())
    h = float(saisie_hauteur.get())
    h1 = float(saisie_hauteur1.get())
    R = float(saisie_rayon.get())
    R1 = float(saisie_rayon1.get())
    D1 = float(saisie_diagonale1.get())
    D2 = float(saisie_diagonale2.get())
    if str(geometrie.get()) == 'Rectangle':
        if str(geometrie2.get()) == 'Normal':
            if L!='' and b!='' and h!='' :
                b1=0.0 ; b2=0.0 ; h1=0.0 ; R=0.0 ; R1=0.0 ; D1=0.0 ; D2=0.0
                valeurs_geometriques=(L,b,b1,b2,h,h1,R,R1,D1,D2)
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or h==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or h=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie2.get(),") :",valeurs_geometriques)
        if str(geometrie2.get()) == 'Troué':
            if L!='' and b!='' and b1!='' and h!='' and h1!='' :
                b2=0.0; R=0.0 ; R1=0.0 ; D1=0.0 ; D2=0.0
                valeurs_geometriques=(L,b,b1,b2,h,h1,R,R1,D1,D2)
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or b1==0 or h==0 or h1==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or b1=='' or h=='' or h1=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie2.get(),") :",valeurs_geometriques)
    if str(geometrie.get()) == 'Carré':
        if str(geometrie3.get()) == 'Normal':
            if L!='' and b!='' :
                b1=0.0 ; b2=0.0 ; h=0.0 ; h1=0.0 ; R=0.0 ; R1=0.0 ; D1=0.0 ; D2=0.0
                valeurs_geometriques=(L,b,b1,b2,h,h1,R,R1,D1,D2)
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie3.get(),") :",valeurs_geometriques)
        if str(geometrie3.get()) == 'Troué':
            if L!='' and b!='' and b1!='' :
                b2=0.0 ; h=0.0 ; h1=0.0 ; R=0.0 ; R1=0.0 ; D1=0.0 ; D2=0.0
                valeurs_geometriques=(L,b,b1,b2,h,h1,R,R1,D1,D2)
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or b1==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or b1=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie3.get(),") :",valeurs_geometriques)            
    if str(geometrie.get()) == 'Forme':
        if str(geometrie4.get()) == 'I':
            if L!='' and b!='' and b1!='' and h!='' and h1!='' and b2!='':
                R=0.0 ; R1=0.0 ; D1=0.0 ; D2=0.0
                valeurs_geometriques=(L,b,b1,b2,h,h1,R,R1,D1,D2)
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or b1==0 or h==0 or h1==0 or b2==0:
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or b1=='' or h=='' or h1=='' or b2=='':
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie4.get(),") :",valeurs_geometriques)
        if str(geometrie4.get()) == 'T':
            if L!='' and b!='' and b1!='' and h!='' and h1!='' :
                b2=0.0; R=0.0 ; R1=0.0 ; D1=0.0 ; D2=0.0
                valeurs_geometriques=(L,b,b1,b2,h,h1,R,R1,D1,D2)
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or b1==0 or h==0 or h1==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or b1=='' or h=='' or h1=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie4.get(),") :",valeurs_geometriques)
        if str(geometrie4.get()) == 'L':
            if L!='' and b!='' and b1!='' and h!='' and h1!='' :
                b2=0.0; R=0.0 ; R1=0.0 ; D1=0.0 ; D2=0.0
                valeurs_geometriques=(L,b,b1,b2,h,h1,R,R1,D1,D2)
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or b1==0 or h==0 or h1==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or b1=='' or h=='' or h1=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie4.get(),") :",valeurs_geometriques)
        if str(geometrie4.get()) == 'Z':
            if L!='' and b!='' and b1!='' and h!='' and h1!='' and b2!='':
                R=0.0 ; R1=0.0 ; D1=0.0 ; D2=0.0
                valeurs_geometriques=(L,b,b1,b2,h,h1,R,R1,D1,D2)
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or b1==0 or h==0 or h1==0 or b2==0:
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or b1=='' or h=='' or h1=='' or b2=='':
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie4.get(),") :",valeurs_geometriques)
        if str(geometrie4.get()) == 'Croix': 
            if L!='' and b!='' and h!='' :
                b1=0.0 ; b2=0.0 ; h1=0.0 ; R=0.0 ; R1=0.0 ; D1=0.0 ; D2=0.0
                valeurs_geometriques=(L,b,b1,b2,h,h1,R,R1,D1,D2)
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or h==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or h=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie4.get(),") :",valeurs_geometriques)
    if str(geometrie.get()) == 'Triangle':
        if str(geometrie5.get()) == 'Rectangle':
            if L!='' and b!='' and h!='' :
                b1=0.0 ; b2=0.0 ; h1=0.0 ; R=0.0 ; R1=0.0 ; D1=0.0 ; D2=0.0
                valeurs_geometriques=(L,b,b1,b2,h,h1,R,R1,D1,D2)
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or b==0 or h==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or b=='' or h=='' :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie5.get(),") :",valeurs_geometriques)
    if str(geometrie.get()) == 'Cercle':
        if str(geometrie6.get()) == 'Normal':
            if L!='' and R!='' :
                b=0.0 ; b1=0.0 ; b2=0.0 ; h=0.0 ; h1=0.0 ; R1=0.0 ; D1=0.0 ; D2=0.0
                valeurs_geometriques=(L,b,b1,b2,h,h1,R,R1,D1,D2)
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or R==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or R=='':
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie6.get(),") :",valeurs_geometriques)
        if str(geometrie6.get()) == 'Troué':
            if L!='' and R!='' and R1!='' :
                b=0.0 ; b1=0.0 ; b2=0.0 ; h=0.0 ; h1=0.0 ; D1=0.0 ; D2=0.0
                valeurs_geometriques=(L,b,b1,b2,h,h1,R,R1,D1,D2)
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or R==0 or R1==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or R=='' or R1=='':
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie6.get(),") :",valeurs_geometriques)
        if str(geometrie6.get()) == 'Demi Cercle':
            if L!='' and R!='' :
                b=0.0 ; b1=0.0 ; b2=0.0 ; h=0.0 ; h1=0.0 ; R1=0.0 ; D1=0.0 ; D2=0.0
                valeurs_geometriques=(L,b,b1,b2,h,h1,R,R1,D1,D2)
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or R==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or R=='':
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie6.get(),") :",valeurs_geometriques)
        if str(geometrie6.get()) == 'Quart de Cercle':
            if L!='' and R!='' :
                b=0.0 ; b1=0.0 ; b2=0.0 ; h=0.0 ; h1=0.0 ; R1=0.0 ; D1=0.0 ; D2=0.0
                valeurs_geometriques=(L,b,b1,b2,h,h1,R,R1,D1,D2)
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or R==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or R=='':
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie6.get(),") :",valeurs_geometriques)
        if str(geometrie6.get()) == 'Ovale':
            if L!='' and D1!='' and D2!='' :
                b=0.0 ; b1=0.0 ; b2=0.0 ; h=0.0 ; h1=0.0 ; R=0.0 ; R1=0.0
                valeurs_geometriques=(L,b,b1,b2,h,h1,R,R1,D1,D2)
                saisie_longueur.focus()
                saisie_longueur.select_range(0,END)
            if L==0 or D1==0 or D2==0 :
                showerror('Erreur', 'Un champ de coordonnées est vide')
            if L=='' or D1=='' or D2=='':
                showerror('Erreur', 'Un champ de coordonnées est vide')
            print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie6.get(),") :",valeurs_geometriques)
    if str(geometrie.get()) == 'Losange':
        if L!='' and D1!='' and D2!='' :
            b=0.0 ; b1=0.0 ; b2=0.0 ; h=0.0 ; h1=0.0 ; R=0.0 ; R1=0.0
            valeurs_geometriques=(L,b,b1,b2,h,h1,R,R1,D1,D2)
            saisie_longueur.focus()
            saisie_longueur.select_range(0,END)
        if L==0 or D1==0 or D2==0 :
            showerror('Erreur', 'Un champ de coordonnées est vide')
        if L=='' or D1=='' or D2=='':
            showerror('Erreur', 'Un champ de coordonnées est vide')
        print("Les valeurs de L,b,b1,b2,h,h1,R,R1,D1 et D2 sont (config ",geometrie.get()," - ",geometrie6.get(),") :",valeurs_geometriques)
# définition de fcts pour les lignes ci-dessous ou on gestionne le passage d'une case à l'autre et la désactivation de certains
def largeur_next(event): #fct pour passer à b
    saisie_largeur.focus()
    saisie_largeur.select_range(0,END)
def hauteur_next(event): #fct pour passer à h
    saisie_hauteur.focus()
    saisie_hauteur.select_range(0,END)
def rayon_next(event): #fct pour passer à R
    saisie_rayon.focus()
    saisie_rayon.select_range(0,END)
def detection_passage(event): # détecte quand on doit passer d'une case à l'autre en fonction du choix de section (radio bouton)
    global geometrie, largeur_next, hauteur_next, rayon_next
    if str(geometrie.get()) == 'Rectangle': # Rectangle
        saisie_largeur.bind('<Return>', largeur_next) # switch de L à b quand on tape sur entrée
        saisie_hauteur.bind('<Return>', hauteur_next) # switch de b à h quand on tape sur entrée
    if str(geometrie.get()) == 'Cercle': # Cercle
        saisie_rayon.bind('<Return>', rayon_next) # switch de L à R quand on tape sur entrée
# Passage d'une combobox à l'autre   
canva_tab1_labelframe1_Combobox1.bind("<<ComboboxSelected>>", ajout_combobox)      
# Bouton pour valider l'entrée des données de géométrie pour rassurer l'utilisateur
Button(canva_tab1, text='Valider la géométrie', command=valider_la_géométrie).place(relx=0.25,rely=0.75,relwidth=0.5, relheight=0.05) # affiche le labelframe type de section  
"""
Fin
"""

### Barre 2 : Matériau ###
tab2 = ttk.Frame(notebook) # Creation de la barre 1 de Notebook
notebook.add(tab2, text='Matériau') # Ajout de la barre 1 au notebook
canva_tab2=Canvas(tab2, bg="red")
canva_tab2.pack(expand=1, fill='both')
#Création labelframe
canva_tab2_labelframe = LabelFrame(canva_tab2,font=("Arial",14 , "bold"),text = 'Données matériau',bg=gris_clair) #définit le message 1
canva_tab2_labelframe.place(relx=0.01,rely=0.01,relwidth=0.98, relheight=0.35) # affiche le labelframe type de section
#messages des inputs E,Mv,m,m,Re,nu
label_young = Label(canva_tab2_labelframe,font = ("Arial",10),text = 'Entrer le Module de Young E de votre poutre en N/mm² ou MPa :')
label_massevol = Label(canva_tab2_labelframe,font = ("Arial",10),text = 'Entrer la Masse volumique Mv de votre poutre en kg/mm3 :')
label_masse = Label(canva_tab2_labelframe,font = ("Arial",10),text = 'Entrer la Masse m de votre poutre en kg :')
label_limiteel = Label(canva_tab2_labelframe,font = ("Arial",10),text = 'Entrer la Limite élastique Re de votre poutre en MPa :')
label_coeffpoiss = Label(canva_tab2_labelframe,font = ("Arial",10),text = 'Entrer le Coefficient de Poisson nu de votre poutre :')
#saisie des inputs E,Mv,m,m,Re,nu
saisie_young = Entry(canva_tab2_labelframe,disabledbackground = gris_tres_fonce,font = ("Arial",11))
saisie_massevol = Entry(canva_tab2_labelframe,disabledbackground = gris_tres_fonce,font = ("Arial",11))
saisie_masse = Entry(canva_tab2_labelframe,disabledbackground = gris_tres_fonce,font = ("Arial",11))
saisie_limiteel = Entry(canva_tab2_labelframe,disabledbackground = gris_tres_fonce,font = ("Arial",11))
saisie_coeffpoiss = Entry(canva_tab2_labelframe,disabledbackground = gris_tres_fonce,font = ("Arial",11))
#saisie affichage de départ
saisie_young.insert(0, "0.0")
saisie_massevol.insert(0, "Option")
saisie_masse.insert(0, "Option")
saisie_limiteel.insert(0, "0.0")
saisie_coeffpoiss.insert(0, "Option")
#Placement des items sur la grille
label_young.grid(row=0)
saisie_young.grid(row=1)
label_massevol.grid(row=2)
saisie_massevol.grid(row=3)
label_masse.grid(row=4)
saisie_masse.grid(row=5)
label_limiteel.grid(row=6)
saisie_limiteel.grid(row=7)
label_coeffpoiss.grid(row=8)
saisie_coeffpoiss.grid(row=9)
# Gestion du stockage des valeurs
def valider_le_materiau():
    global valeurs_materiau
    #Gestion du stockage des valeurs
    E = float(saisie_young.get())
    m = str(saisie_masse.get())
    Mv = str(saisie_massevol.get())
    Re = float(saisie_limiteel.get())
    nu = str(saisie_coeffpoiss.get())
    if E!='' and Re!='' :
        if Mv!='Option' :
            m = 0.0 ; nu = 0.0
            Mv = float(saisie_massevol.get())
            valeurs_materiau = (E,Mv,m,Re,nu)
            saisie_young.focus()
            saisie_young.select_range(0,END)
        if m!='Option' :
            Mv = 0.0 ; nu = 0.0
            m = float(saisie_masse.get())
            valeurs_materiau = (E,Mv,m,Re,nu)
            saisie_young.focus()
            saisie_young.select_range(0,END)
        if  nu!='Option' :
            Mv = 0.0 ; m = 0.0
            nu = float(saisie_coeffpoiss.get())
            valeurs_materiau = (E,Mv,m,Re,nu)
            saisie_young.focus()
            saisie_young.select_range(0,END)
        if  Mv!='Option' or m!='Option' :
            Mv = 0.0 ; m = 0.0
            nu = float(saisie_coeffpoiss.get())
            valeurs_materiau = (E,Mv,m,Re,nu)
            saisie_young.focus()
            saisie_young.select_range(0,END)
        else :
            Mv = 0.0 ; m = 0.0 ; nu = 0.0
            valeurs_materiau = (E,Mv,m,Re,nu)
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
# initialisation sélection
saisie_young.focus()
saisie_young.select_range(0,END)
saisie_young.bind('<Return>', detection_passage2)         
# Bouton pour valider l'entrée des données de matériau pour rassurer l'utilisateur
Button(canva_tab2_labelframe, text='Valider le matériau', command=valider_le_materiau).grid(row=10)
"""
Fin
"""

### Barre 3 : Chargement ###
tab3 = ttk.Frame(notebook) # Creation de la barre 1 de Notebook
notebook.add(tab3, text='Chargement') # Ajout de la barre 1 au notebook
canva_tab3=Canvas(tab3, bg="white")
canva_tab3.pack(expand=1, fill='both')
# Création labelframe 1
canva_tab3_labelframe1 = LabelFrame(canva_tab3,font=("Arial",14 , "bold"),text = 'Charge concentrée',bg=gris_clair) #définit le message 1
canva_tab3_labelframe1.place(relx=0.01,rely=0.01,relwidth=0.98, relheight=0.35) # affiche le labelframe type de section
# Création labelframe 2
canva_tab3_labelframe2 = LabelFrame(canva_tab3,font=("Arial",14 , "bold"),text = 'Charge répartie',bg=gris_clair) #définit le message 1
canva_tab3_labelframe2.place(relx=0.01,rely=0.37,relwidth=0.98, relheight=0.35) # affiche le labelframe type de section
# messages des inputs label frame 1
label_force_conc_1 = Label(canva_tab3_labelframe1,font = ("Arial",10),text = 'Entrer la Force concentrée P sur votre poutre en N :')
label_pos_a = Label(canva_tab3_labelframe1,font = ("Arial",10),text = 'Entrer la distance a de votre poutre en mm :')
label_pos_b = Label(canva_tab3_labelframe1,font = ("Arial",10),text = 'Entrer la distance b de votre poutre mm :')
# saisie des inputs label frame 1
saisie_force_conc_1 = Entry(canva_tab3_labelframe1,disabledbackground = gris_tres_fonce,font = ("Arial",11))
saisie_pos_a = Entry(canva_tab3_labelframe1,disabledbackground = gris_tres_fonce,font = ("Arial",11))
saisie_pos_b = Entry(canva_tab3_labelframe1,disabledbackground = gris_tres_fonce,font = ("Arial",11))
# Placement des items sur la grille labelframe1
label_force_conc_1.grid(row=0)
saisie_force_conc_1.grid(row=1)
label_pos_a.grid(row=2)
saisie_pos_a.grid(row=3)
label_pos_b.grid(row=4)
saisie_pos_b.grid(row=5)
# messages des inputs label frame 2
label_force_rep_1 = Label(canva_tab3_labelframe2,font = ("Arial",10),text = 'Entrer la Force répartie q de votre poutre en N :')
label_pos_a1 = Label(canva_tab3_labelframe2,font = ("Arial",10),text = 'Entrer la distance a1 de votre poutre en mm :')
label_pos_b1 = Label(canva_tab3_labelframe2,font = ("Arial",10),text = 'Entrer la distance b1 de votre poutre en mm :')
# saisie des inputs label frame 2
saisie_force_rep_1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
saisie_pos_a1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
saisie_pos_b1 = Entry(canva_tab3_labelframe2,disabledbackground = gris_tres_fonce,font = ("Arial",11))
# Placement des items sur la grille labelframe2
label_force_rep_1.grid(row=0)
saisie_force_rep_1.grid(row=1)
label_pos_a1.grid(row=2)
saisie_pos_a1.grid(row=3)
label_pos_b1.grid(row=4)
saisie_pos_b1.grid(row=5)
# # saisie affichage de départ
# saisie_young.insert(0, "0.0")
# saisie_massevol.insert(0, "Option")
# saisie_masse.insert(0, "Option")
# saisie_limiteel.insert(0, "0.0")
# saisie_coeffpoiss.insert(0, "Option")
# # Gestion du stockage des valeurs
# def valider_le_chargement():
#     global valeurs_materiau
#     #Gestion du stockage des valeurs
#     E = float(saisie_young.get())
#     m = str(saisie_masse.get())
#     Mv = str(saisie_massevol.get())
#     Re = float(saisie_limiteel.get())
#     nu = str(saisie_coeffpoiss.get())
#     if E!='' and Re!='' :
#         if Mv!='Option' :
#             m = 0.0 ; nu = 0.0
#             Mv = float(saisie_massevol.get())
#             valeurs_materiau = (E,Mv,m,Re,nu)
#             saisie_young.focus()
#             saisie_young.select_range(0,END)
#         if m!='Option' :
#             Mv = 0.0 ; nu = 0.0
#             m = float(saisie_masse.get())
#             valeurs_materiau = (E,Mv,m,Re,nu)
#             saisie_young.focus()
#             saisie_young.select_range(0,END)
#         if  nu!='Option' :
#             Mv = 0.0 ; m = 0.0
#             nu = float(saisie_coeffpoiss.get())
#             valeurs_materiau = (E,Mv,m,Re,nu)
#             saisie_young.focus()
#             saisie_young.select_range(0,END)
#         if  Mv!='Option' or m!='Option' :
#             Mv = 0.0 ; m = 0.0
#             nu = float(saisie_coeffpoiss.get())
#             valeurs_materiau = (E,Mv,m,Re,nu)
#             saisie_young.focus()
#             saisie_young.select_range(0,END)
#         else :
#             Mv = 0.0 ; m = 0.0 ; nu = 0.0
#             valeurs_materiau = (E,Mv,m,Re,nu)
#             saisie_young.focus()
#             saisie_young.select_range(0,END)
#     if E==0 or Re==0 :
#         showerror('Erreur', 'Un champ de coordonnées est vide')
#     if E=='' or Re=='' :
#         showerror('Erreur', 'Un champ de coordonnées est vide')
#     print("Les valeurs de E,Mv,m,Re et nu sont :",valeurs_materiau)
# # définition de fcts pour les lignes ci-dessous ou on gestionne le passage d'une case à l'autre et la désactivation de certains
# def massevol_next(evt): #fct pour passer à Mv
#     saisie_massevol.focus()
#     saisie_massevol.select_range(0,END)
# def masse_next(evt): #fct pour passer à m
#     saisie_masse.focus()
#     saisie_masse.select_range(0,END)
# def limiteel_next(evt): #fct pour passer à Re
#     saisie_limiteel.focus()
#     saisie_limiteel.select_range(0,END)
# def coeffpoiss_next(evt): #fct pour passer à nu
#     saisie_coeffpoiss.focus()
#     saisie_coeffpoiss.select_range(0,END)
# def detection_passage2(evt): # détecte quand on doit passer d'une case à l'autre
#     saisie_young.bind('<Return>', massevol_next) # switch de E à Mv quand on tape sur entrée
#     saisie_massevol.bind('<Return>', masse_next) # switch de Mv à m quand on tape sur entrée
#     saisie_masse.bind('<Return>', limiteel_next) # switch de m à Re quand on tape sur entrée
#     saisie_limiteel.bind('<Return>', coeffpoiss_next) # switch de Re à nu quand on tape sur entrée
# initialisation sélection
saisie_force_conc_1.focus()
saisie_force_conc_1.select_range(0,END)
# saisie_young.bind('<Return>', detection_passage2)         
# Bouton pour valider l'entrée des données de matériau pour rassurer l'utilisateur
Button(canva_tab3, text='Valider la charge', command=donothing).place(relx=0.25,rely=0.80,relwidth=0.5, relheight=0.10)
"""
Fin
"""

### left_canvas_2 ###
# Bouton Calculer #
bouton_calculer= Button(left_canvas2, text="Calculer",textvariable="Re-Calculer",relief="raised",overrelief="groove", font=("Tahoma", 20,"bold"), bg=gris_tres_fonce, fg ="white", command=calcul)
bouton_calculer.place(relx=0.5,rely=0.5,relwidth=0.5, relheight=0.5,anchor='center') # afficher le bouton
"""
Fin
"""

### right frame ###

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