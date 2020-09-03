# DE ELECTRONIQUE A SECOUER
# (utilisation des deux axes x et y uniquement)

# Importation des bibliotheques utiles
# ------------------------------------
from sense_hat import SenseHat
import time
import random

# Instanciation de l'objet SenseHat
sense = SenseHat()
sense.clear()

# Affichage d'un message lors du premier lancement


# Définition des couleurs utiles
noir = [0, 0, 0]
rouge = [255, 0, 0]

# Seuil de détection
SEUIL = 

# Définition des différentes faces du dé
un = [
noir,noir,noir,noir,noir,noir,noir,noir,
noir,noir,noir,noir,noir,noir,noir,noir,
noir,noir,noir,noir,noir,noir,noir,noir,
noir,noir,noir,rouge,rouge,noir,noir,noir,
noir,noir,noir,rouge,rouge,noir,noir,noir,
noir,noir,noir,noir,noir,noir,noir,noir,
noir,noir,noir,noir,noir,noir,noir,noir,
noir,noir,noir,noir,noir,noir,noir,noir,
]

deux = [
noir,noir,noir,noir,noir,noir,noir,noir,
noir,rouge,rouge,noir,noir,noir,noir,noir,
noir,rouge,rouge,noir,noir,noir,noir,noir,
noir,noir,noir,noir,noir,noir,noir,noir,
noir,noir,noir,noir,noir,noir,noir,noir,
noir,noir,noir,noir,rouge,rouge,noir,noir,
noir,noir,noir,noir,rouge,rouge,noir,noir,
noir,noir,noir,noir,noir,noir,noir,noir,
]

trois = [
rouge,rouge,noir,noir,noir,noir,noir,noir,
rouge,rouge,noir,noir,noir,noir,noir,noir,
noir,noir,noir,noir,noir,noir,noir,noir,
noir,noir,noir,rouge,rouge,noir,noir,noir,
noir,noir,noir,rouge,rouge,noir,noir,noir,
noir,noir,noir,noir,noir,noir,noir,noir,
noir,noir,noir,noir,noir,noir,rouge,rouge,
noir,noir,noir,noir,noir,noir,rouge,rouge,
]

quatre = [
noir,noir,noir,noir,noir,noir,noir,noir,
noir,rouge,rouge,noir,noir,rouge,rouge,noir,
noir,rouge,rouge,noir,noir,rouge,rouge,noir,
noir,noir,noir,noir,noir,noir,noir,noir,
noir,noir,noir,noir,noir,noir,noir,noir,
noir,rouge,rouge,noir,noir,rouge,rouge,noir,
noir,rouge,rouge,noir,noir,rouge,rouge,noir,
noir,noir,noir,noir,noir,noir,noir,noir,
]

cinq = [
rouge,rouge,noir,noir,noir,noir,rouge,rouge,
rouge,rouge,noir,noir,noir,noir,rouge,rouge,
noir,noir,noir,noir,noir,noir,noir,noir,
noir,noir,noir,rouge,rouge,noir,noir,noir,
noir,noir,noir,rouge,rouge,noir,noir,noir,
noir,noir,noir,noir,noir,noir,noir,noir,
rouge,rouge,noir,noir,noir,noir,rouge,rouge,
rouge,rouge,noir,noir,noir,noir,rouge,rouge,
]

six = [
rouge,rouge,noir,noir,noir,noir,rouge,rouge,
rouge,rouge,noir,noir,noir,noir,rouge,rouge,
noir,noir,noir,noir,noir,noir,noir,noir,
rouge,rouge,noir,noir,noir,noir,rouge,rouge,
rouge,rouge,noir,noir,noir,noir,rouge,rouge,
noir,noir,noir,noir,noir,noir,noir,noir,
rouge,rouge,noir,noir,noir,noir,rouge,rouge,
rouge,rouge,noir,noir,noir,noir,rouge,rouge,
]

# Fonction de lancer de dé --> renvoie image du dé avec valeur aléatoire
def lance_de():
    r = random.randint(1,6)
    if r == 1:
        sense.set_pixels(un)
    elif r == 2:
        sense.set_pixels(deux)
    elif r == 3:
        sense.set_pixels(trois)
    elif r == 4:
        sense.set_pixels(quatre)
    elif r == 5:
        sense.set_pixels(cinq)
    elif r == 6:
        sense.set_pixels(six)

# Boucle infinie
while True:
    # Récupération des valeurs de l'accéléromètre suivant ses trois axes

    # Valeurs absolues pour un fonctionnement dans les deux directions de chaque axe

    # Test si un seuil est franchi pour chaque axe

        # Affiche le dé
		
    # Attente pour la visualisation du résultat
    time.sleep(3)
