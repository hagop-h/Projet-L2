from intersection import *
def main_histogramme(image_path,pas=180):
    """
    Fonction qui calcule la relation spatiale par histogramme d'angle et qui renvoie le résultat
    ENTREE : chaîne de caractères(chemin de l'image) x entier(pas de l'histogramme)
    SORTIE : chaine de caractères(résultat)
    """
    
    #calcul de l'histogramme
    histogramme = histo(image_path,pas)
    chaine = ""
    
    #Calcul de chaque intersection entre l'histogramme et chaque prototype(Haut,Bas,Droite,Gauche)
    x,prototypeH = proto(pas,3)
    interH = intersection(prototypeH,histogramme)
    x,prototypeB = proto(pas,2)
    interB = intersection(prototypeB,histogramme)
    x,prototypeD = proto(pas,0)
    interD = intersection(prototypeD,histogramme)
    x,prototypeG = proto(pas,1)
    interG = intersection(prototypeG,histogramme)

    #Calcul de l'eloignement de l'intersection et le max de chaque proto
    #Et renvoie dans une chaine de caractère
    chaine += "L'objet vert {} au dessus de l'objet jaune\n".format(eloignement(interH,prototypeH))
    chaine += "L'objet vert {} en dessous de l'objet jaune\n".format(eloignement(interB,prototypeB))
    chaine +="L'objet vert {} à droite de l'objet jaune\n".format(eloignement(interD,prototypeD))
    chaine += "L'objet vert {} à gauche de l'objet jaune\n".format(eloignement(interG,prototypeG))
    
    
    #Retour de la chaine final contenant les 4 directions
    return chaine