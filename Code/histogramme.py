import cv2 as cv
import numpy as np

#creation de deux objets

def creerObjet(url):

        """
        Fonction qui sépare les deux objets de l'image et qui renvoie leur coordonnées
        ENTREE : chaine de caractère(chemin de l'image)
        SORTIE : deux tableaux à 2 dimensions
        """
        img = cv.imread(url)

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        #Distinction des couleurs des objets
        colorA = np.array([215,215,215])
        colorB = np.array([123,123,123])

        #création des tableaux qui contiendront les coordonnées
        tA = []
        tB = []

        #Boucle comparant chaque pixel de l'image avec les couleurs recherchées
        #Rempli les tableaux
        for i in range(0,len(gray)):
            for j in range(0,len(gray)):
                if(gray[i][j] == colorA).all():
                    tA.append([i, j])
                elif (gray[i][j] == colorB).all():
                    tB.append([i, j])
        return tA, tB

# Calculer ls angles entre  objets dans une image

def calculAngle(pt1, pt2):
    """
    Fonction qui renvoie l'angle entre 2 points passés en paramètres.

    ENTREE : Deux tableaux d'entiers [x,x]
    SORTIE : Un flottant
    """
    dx = pt2[0] - pt1[0]
    dy = pt2[1] - pt1[1]
    angle_radian = np.arctan2(dx, dy)#angles en radian
    #conversion des angles en degrés
    angle_degrees = np.rad2deg(angle_radian)
    return angle_degrees

# Ajouter les angles dans un histogramme

def histogramme(tA,tB,pas=36):
    """
        Fonction qui renvoie l'histogramme d'angle de deux objets A et B

        ENTREE : Deux tableaux à 2 dimensions (A et B)
        SORTIE : à remplir
    """

    angles = []
    for i in range(0, len(tA)):
        for j in range(0, len(tB)):
            angle = calculAngle(tA[i], tB[j])
            angles.append(angle)
    #bin=classe d'un histogramme représente une plage de valeurs d'angles égale
    hist, bins = np.histogram(angles, bins=pas, range=(-180, 180))
    return hist







