import cv2 as cv

def trouver_contour(image):

    """
    Fonction qui trouve les contour de l'objet jaune et de l'objet vert dans une image

    ENTREE : l'image contenant les objets

    SORTIE : deux tableau contenant les contours OpenCV de l'objet jaune et de l'objet vert
    """

    # Convertir l'image en niveaux de gris
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Appliquer la méthode d'OTSU pour binariser l'image (OTSU donne la seuil)
    _, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

    # Trouver les contours dans l'image ouverte
    contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Trier les contours par aire et retourner les deux plus grands
    contours_sorted = sorted(contours, key=cv.contourArea, reverse=True)
    return contours_sorted[0], contours_sorted[1]
