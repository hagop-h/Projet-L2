
import cv2 as cv

from Barycentre import barycentre
from creer_objet import creerObjet
from degre_eloignement_barycentrique import degre_eloignement_barycentrique
from rapport_taille import rapport
from trouver_contour import trouver_contour


def main_Barycentre(image_path):
    """
    Fonction retournant l'éloignement barycentrique des deux objets de l'image
    ENTREE : chaine de caractères (chemin de l'image)
    SORTIE : chaine de caractère (éloignement barycentrique)
    """
    
    # Dimensions d'image
    image = cv.imread(image_path, cv.IMREAD_COLOR)
    height, width, _ = image.shape

    vert, jaune = creerObjet(image_path)

    #Calcul du barycentre
    x1, y1, x2, y2 = barycentre(vert, jaune)


    contours = trouver_contour(image)
    taille =rapport(contours[0],contours[1])
    e = degre_eloignement_barycentrique(x1, y1, x2, y2, height, width, taille)

    return(e)
