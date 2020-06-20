# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 12:51:09 2020

@author: Clara
"""
import classe 

charge_concentrée = []
a1 = 1
a2 = 2
salut = classe.charge_concentrée(a1, a2)
charge_concentrée.append(salut)
print(salut.P)
print(charge_concentrée[0].P)
print(charge_concentrée[0].a)

salut = classe.charge_concentrée(a1+5,a2+5)
charge_concentrée.append(salut)
print(salut.P)
print(charge_concentrée[1].P)
print(charge_concentrée[1].a)