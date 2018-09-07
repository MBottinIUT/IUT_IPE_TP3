#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module IPE - TPs Raspberry
auteurs : Noms des etudiants
Etablissement : IUT de Rennes - Dpt GEII
Date : 31.07.2018 21:53:31 Paris, Madrid

Commentaires : 
"""

# SAUVEGARDE D'UNE SERIE DE MESURES DE TEMPERATURE DANS UN FICHIER
# ---------------------------------------------------------------- 

# Importation des bibliotheques utiles
# ------------------------------------
import time			# pour la fonction d'attente 'sleep'
from sense_hat import SenseHat	# bibliotheque de la carte sense hat
from pyexcel_ods import save_data	# sudo pip install pyexcel-ods
from collections import OrderedDict
from gpiozero import CPUTemperature

# Instanciation du dictionnaire de données
donnees = OrderedDict()

# Déclaration des listes de mesures vides
???????????????????????????

# Instanciation de l'objet SenseHat
???????????????????????

# Demande des parametres à l'utilisateur
# --------------------------------------
print ("MESURE DE TEMPERATURE AVEC SAUVEGARDE DANS UN FICHIER")
nom_fichier = ?????????????????????????
duree_mesures = ??????????????????????
pas_mesures = ???????????????????????
nombre_mesures = ??????????????????????

# -------------------------
# -- PROGRAMME PRINCIPAL --
# -------------------------
# Sauvegarde de la température mesuree dans le fichier
# ----------------------------------------------------
for i in range(nombre_mesures+1) :	
	try :
		# Determination de la  température
		????????????????????????????????
		# Ajout du numéro de mesure à la liste_temporelle
		???????????????????????????????????
		# Ajout de la temperature à la liste_temperature
		????????????????????????????????????
		# Animation durant la mesure permettant de savoir que le programme n'est pas bloque
		sense.show_message("..", scroll_speed=0.05, text_colour=(255,255,255), back_colour=(0,0,0))
		# Attente de la duree choisie par l'utilisateur entre chaque mesure
		?????????????????????????????????
	except KeyboardInterrupt :
		sense.clear()
		print ("\nAu revoir ...")
		break
# Fin du programme lorsque le nombre de mesures demande est atteint
donnees.update({"Mesure de temperature": [liste_temporelle, liste_temperature]})
save_data(nom_fichier+".ods", donnees)
print ""
print "votre fichier " + nom_fichier + ".ods a bien été sauvegardé"
