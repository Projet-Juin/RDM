# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 15:40:18 2020
@author: Forjot Henri
"""


###INPUTS###


#Initialisation#
print('******************** Veuillez rentrer les éléments caractéristiques de votre étude : ********************\n')
materiau=input('Quel est le matériau utilisé ?\n')
etude=input('S\'agit\'il d\'une étude en charge concentrée (Rentrer "A"),répartie (Rentrer "B"), ou les deux (Rentrer "C") ?\n')
if etude!='A' or etude!='B' or etude!='C': 
    #Vérification si l'étude est bien définie sur un des 3 cas posssibles
    print ('!!!! Erreur !!!!','  On recommence :') #Sinon on renvoie une erreur et il faut relancer la question
    etude=input('S\'agit\'il d\'une étude en charge concentrée (Rentrer "A"),répartie (Rentrer "B"), ou les deux (Rentrer "C") ?\n')
    if etude!='A' or etude!='B' or etude!='C': #Re-vérification
        #Erreur considérée comme volontaire, arrêt du programme!
        print("******************** Erreur...ENCORE ********************")
        print("******************** Arrêt du programme ********************")


#Géométrie#
print('******************** Rentrez les caractéristiques géométriques de votre poutre en ',materiau,' : ********************\n')
h=input('Entrer la hauteur de la poutre en mm: ')
L=input('Entrer la longueur de la poutre en mm: ')
l=input('Entrer la largeur de la poutre en mm: ')
if type(h)!=int() or type(h)!=float() or type(L)!=int() or type(L)!=float() or type(l)!=int() or type(l)!=float():
    #Vérification si les valeurs sont bien des nombres
    print ('!!!! Erreur !!!!','  On recommence :')
    h=input('Entrer la hauteur de la poutre en mm: ')
    L=input('Entrer la longueur de la poutre en mm: ')
    l=input('Entrer la largeur de la poutre en mm: ')
    if type(h)!=int() or type(h)!=float() or type(L)!=int() or type(L)!=float() or type(l)!=int() or type(l)!=float():
    #Re-Vérification si les valeurs sont bien des nombres ..... Erreur considérée comme volontaire, arrêt du programme!
        print("******************** Erreur...ENCORE ********************")
        print("******************** Arrêt du programme ********************")
print('\n')  


#Caractéristiques matériau#
print('******************** Rentrez les caractéristiques physiques du matériau de votre poutre en ',materiau,' : ********************\n')
E=input('Entrer son Module de Young de la poutre en MPa:')
Mv=input('Entrer sa Masse Volumique de la poutre en g/cm^3:')
Elim=input('Entrer sa limite élastique :')
if type(E)!=int() or type(E)!=float() or type(Mv)!=int() or type(Mv)!=float() or type(Elim)!=int() or type(Elim)!=float():
    #Vérification si les valeurs sont bien des nombres
    print ('!!!! Erreur !!!!','  On recommence :')
    E=input('Entrer son Module de Young de la poutre en MPa:')
    Mv=input('Entrer sa Masse Volumique de la poutre en g/cm^3:')
    Elim=input('Entrer sa limite élastique :')
    if type(E)!=int() or type(E)!=float() or type(Mv)!=int() or type(Mv)!=float() or type(Elim)!=int() or type(Elim)!=float():
    #Re-Vérification si les valeurs sont bien des nombres ..... Erreur considérée comme volontaire, arrêt du programme!
        print("******************** Erreur...ENCORE ********************")
        print("******************** Arrêt du programme ********************")
print('\n')


#Chargement#
print('******************** Rentrez les caractéristiques du chargement de votre poutre en ',materiau,' : ********************\n')
if etude=='A':
    p=input('Entrer la Force de la charge ponctuelle en N :')
    a=input('Entrer la Distance entre la charge ponctuelle et le zéro de la poutre :')
    b=L-a
if type(p)!=int() or type(p)!=float() or type(a)!=int() or type(a)!=float():
    #Vérification si les valeurs sont bien des nombres
    print ('!!!! Erreur !!!!','  On recommence :')
    p=input('Entrer la Force de la charge ponctuelle en N :')
    a=input('Entrer la Distance entre la charge ponctuelle et le zéro de la poutre :')
    b=L-a
    if type(p)!=int() or type(p)!=float() or type(a)!=int() or type(a)!=float():
        #Re-Vérification si les valeurs sont bien des nombres ..... Erreur considérée comme volontaire, arrêt du programme!
        print("******************** Erreur...ENCORE ********************")
        print("******************** Arrêt du programme ********************")
if etude=='B':
    q=input('Entrer la Force linéique de la charge répartie en N/mm :')
if type(q)!=int() or type(q)!=float():
    #Vérification si les valeurs sont bien des nombres
    print ('!!!! Erreur !!!!','  On recommence :')
    q=input('Entrer la Force linéique de la charge répartie en N/mm :')
    if type(q)!=int() or type(q)!=float():
        #Re-Vérification si les valeurs sont bien des nombres ..... Erreur considérée comme volontaire, arrêt du programme!
        print("******************** Erreur...ENCORE ********************")
        print("******************** Arrêt du programme ********************")
if etude=='C':
    p=input('Entrer la Force de la charge ponctuelle en N :')
    q=input('Entrer la Force linéique de la charge répartie en N/mm :')
    a=input('Entrer la Distance entre la charge ponctuelle et le zéro de la poutre :')
    b=L-a
if type(p)!=int() or type(p)!=float() or type(a)!=int() or type(a)!=float() or type(q)!=int() or type(q)!=float():
    #Vérification si les valeurs sont bien des nombres
    print ('!!!! Erreur !!!!','  On recommence :')
    p=input('Entrer la Force de la charge ponctuelle en N :')
    q=input('Entrer la Force linéique de la charge répartie en N/mm :')
    a=input('Entrer la Distance entre la charge ponctuelle et le zéro de la poutre :')
    b=L-a
    if type(p)!=int() or type(p)!=float() or type(a)!=int() or type(a)!=float() or type(q)!=int() or type(q)!=float():
        #Re-Vérification si les valeurs sont bien des nombres ..... Erreur considérée comme volontaire, arrêt du programme!
        print("******************** Erreur...ENCORE ********************")
        print("******************** Arrêt du programme ********************")
print('\n')


###CALCULS INTERMEDIAIRES###

#Réactions aux appuis#
if etude=='A':
    RA=(p*b)/L
    RB=(p*a)/L
if etude=='B':
    RA=(q*L)/2
    RB=(q*L)/2
if etude=='C':
    RA=((p*b)/L)+((q*L)/2)
    RB=((p*a)/L)+((q*L)/2)