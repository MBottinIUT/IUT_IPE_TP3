#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module IPE - TPs Raspberry
auteurs : Noms des etudiants
Etablissement : IUT de Rennes - Dpt GEII
Date : 31.07.2018 21:53:31 Paris, Madrid

Commentaires : 
"""
# AFFICHAGE D'UNE IMAGE ANIMEE

# Importation des modules nécessaires
from sense_hat import SenseHat		# Librairie gérant la carte 'Sense Hat'
from time import sleep

# Instanciation de l'objet SenseHat
sense = SenseHat()

# Définition des couleurs (trois composantes, ordre : r,v,b)
r = [255,0,0]
b = [255,255,255]
n = [0,0,0]

# Déclaration des deux tableaux contenant chacun une image 8x8
heart1 = [
    n,n,n,n,n,n,n,n,
    n,r,r,n,n,r,r,n,
    r,r,b,b,r,r,r,r,
    r,b,r,r,r,r,r,r,
    n,r,r,r,r,r,r,n,
    n,n,r,r,r,r,n,n,
    n,n,n,r,r,n,n,n,
    n,n,n,n,n,n,n,n,
    ]

heart2 = [
    n,n,n,n,n,n,n,n,
    n,n,n,n,n,n,n,n,
    n,n,r,n,n,r,n,n,
    n,r,r,b,r,r,r,n,
    n,n,r,r,r,r,n,n,
    n,n,n,r,r,n,n,n,
    n,n,n,n,n,n,n,n,
    n,n,n,n,n,n,n,n,
    ]

# -------------------------
# -- PROGRAMME PRINCIPAL --
# -------------------------	
# Boucle infinie
while True :
	try :
		
	except KeyboardInterrupt :
		sense.clear()
		print "Au revoir..."
		break
    
    
