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
# Création labelframe
canva_tab1_labelframe = LabelFrame(canva_tab1,font=("Arial",14 , "bold"),text = 'Type de section',bg="blue") #définit le message 1
canva_tab1_labelframe.place(relx=0.01,rely=0.01,relwidth=0.98, relheight=0.30) # affiche le labelframe type de section    
# Sélection de circulaire ou rectangulaire
type_de_section = IntVar() # Valeur 1 si circulaire sinon valeur 0
canva_tab1_label1 = Label(canva_tab1_labelframe,font = ("Arial",11),text = 'Rectangulaire')
case1_tab1 = Radiobutton(canva_tab1_labelframe,selectcolor = 'red',variable = type_de_section,value=0)
canva_tab1_label2 = Label(canva_tab1_labelframe,font = ("Arial",11 ),text = 'Circulaire')
case2_tab1 = Radiobutton(canva_tab1_labelframe,selectcolor = 'red',variable = type_de_section,value=1)
# Placement des 4 ci-dessus items sur une grille *4
case1_tab1.grid(row=0,column=0) # affiche le radio bouton rectangulaire
canva_tab1_label1.grid(row=0,column=1) # affiche le label rectangulaire
case2_tab1.grid(row=0,column=2) # affiche le radio bouton circulaire
canva_tab1_label2.grid(row=0,column=3) #affiche le label circulaire
# messages des inputs L,b,h,R
label_longueur = Label(canva_tab1_labelframe,font = ("Arial",10),text = 'Entrer la Longueur L de votre poutre en mm :')
label_largeur = Label(canva_tab1_labelframe,font = ("Arial",10),text = 'Entrer la Largeur b de votre poutre en mm :')
label_hauteur = Label(canva_tab1_labelframe,font = ("Arial",10),text = 'Entrer la Hauteur h de votre poutre en mm :')
label_rayon = Label(canva_tab1_labelframe,font = ("Arial",10),text = 'Entrer le Rayon R de votre poutre en mm :')
# saisie des inputs L,b,h
saisie_longueur = Entry(canva_tab1_labelframe,disabledbackground = gris_tres_fonce,font = ("Arial",11))
saisie_largeur = Entry(canva_tab1_labelframe,disabledbackground = gris_tres_fonce,font = ("Arial",11))
saisie_hauteur = Entry(canva_tab1_labelframe,disabledbackground = gris_tres_fonce,font = ("Arial",11))
saisie_rayon = Entry(canva_tab1_labelframe,disabledbackground = gris_tres_fonce,font = ("Arial",11))
# Placement des items sur la grille 4 colonnes
label_longueur.grid(row=2,column=1,columnspan=4)
saisie_longueur.grid(row=3,column=1,columnspan=4)
label_largeur.grid(row=4,column=1,columnspan=4)
saisie_largeur.grid(row=5,column=1,columnspan=4)
label_hauteur.grid(row=6,column=1,columnspan=4)
saisie_hauteur.grid(row=7,column=1,columnspan=4)
label_rayon.grid(row=8,column=1,columnspan=4)
saisie_rayon.grid(row=9,column=1,columnspan=4)   
# Gestion du stockage des valeurs
def valider_la_géométrie():
    global valeurs_geometriques,type_de_section
    L = float(saisie_longueur.get())
    b = float(saisie_largeur.get())
    h = float(saisie_hauteur.get())
    R = float(saisie_rayon.get())
    if int(type_de_section.get()) == 0 : # 0 si radio bouton sur rectangulaire
        if L!='' and b!='' and h!='' :
            R=0.0
            valeurs_geometriques=(L,b,h,R)
            saisie_longueur.focus()
            saisie_longueur.select_range(0,END)
        if L==0 or b==0 or h==0 :
            showerror('Erreur', 'Un champ de coordonnées est vide')
        if L=='' or b=='' or h=='' :
            showerror('Erreur', 'Un champ de coordonnées est vide')
        print("Les valeurs de L,b,h et R sont (config RECTANGULAIRE):",valeurs_geometriques)
    else : # 1 si radio bouton sur circulaire
        if L!='' and R!='' :
            b=0.0
            h=0.0
            valeurs_geometriques=(L,b,h,R)
            saisie_longueur.focus()
            saisie_longueur.select_range(0,END)
        if L==0 or R==0 :
            showerror('Erreur', 'Un champ de coordonnées est vide')
        if L=='' or R=='' :
            showerror('Erreur', 'Un champ de coordonnées est vide')
        print("Les valeurs de L,b,h et R sont (config CIRCULAIRE):",valeurs_geometriques)
