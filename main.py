# -*- coding: utf-8 -*-
"""
@author: Forjot Henri

Création du main

"""
### IMPORTATIONS ###
from tkinter import *
from appel_fonctions_annexes import *
#from gestion_des_entrées import *
from gestion_des_calculs import *
from tkinter import ttk

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
main.geometry("%dx%d" % (width, 1050))
# main.resizable(width=FALSE, height=FALSE) #empêche de déformer la fenetre
"""
Fin
"""

### Creation d'une Barre de menu ###
barre_de_menu = Menu(main, tearoff=0)
main.config(menu=barre_de_menu)
# Création d'un menu fichier et ajout d'items
fichier_menu = Menu(barre_de_menu,activebackground=gris_clair) # Création d'un menu fichier
fichier_menu.add_command(label='Ouvrir',command=ouvrir) # ajout de l'item ouvrir
fichier_menu.add_command(label='Sauvegarder            (Ctrl+S)',command=sauvegarder) # ajout de l'item sauvegarder
fichier_menu.add_command(label='Sauvegarder Sous   (Shift+Ctrl+S)',command=sauvegarder_sous) # ajout de l'item sauvegarder sous
fichier_menu.add_command(label='Redémarrer',command=reboot_programme) # ajout de l'item redémarrer
fichier_menu.add_separator() #ajout d'un separateur
fichier_menu.add_command(label='Quitter',command=main.destroy) # ajout de l'item quitter
# Création d'un menu éléments finis et ajout d'items
elts_finis_menu = Menu(barre_de_menu,activebackground=gris_clair) # Création d'un menu élts finis
elts_finis_menu.add_command(label='Switch vers Éléments finis',command=switch_elts_finis) # ajout de l'item permettant d'aller en élément finis
elts_finis_menu.add_separator() #ajout d'un separateur
elts_finis_menu.add_command(label='Importer les Inputs d\'Éléments finis',command=import_elts_finis) # ajout de l'item permettant d'importer les données d'éléments finis
elts_finis_menu.add_command(label='Exporter les Inputs d\'Éléments finis',command=export_elts_finis) # ajout de l'item permettant d'exporter les données d'éléments finis
# Création d'un menu autres et ajout d'items
autres_menu = Menu(barre_de_menu,activebackground=gris_clair) # Création d'un menu autres
autres_menu.add_command(label='Aide',command=aide) # ajout de l'item aide
autres_menu.add_command(label='Conditions de fonctionnement',command=ctds_de_fct) # ajout de l'item conditions de la rdm
autres_menu.add_separator() #ajout d'un separateur
autres_menu.add_command(label='Crédit',command=credit) # ajout de l'item crédit
#Ajouts des barres de menus
barre_de_menu.add_cascade(label='Fichier', menu=fichier_menu,command=donothing) # ajouter de fichier_menu dans barre_de_menu
barre_de_menu.add_cascade(label='Éléments finis', menu=elts_finis_menu,command=donothing) # ajouter de elts_finis_menu dans barre_de_menu
barre_de_menu.add_cascade(label='Autres', menu=autres_menu,command=donothing) # ajouter de autres_menu dans barre_de_menu
"""
Fin
"""

### Création de 2 frames principales ###
#Fenetre principale en 2 frames
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
# Barre 1 : Géométrie
tab1 = ttk.Frame(notebook) # Creation de la barre 1
notebook.add(tab1, text='Géométrie') # Ajout de la barre 1 au notebook
canva_tab1=Canvas(tab1, bg="yellow")
canva_tab1.pack(expand=1, fill='both')
# Barre 2 : Matériau
tab2 = ttk.Frame(notebook) # Creation de la barre 1 de Notebook
notebook.add(tab2, text='Matériau') # Ajout de la barre 1 au notebook
canva_tab2=Canvas(tab2, bg="red")
canva_tab2.pack(expand=1, fill='both')
#Barre 3 : Chargement
tab3 = ttk.Frame(notebook) # Creation de la barre 1 de Notebook
notebook.add(tab3, text='Chargement') # Ajout de la barre 1 au notebook
canva_tab3=Canvas(tab3, bg="white")
canva_tab3.pack(expand=1, fill='both')
# on place le notebook
notebook.enable_traversal() # permet de swtich avec le clavier d'un tab à l'autre [Ctl+tab,Ctrl+shift+tab,Alt+K]
notebook.pack(expand=1, fill='both') 

# LabelFrame using tab1 as the parent
# mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')
# mighty.grid(column=0, row=0, padx=8, pady=4)
# a_label = ttk.Label(mighty, text=' Enter a number: ')
# a_label.grid(column=0, row=0, sticky='W')

### scrolbar - left_canva2 ###
# Onglet1 = TTK.Notebook(root) 
# Onglet1.pack(side=TK.LEFT)
# Onglet1.enable_traversal()
# f1 = TK.Frame(Onglet1, bg='green', bd=5)
# Onglet1.add(f1, text='Onglet 1')
# s1 = TK.Scrollbar(f1,orient=TK.VERTICAL)
# texte1 = TK.Text(f1, wrap=TK.WORD)
# texte1.config(yscrollcommand=s1.set, font=('courier', 11),
# 	background='seashell2', foreground='black', insertbackground='purple')
# texte1.grid(column=0, row=0)
# s1.grid(column=1, row=0, sticky=TK.S+TK.N)
# Onglet1.select(Onglet1.index('end')-1)
# texte1.focus_set()
 
# Onglet2 = TTK.Notebook(root) 
# Onglet2.pack() 
# Onglet2.enable_traversal() 
# f2 = TK.Frame(Onglet2, bg='red', bd=5) 
# Onglet2.add(f2, text='Onglet 2')
# s2 = TK.Scrollbar(f2,orient=TK.VERTICAL)
# texte2 = TK.Text(f2, wrap=TK.WORD)
# texte2.config(yscrollcommand=s2.set, font=('courier', 11),
# 	background='seashell2', foreground='purple', insertbackground='purple')
# texte2.grid(column=0, row=0)
# s2.grid(column=1, row=0, sticky=TK.S+TK.N)
# Onglet2.select(Onglet2.index('end')-1)
 
# root.mainloop()

### Bouton Calculer ###
bouton_calculer= Button(left_canvas2, text="Calculer",textvariable="Re-Calculer",relief="raised",overrelief="groove", font=("Tahoma", 20,"bold"), bg=gris_tres_fonce, fg ="white", command=calcul)
#création d'une grille 3*3 pour placer le bouton au centre
# left_canvas2.columnconfigure(0, weight=1)
# left_canvas2.columnconfigure(1, weight=10)
# left_canvas2.columnconfigure(2, weight=1)
# left_canvas2.rowconfigure(0, weight=1)
# left_canvas2.rowconfigure(1, weight=10)
# left_canvas2.rowconfigure(2, weight=1)
# bouton_calculer.grid(row=0,column=0,rowspan=20,columnspan=20) # afficher le bouton
bouton_calculer.place(relx=0.5,rely=0.5,relwidth=0.5, relheight=0.5,anchor='center')
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