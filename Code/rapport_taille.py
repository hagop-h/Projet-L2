def rapport(objetA, objetB):
    """
    Calcule la taille de l'objet jaune par rapport à l'objet vert en utilisant les contours.

    ENTREE: une image en couleur(BGR) et deux contour de l'objet vert (tableau numpy de coordonnées) et de l'objet jaune (tableau numpy de coordonnées)

    SORTIE: un nombre flottant représentant la taille de l'objet jaune par rapport à l'objet vert
    """

    # Calculer l'aire de chaque objet
    aireA = len(objetA)
    aireB = len(objetB)

    # Calculer le ratio de taille
    rapport_taille = aireA / aireB
    # Pour eviter division par 0
    if rapport_taille == 0:
        rapport_taille = 1

    # Arrondir le ratio à l'entier le plus proche et retourner la valeur
    return round(rapport_taille)

