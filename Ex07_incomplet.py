#!/usr/bin/env python
# -*- coding: utf-8 -*-

# IUT RENNES - Dpt GEII
# Groupe : Enseignant
# Poste : perso
# Date : 03/10/2016

# CORRESPONDANCE ENTRE LA COULEUR SOUS LE CURSEUR ET CELLE D'UNE LED
# on affiche une image multicolore à l'écran et en déplaçant le curseur
# de la souris sur l'image, la LED prend la couleur correspondante

# Importation des modules nécessaires
import Tkinter
from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

# Fonction appelée lors d'un clic gauche de la souris
def onClick(event) :
	print event.x, event.y
	(r,v,b) = fond.get(event.x, event.y)
	print r,v,b
	# REMPLISSAGE DE LA MATRICE 8x8 AVEC LA COULEUR RECUPEREE

# Mise en place de la fenêtre
fenetre = Tkinter.Tk()
fenetre.geometry("1024x500+100+50")
#fenetre.attributes('-fullscreen', True)
fenetre.title("Sélectionnez une couleur")
# Mise en place d'un bouton pour quitter
bouton_quit = Tkinter.Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quit.pack(side=Tkinter.BOTTOM)
# Mise en place d'une zone de dessin
zone = Tkinter.Canvas(fenetre, width=800, height=450, background='black')
zone.pack()
# Chargement d'une image dans la zone de dessin
fond = Tkinter.PhotoImage(file="images/Matriochka.png")
zoom_l=int(fond.width()/800)
fond = fond.subsample(zoom_l)
mon_fond = zone.create_image(0, 0, anchor=Tkinter.NW, image=fond)
# Ajout d'une gestion d'événement au clic gauche de la souris (uniquement dans la zone de dessin)
zone.bind('<Button-1>', onClick)
# Boucle principale infinie de la fenêtre
fenetre.mainloop()