# définition de fcts pour les lignes ci-dessous ou on gestionne le passage d'une case à l'autre et la désactivation de certains
def largeur_next(evt): #fct pour passer à b
    saisie_largeur.focus()
    saisie_largeur.select_range(0,END)
def hauteur_next(evt): #fct pour passer à h
    saisie_hauteur.focus()
    saisie_hauteur.select_range(0,END)
def rayon_next(evt): #fct pour passer à R
    saisie_rayon.focus()
    saisie_rayon.select_range(0,END)
def detection_passage(evt): # détecte quand on doit passer d'une case à l'autre en fonction du choix de section (radio bouton)
    global type_de_section
    if int(type_de_section.get()) == 0 : #rectangulaire
        saisie_largeur.bind('<Return>', largeur_next) # switch de L à b quand on tape sur entrée
        saisie_hauteur.bind('<Return>', hauteur_next) # switch de b à h quand on tape sur entrée
    else : # circulaire
        saisie_rayon.bind('<Return>', rayon_next) # switch de L à R quand on tape sur entrée
def detection_choix_section(evt): # fct pour voir quel radio bouton est sélectionné et donc qu'elles cases doivent etre grisé
    global type_de_section
    saisie_longueur.delete(0,END) # saisie affichage de départ
    saisie_longueur.insert(0, "0.0") # saisie affichage de départ
    saisie_longueur.config(cursor='hand1')
    if int(type_de_section.get()) == 0 : #rectangulaire
        saisie_largeur.insert(0, "0.0") # saisie affichage de départ
        saisie_hauteur.insert(0, "0.0") # saisie affichage de départ
        saisie_rayon.delete(0,END) # saisie affichage de départ
        saisie_longueur.focus() #refait le focus automatique sur la première case dès qu'on change le choix du radio bouton type de section
        saisie_longueur.select_range(0,END)
        label_rayon.config(state = DISABLED,cursor='X_cursor')
        saisie_rayon.config(state = DISABLED,cursor='X_cursor')
        label_largeur.config(state = NORMAL)
        label_hauteur.config(state = NORMAL)
        saisie_largeur.config(state = NORMAL,cursor='hand1')
        saisie_hauteur.config(state = NORMAL,cursor='hand1')
        print ("saisie_rayon désactivé")
    else : # circulaire
        saisie_rayon.insert(0, "0.0") # saisie affichage de départ
        saisie_largeur.delete(0,END) # saisie affichage de départ
        saisie_hauteur.delete(0,END) # saisie affichage de départ
        saisie_longueur.focus() #refait le focus automatique sur la première case dès qu'on change le choix du radio bouton type de section
        saisie_longueur.select_range(0,END)
        label_largeur.config(state = DISABLED)
        label_hauteur.config(state = DISABLED)
        saisie_largeur.config(state = DISABLED,cursor='X_cursor')
        saisie_hauteur.config(state = DISABLED,cursor='X_cursor')
        label_rayon.config(state = NORMAL,cursor='hand1')
        saisie_rayon.config(state = NORMAL,cursor='hand1')
        print ("saisie_largeur désactivé \nsaisie_hauteur désactivé")
# initialisation sélection
saisie_longueur.focus() 
saisie_longueur.select_range(0,END) 
saisie_longueur.bind('<Return>', detection_passage) 
# Passage d'une casse à l'autre avec détection si circulaire ou rectangulaire (et donc grisage des cases en fonction)
case1_tab1.bind('<ButtonPress>', detection_choix_section)
case2_tab1.bind('<ButtonPress>', detection_choix_section)           
# Bouton pour valider l'entrée des données de géométrie pour rassurer l'utilisateur
Button(canva_tab1_labelframe, text='Valider la géométrie', command=valider_la_géométrie).grid(row=10,column=1,pady=15,columnspan=4)
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
Button(canva_tab2_labelframe, text='Valider la matériau', command=valider_le_materiau).grid(row=10)
"""
Fin
"""

### Barre 3 : Chargement ###
tab3 = ttk.Frame(notebook) # Creation de la barre 1 de Notebook
notebook.add(tab3, text='Chargement') # Ajout de la barre 1 au notebook
canva_tab3=Canvas(tab3, bg="white")
canva_tab3.pack(expand=1, fill='both')
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