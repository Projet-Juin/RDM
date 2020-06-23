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
font_texte2 = ("Arial", 11)
gris_1_bis='#EAECEE'
gris_1='#D5D8DC'
gris_2='#ABB2B9'
gris_3='#85929E'
gris_4='#808B96'
gris_5='#5D6D7E'
gris_6='#566573'
gris_7='#34495E'

def donothing(): # Pour eviter les bugs, fonctions qui dit que rien n'est encore codé quand on sélectionne un élts non codés
    nouvelle_fenetre =Tk()
    boutton = Button(nouvelle_fenetre, text="Ne fait rien pour le moment \n A venir très prochainement !")
    boutton.pack(side='top')  
    nouvelle_fenetre.mainloop()

def donothing_event(event): # Pour eviter les bugs, fonctions qui dit que rien n'est encore codé quand on sélectionne un élts non codés
    donothing()

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

# import json
# def ouvrir():
#     global liste_noeuds, liste_poutres
#     with open("inputs_example.json", "r") as f:
#         liste_noeuds, liste_poutres = json.load(f)
    
# def sauvegarder():
#     with open("inputs_example.json", "w") as f:
#         json.dump((liste_noeuds, liste_poutres), f)
#         import matplotlib

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
    root=Tk()
    root.title("Solve Structure --- Aide") #Titre de l'encadré
    root.config(bg=gris_5)
    root.wm_iconbitmap('images/petitlogo1.ico')
    root.geometry("%dx%d" % (500,150))
    label0=Label(root,justify='left',bg=gris_5,font=("Arial", 14, "bold italic"),text='\n')
    label0.pack(fill='both')
    label2=Label(root,justify='left',bg=gris_5,font=font_texte2,text= '\n')
    label2.pack(fill='both')
    label4=Label(root,justify='left',bg=gris_5,font=font_texte2,text= '\n')
    label4.pack(fill='both')
    label6=Label(root,justify='left',bg=gris_5,font=font_texte2,text= '\n')
    label6.pack(fill='both')
    label8=Label(root,justify='left',bg=gris_5,font=font_texte2,text= '\n')
    label8.pack(fill='both')
    root.mainloop()
    
def ctds_de_fct(): # annonce les conditions dans lequels le programme renvois des valeurs "exactes"
    root=Tk()
    root.title("Solve Structure --- Conditions de fonctionnement") #Titre de l'encadré
    root.config(bg=gris_5)
    root.wm_iconbitmap('images/petitlogo1.ico')
    root.geometry("%dx%d" % (1200,500))
    label0=Label(root,justify='left',bg=gris_5,font=("Arial", 14, "bold italic"),text='Principes fondamentaux de la théorie des poutres\n')
    label0.pack(fill='both')
    label2=Label(root,justify='left',bg=gris_5,font=font_texte2,text= 'Le postulat de la Résitance Des Matériaux (RDM) implique que : \n\nDeux des dimensions de la poutre sont petites par rapport à la troisième. En d\'autres termes les dimensions de la section droite sont petites par rapport à la longueur de la poutre. \nCe principe permet d\'approximer la poutre par une ligne (droite ou courbe) et des sections droites. En général, une longueur ou une distance de l\'ordre de deux à trois fois la plus\ngrande dimension de la section droite est considérée suffisante pour appliquer le modèle RDM.\n\n')
    label2.pack(fill='both')
    label4=Label(root,justify='left',bg=gris_5,font=font_texte2,text= 'Le principe de Saint-Venant précise que le comportement en un point quelconque de la poutre, pourvu que ce point soit suffisamment éloigné des zones d\'applications des\nforces et des liaisons,est indépendant de la façon dont sont appliquées les forces et de la façon dont sont physiquement réalisées les liaisons; le comportement dépend alors\nuniquement du torseur des forces internes en ce point. La conséquence est que les contraintes produites par un système de forces dans une section éloignée du point d\'application\nde ces forces ne dépendent que de la résultante générale et du moment résultat du système de forces appliquées à gauche de cette section.\n\n')
    label4.pack(fill='both')
    label6=Label(root,justify='left',bg=gris_5,font=font_texte2,text= 'Le modèle RDM n\'est plus valide lorsque le principe de Saint Venant n\'est pas satisfait, c\'est-à-dire à proximité des liaisons, des appuis ou des points d\'application des forces.\nDans ces cas particuliers, il faut appliquer les principes de la mécanique des milieux continus. Le principe de Navier-Bernoulli précise que les sections droites le long de la fibre\nmoyenne restent planes après déformation. Les déformations dues à l\'effort tranchant montrent que les sections droites ne peuvent pas rester planes mais subissent un\ngauchissement. Pour tenir compte de ce fait l\'énoncé de ce principe peut prendre la forme suivante: deux sections droites infiniment voisines deviennent après déformation deux\nsections gauches superposables par déplacement.Comme ce déplacement est petit, on peut considérer que les allongements ou raccourcissements de tout tronçon de fibre sont\ndes fonctions linéaires des coordonnées de la fibre dans le plan de la section.\n\n')
    label6.pack(fill='both')
    label8=Label(root,justify='left',bg=gris_5,font=font_texte2,text= 'La loi de Hooke précise que, dans le domaine élastique du matériau, les déformations sont proportionnelles aux contraintes. Le principe de superposition permet de décomposer\ntoute sollicitation complexe en une somme de sollicitations élémentaires dont les effets sont ensuite additionnés. Ce principe est directement lié à l\'hypothèse de linéarité de la loi de\nHooke.\n')
    label8.pack(fill='both')
    root.mainloop()
def credit(): # annonce la version du programme, les concepteurs du programme et l'année de développement
    donothing()
    