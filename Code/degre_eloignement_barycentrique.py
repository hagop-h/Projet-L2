import numpy as np
from Distance import dist

def degre_eloignement_barycentrique(x1, y1, x2, y2, height, width, size_ratio):
    """
    Fonction qui renvoie la la direction ,la precision et la direction relative

    ENTREE : les 2 coords de barycentre, hauteur, largeur de l'image et un rapport de taille (1 par défaut)
    SORTIE : un tuple contenant un entier qui représente la direction de l'objet vert
             par rapport à l'objet jaune (entre 0 et 3) et une chaîne de caractères qui indique
             la précision de la position de l'objet jaune par rapport à l'objet jaune
             et la direction relative à laquelle il se trouve par rapport à l'objet jaune
    """

    # Calcul de la différence entre les deux barycentres
    diff = np.array([x1 - x2, y1 - y2])
    if size_ratio == 0 : size_ratio = 1
    distance = dist(x1, y1, x2, y2) * (1/size_ratio) # distance entre les deux barycentres en prenant en compte la taille

    # Calcul de l'angle de la différence par rapport à l'axe des abscisses
    angle = np.degrees(np.arctan2(diff[1], diff[0]))

    # Conversion de l'angle en entier entre 0 et 3
    if -45 < angle <= 45:
        direction = 1  # À droite
    elif -135 < angle <= -45:
        direction = 0  # en dessous
    elif 45 < angle <= 135:
        direction = 2  # en dessus
    else:
        direction = 3  # À gauche

    # Détermination de la précision de la position
    # Calcul de la distance normalisée entre 0 et 1
    max_distance = np.sqrt(width ** 2 + height ** 2) * (1/size_ratio) # Pythagore en prenant en compte la taille
    norm_distance = distance / max_distance  # Calcul de la distance maximale possible entre les deux barycentres

    # Détermination de la précision
    if norm_distance < 0.30:
        precision = "très proche"
    elif norm_distance < 0.35:
        precision = "proche"
    elif norm_distance < 0.45:
        precision = "loin"
    else:
        precision = "très loin"

    # Détermination de la direction relative
    if direction in [1, 3]:
        return direction, f"{precision} à {'droite' if direction == 1 else 'gauche'}"
    else:
        return direction, f"{precision} {'au-dessus' if direction == 0 else 'en dessous'}"
