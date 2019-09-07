# AFFICHAGE DE L'HEURE SUR LA MATRICE

# Importation des modules nécessaires
from sense_hat import SenseHat      # Librairie gérant la carte 'Sense Hat'
import time

# Creation de l'objet Sense Hat
sense = SenseHat()
# Limitation de la luminosité
sense.low_light = True
# Changement de l'orientation de la matrice
sense.set_rotation(0)

# Creation des chiffres au format 4x4
chiffres = [
[[0,1,1,1], # Zero
[0,1,0,1],
[0,1,0,1],
[0,1,1,1]],
[[0,0,1,0], # Un
[0,1,1,0],
[0,0,1,0],
[0,1,1,1]],
[[0,1,1,1], # Deux
[0,0,1,1],
[0,1,1,0],
[0,1,1,1]],
[[0,1,1,1], # Trois
[0,0,1,1],
[0,0,1,1],
[0,1,1,1]],
[[0,1,0,1], # Quatre
[0,1,1,1],
[0,0,0,1],
[0,0,0,1]],
[[0,1,1,1], # Cinq
[0,1,1,0],
[0,0,1,1],
[0,1,1,1]],
[[0,1,0,0], # Six
[0,1,1,1],
[0,1,0,1],
[0,1,1,1]],
[[0,1,1,1], # Sept
[0,0,0,1],
[0,0,1,0],
[0,1,0,0]],
[[0,1,1,1], # Huit
[0,1,1,1],
[0,1,1,1],
[0,1,1,1]],
[[0,1,1,1], # Neuf
[0,1,0,1],
[0,1,1,1],
[0,0,0,1]]
]
pas_de_chiffre = [0,0,0,0]

couleur_heure = [255,0,255] # Magenta
couleur_minute = [0,255,255] # Cyan
couleur_vide = [0,0,0] # Black/Off

# Boucle infinie
while True :
    # Creation d'une liste vide
    image_horloge = []
    # Recuperation de l'heure locale
    heure = 
    minute = 
    # détermination des dizaines et unités pour l'heure
    for index in range(0, 4):
        if (heure >= 10):
            image_horloge.extend(chiffres[int(heure/10)][index])
        else:
            image_horloge.extend(pas_de_chiffre)
        image_horloge.extend(chiffres[int(heure%10)][index])

    # détermination des dizaines et unités pour les minutes
    for index in range(0, 4):
        image_horloge.extend(chiffres[int(minute/10)][index])
        image_horloge.extend(chiffres[int(minute%10)][index])
    
    # Remplissage des couleurs selon heure ou minute
    
    # Affichage de l'horloge digitale
    