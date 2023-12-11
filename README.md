# Projet L2P1
## Description
Ce projet a pour but de calculer les relations spatiales directionnelles entre deux objets à partir de leur histogramme d'angles. 

Les objets sont représentés sous forme de points (pixel) dans un espace en deux dimensions, et l'histogramme d'angles représente la distribution des angles entre chaque paire de points dans chaque objet. 
Les relations spatiales directionnelles qui peuvent être calculées à partir de l'histogramme d'angles comprennent la distance, la barycentre , la position etc.

## Fonctionnement
Le projet est écrit en Python et utilise la bibliothèque OpenCV pour la manipulation d'images , la bibliothèque NumPy pour le calcul d'histogrammes , la bibliothèque matplotlib pour manipulation d'histogramme et la bibliothèque tkinter pour l'interface . 
Le code est divisé en plusieurs fonctions qui effectuent les différentes étapes du calcul des relations spatiales directionnelles.


## Utilisation
Pour utiliser ce projet:
###Methode :
Vous devez avoir Python et les bibliothèques OpenCV , NumPy et Matplotlib installées sur votre ordinateur.
Vous devez installez les requirments (voir Manuel d'utilisation)
Vous pouvez ensuite exécuter le fichier main.py pour exécuter le code principal, oubien exécuter executable.py pour créer un exécutable de main.py vous pouvez ensuite directement lancer le logiciel en cliquant sur main.exe sans utiliser python,pip et les bibliothèques.

###Attention: 
Lorsque vous utilisez les deux méthodes (barycentre et histogramme), vous devez spécifier le pas de l'histogramme et attendre que le résultat de la méthode histogramme s'affiche avant de cliquer sur "Quit"

## Prérequis

- Langage : Python 3.6 ou supérieur
- Bibliothèques : 
  - matplotlib
  - numpy
  - OpenCV
  - tkinter

## Auteurs
Ce projet a été créé par [Hagop Hannachian , Victor Soler, Amy Lo, Amelie Humeau] dans le cadre du cours de [L2 informatique] à l'université [Université Paris Cite].
