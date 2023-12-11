
def barycentre(a, b):

    """
    Fonction qui renvoie les coordonnées de Barycentre des 2 objets

    ENTREE :les 2 objets
    SORTIE : les coords de barycentre de deux objets : cx,cy,cx1,cx2
    """

    # Initialiser les somme des x et y
    sum_x, sum_y = 0, 0
    sum_x1, sum_y1 = 0, 0

    # Parcourir les objets
    for i in range(len(a)):
        x, y = a[i][0], a[i][1]
        sum_x += x
        sum_y += y
    for i in range(len(b)):
        x1, y1 = b[i][0], b[i][1]
        sum_x1 += x1
        sum_y1 += y1

    # calcul barycentre (somme des x ou y) sur (nombre des pixels)
    cx, cy = int(sum_x / len(a)), int(sum_y / len(a))  # Objet A
    cx1, cy1 = int(sum_x1 / len(b)), int(sum_y1 / len(b))  # Objet B

    return cx, cy, cx1, cy1



