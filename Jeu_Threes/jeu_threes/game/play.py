import os
import sys

my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(my_path + '/../')

from life_cycle.cycle_game import get_score
from tiles.tiles_moves import get_next_alea_tiles, put_next_tiles

########################################################
###                    PARTIE 1                      ###
########################################################


# Fonction de la partie 1
def init_play():
    """
	Retourne un plateau correspondant à une nouvelle partie. 

	Une nouvelle partie est un dictionnaire avec les couples clé:valeur suivants:
	- 'n': vaut 4.
	- 'nombre_cases_libres': vaut 16 au départ.
	- 'tiles': Un tableau de 4*4 cases initialisées à 0.

	:return: Un dictionnaire correspondant à un plateau de jeu.
	"""
    return {'n': 4, 'nombre_cases_libres': 16, 'tiles': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}


########################################################
###                    PARTIE 3                      ###
########################################################


# Fonction de la partie 3
def create_new_play():
    """
    Crée une nouvelle partie sous la forme d'un dictionnaire.

    Ses clés sont les suivantes:
    - 'plateau': Un dictionnaire correspondant au plateau de jeu.
    - 'next_tile': Un dictionnairement mémorisant la prochaine tuile à placer (vide au départ).
    - 'score': Un entier correspondant au score courant du joueur.

    :return: Un dictionnaire correspondant à la partie créée.
    """
    plateau = init_play()

    tiles = get_next_alea_tiles(plateau, "init")  # Génération des tuiles de départ.

    put_next_tiles(plateau, tiles)                # Ajout des tuiles de départ dans le plateau.

    return {'plateau': plateau, 'next_tile': {}, 'score': get_score(plateau)}




