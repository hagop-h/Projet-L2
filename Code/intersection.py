#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 09:54:39 2023

@author: io02718 (VICTOR SOLER)

Ici, toutes les fonctions necessaires au calcul du prototype de direction, et de l'éloignement de l'histogramme d'angle avec celui ci
La fonction main2() execute toutes les fonctions et renvoie les données importantes pour leurs futurs traitement et affichage dans l'interface
"""
import matplotlib


import numpy as np
import matplotlib.pyplot as plt
from histogramme import *

#------------------------------------------------------------------------------------------------------------------------------
# ENTREES : pas du prototype, 0 pour droit, 1 pour gauche, 2 pour bas, 3 pour haut
# SORTIE : x angles entre -180° et 180°, protoype en cos^2(x)/sin^2(x)
def proto(pas,direction):
    x = np.linspace(-180,180,int(pas))

    if (direction==0)|(direction==1):

        y = [np.cos((np.pi*i/180))**2 for i in x]
        if direction==0:#proto droit
            for i in range(0,int(pas/4)):
                y[i]=0;
            for i in range(3*int(pas/4),int(pas)):
                y[i]=0;
        if direction==1:#proto gauche
            for i in range(int(pas/4),3*int(pas/4)):
                y[i]=0
    if (direction==2)|(direction==3):
        y = [np.sin((np.pi*i/180))**2 for i in x]
        if direction==2:#proto bas
            for i in range(0,int(pas/2)):
                y[i]=0;
        if direction==3:#proto haut
            for i in range(int(pas/2),int(pas)):
                y[i]=0
    return (x,y)

#------------------------------------------------------------------------------------------------------------------------------
#Fonction d'affichage du prototype et de l'histogramme
# x : abscisses
def afficherproto(proto,histo,x):
    plt.clf()
    plt.plot(x,histo)
    plt.plot(x,proto,label="prototype")
    plt.show()
    radx=[i*np.pi/180 for i in x]
    plt.clf()
    plt.polar(radx,proto,label="prototype")
    plt.polar(radx,histo,label="histogramme")
    plt.show()

#------------------------------------------------------------------------------------------------------------------------------
#entrées : prototype et histogramme
#sorties lintersec la liste des intersections et f(xi) de l'histogramme
# imax intersection max et xmax sa valeur
def intersection(proto,histo):
    lintersec = []
    imax = 0
    xmax = -1
    for i in range(0,len(proto)):
        if proto[i]-0.04<=histo[i]<=proto[i]+0.04:
            lintersec.append([histo[i],i])
            if histo[i]>imax:
                imax=histo[i]
                xmax = i
    #print("xmax = ")
    #print(xmax)
    # print(lintersec)
    return xmax

#------------------------------------------------------------------------------------------------------------------------------
#ENTREE : l'indice d' lintersection entre le prototype et l'htogramme, le prototype
#SORTIE : chaine exprimant l'eloignement par rappor au prototype
def eloignement(intersection,proto):
    pmax = proto.index(max(proto))
    #print("pmax =")
    #print(pmax-intersection)
    if(pmax==0):
        ecart = min(np.abs(pmax-intersection),np.abs(int(len(proto))-intersection))
    else:
        ecart = np.abs(pmax-intersection)
    
    if(0<ecart<len(proto)/16):
        # print("l'objet est très proche de la direction analysée")
        return "est très"
    if(1 + len(proto)/16<ecart<len(proto)/8):
        # print("l'objet est assez proche de la direction analysée")
        return "est assez"
    if(1 + len(proto)/8<ecart<len(proto)/4):
        # print("l'objet n'est pas proche de la direction analysée")
        return "n'est pas"
    else:
        # print("lobjet est à l'opposé de la direction analysée")
        return "n'est pas du tout"

#------------------------------------------------------------------------------------------------------------------------------
#ENTREES : chemin vers l'image à traiter, le pas de l'histogramme
#crée un histogramme d'angle normalisé
#SORTIE : L'histogramme normalisé
def histo(url,pas):
    tA,tB = creerObjet(url)
    hist = histogramme(tA,tB,pas)
    maxi = np.max(hist)
    histnorm = [i/maxi for i in hist]
    return (histnorm)

#------------------------------------------------------------------------------------------------------------------------------
#ENTREE :  le chemin vers l'image à traiter, la direction (0 pour droite, 1 pour gauche, 2 pour bas, 3 pour haut), et le pas de l'histogramme.
#(NB, j'ai changé le programme d'Amy pour pouvoir mettre le pas en entrée)
#SORTIE : l'abscisse x, l'histogramme d'angle normalisé, le protoype, et e l'éloignement entre 0 et 3
def main2(url,dir,pas):
    his = histo(url,pas)
    x,pro = proto(pas,dir)
    xm=intersection(pro,his)
    afficherproto(pro,his,x)
    e = eloignement(xm,pro)
    return(x,his,pro,e)
