import cv2 as cv
import numpy as np

# creation de deux objets

def creerObjet(chemin):
    # Chargement de l'image
    img = cv.imread(chemin)

    # Conversion de l'image au niveau gris
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Couleur de l'objet A (vert)
    colorA = np.array([123, 123, 123])
    # Couleur de l'objet B (jaune)
    colorB = np.array([215, 215, 215])

    # Création de deux listes vides
    # pour stocker les pixels des objets A et B
    tA = []
    tB = []

    # Trouve les coordonnées des pixels appartenant à chaque objet
    # et retourne deux listes remplis
    for i in range(0, len(gray)):
        for j in range(0, len(gray)):
            if (gray[j][i] == colorA).all():
                tA.append([i, j])
            elif (gray[j][i] == colorB).all():
                tB.append([i, j])

    return tA, tB
