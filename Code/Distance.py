import numpy as np

def dist(x1, y1, x2, y2):
    """
    Fonction qui renvoie la distance entre 2 barycentre

    ENTREE :les 2 barycentre
    SORTIE : la distance
    """

    distance = np.sqrt((x2-x1)**2+(y2-y1)**2)

    return round(distance)

