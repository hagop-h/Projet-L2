import sys #importation de sys pour "sys.exit()"

#importation des deux méthodes
from main_barycentre import main_Barycentre
from main_histogramme import main_histogramme

#importation de tkinter pour l'interface graphique
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


def imagepath():
    """
    Fonction qui permet de choisir une image dans l'explorateur de fichier et renvoie le chemin
    ENTREE : None
    SORTIE : chaîne de caractères
    """ 
    image_path = filedialog.askopenfilename(title="Selectionnez une image", filetypes=(
        ("Fichier d'images", "*.jpg;*.jpeg;*.png"), ("Tout les fichiers", "*.*")))
    if image_path == "":
        sys.exit()
    return image_path


def close_window():
    """
    Méthode permettant de quitter le programme
    ENTREE : None
    SORTIE : None
    """
    sys.exit()



# Méthode Barycentre
def methodeBarycentre():
    """
    Méthode permettant de créer une fenetre, calculer "main barycentre" et afficher le résultat
    ENTREE : None
    SORTIE : None
    """
    #Destruction de la fenêtre principale
    root.destroy()
    #Création de la fenetre barycentre
    fenetre = Tk()
    fenetre.title("Méthode Barycentre")
    fenetre.geometry("400x200")
    #Création du conteneur
    affichage = ttk.Frame(fenetre,padding=50)
    affichage.grid()
    
    #Calcul et affichage du résultat de la méthode barycentre
    e,directionBarycentre=main_Barycentre(image_path)
    chaine = "resultat : l'objet vert est " + directionBarycentre + " de l'objet jaune"
    ttk.Label(affichage, text=chaine).grid(column=1, row=0)
    ttk.Button(affichage, text="Quitter", command=close_window).grid(column=1, row=2)

#Méthode Histogramme d'angle
def methodeHisto():
    """
    Méthode permettant de créer une fenetre et récupérer le pas de l'histogramme
    ENTREE : None
    SORTIE : None
    """
    
    #On fait un "try" pour éviter l'erreur où root n'existe plus car elle est déjà détruite
    #par la méthode barycentre.
    try:
        root.destroy()
    except:
        pass

    #création de la fenêtre
    global histogramme
    histogramme = Tk()
    histogramme.title("Méthode avec l'histogramme d'angle")
    histogramme.geometry("200x200")
    #création du conteneur
    global affichageH
    affichageH = ttk.Frame(histogramme, padding=50)
    affichageH.grid()
    #récupération du pas
    entry = Entry(histogramme, width=5)
    entry.grid(column=0, row=1)
    
    #affichage du bouton permettant de récupérer le pas qui renvoie à la fonction "get_pas(ent)"
    ttk.Button(affichageH, text="Saisir le pas", command=lambda: get_pas(entry)).grid(column=1, row=1)

#Appel aux deux méthodes
def methodeBaryHisto():
    """
    Méthode appelant les deux autres méthodes (barycentre et histogramme)
    ENTREE : None
    SORTIE : None
    """
    methodeBarycentre()
    methodeHisto()


def get_pas(ent):
    """
    Méthode permettant de stocker le pas dans une variable et faire appel à la fonction histo()
    ENTREE : objet de type Entry
    SORTIE : None
    """
    #conversion du pas en entier
    pas = int(ent.get())
    #appel à la fonction qui calcule l'histogramme grâce au pas saisi
    histo(pas)


def histo(pas=180):
    """
    Méthode permettant de calculer "main histogramme" et afficher le résultat
    ENTREE : entier(int)
    SORTIE : None
    """
    #récupération des variables globales
    global affichageH
    global histogramme
    #modification de la taille de la fenêtre pour s'adapter au résultat
    histogramme.geometry("500x200")
    #calcul de l'histogramme et récupération dans une chaine du réultat
    chaine = main_histogramme(image_path, pas)
    
    #affichage du résultat et ajout du bouton "Quitter"
    ttk.Label(affichageH, text=chaine).grid(column=0, row=1)
    ttk.Button(affichageH, text="Quitter", command=close_window).grid(column=2, row=1)

#Création de la fenêtre principale
root = Tk()
root.title("Choix de la méthode")
root.geometry("600x500")

#Création de son conteneur
frm = ttk.Frame(root, padding=50)
frm.grid()

#récupération de l'image 
#(La récupération de l'image se fait après la création de la fenêtre pour
# éviter d'avoir une fenêtre "fantôme")
image_path = imagepath()

#Affichage de l'image choisie
photo = PhotoImage(master=root, file=image_path)
canvas = Canvas(root, width=244, height=244)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.grid()

#Affichage des boutons reliés aux différentes fonctions
ttk.Button(frm, text="Quitter", command=close_window).grid(column=4, row=0)
ttk.Button(frm, text="Méthode barycentre", command=methodeBarycentre).grid(column=1, row=0)
ttk.Button(frm, text="Méthode Histogramme", command=methodeHisto).grid(column=2, row=0)
ttk.Button(frm, text="utiliser les deux méthodes", command=methodeBaryHisto).grid(column=3, row=0)

root.mainloop()
