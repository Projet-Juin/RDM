# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:02:26 2020

@author: CLARA (rendons à cesear ce qui est à cesear)
"""
import math

def carré(L, b) :
    S = b**2
    Igz = pow(b,4)/12
    volume = S*L
    return Igz, L, b, volume

def carré_creux(L, b, b1) :
    S = b**2 - b1**2
    Igz = ((b**4)-(b1**4))/12
    volume = S*L
    return Igz, L, b, volume

def rectangle(L, b, h) :
    S = h*b
    Igz = (b *(pow(h,3)))/12
    volume = S*L
    return Igz, L, h, volume

def rectangle_creux(L, b, h, b1, h1) :
    S = h*b - h1*b1
    Igz = ((b*(h**3)) - b1*(h1**3))/12
    volume = S*L
    return Igz, L, h, volume

def I(L, b, h, b1, b2, h1) :
    S = h1*(b - b1 - b2) + h*(b1 + b2)
    Igz =  (2*b*(h1**3)+((h**3)-(h1**3))*(b1 + b2)) / 24
    volume = S*L
    return Igz, L, h, volume

def T(L, b, h, b1, h1) :
    S = b1*h - h1*(b1 - b)
    Igz =  (b*(h1**3)+((h**3)-(h1**3))*b1) / 12
    volume = S*L
    return Igz, L, h, volume

def L(L, b, h, b1, h1) :
    S = h*b1 - h1*(b1-b)
    Igz = (b*(h1**3)+((h**3)-(h1**3))*b1) / 12
    volume = S*L
    return Igz, L, h, volume

def Z(L, b, h, b1, b2, h1) :
    S =  h1*(b-b1-b2)+h*(b1+b2)
    Igz = (2*b*(h1**3)+((h**3)-(h1**3))*(b1+b2)) / 24
    volume = S*L
    return Igz, L, h, volume

def triangle_rectangle(L, b, h) :
    S = h*b/2
    Igz = b*(h**3)/36
    volume = S*L
    return Igz, L, h, volume

def cercle(L, R) :
    S = math.pi * R**2
    Igz = math.pi* (R**4) / 4
    volume = S*L
    return Igz, L, 2*R, volume

def cercle_creux(L, R, R1) :
    S = math.pi * (R**2 - R1**2)
    Igz = math.pi*((R**4)-(R1**4)) / 4
    volume = S*L
    return Igz, L, 2*R, volume

def demi_cercle(L, R) :
    S = math.pi*(R**2)/2
    Igz =  (R**4)*((math.pi/8)-(8/(9*math.pi)))
    volume = S*L
    return Igz, L, R, volume

def quart_cercle(L, R) :
    S = (math.pi*((R)**2))/4
    Igz = (R**4)*((math.pi/8) - (8/(9*math.pi))) / 2
    volume = S*L
    return Igz, L, R, volume

def ovale(L, D2, D1) :
    S = (math.pi*D1*D2) / 4
    Igz = (math.pi*D1*(D2**3)) / 64
    volume = S*L
    return Igz, L, D1, volume

def croix(L, b, h) :
    S = 2*b*h - b**2
    Igz = (b*(h**3)+(b**3)*h-(b**4))/12
    volume = S*L
    return Igz, L, h, volume

def losange(L, D2, D1) :
    S = D1*D2 / 2
    Igz = (D1**3)*D2 / 48
    volume = S*L
    return Igz, L, D1, volume


        


    