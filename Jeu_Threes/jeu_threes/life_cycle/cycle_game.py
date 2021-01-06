import os
import sys

my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(my_path + '/../')

from tiles.tiles_moves import get_nb_empty_rooms


# Fonction de la partie 1
def is_game_over(plateau):
    """
	Permet de vérifier si une partie est terminée.

	:param plateau: Un dictionnaire correspondant à un plateau de jeu.

	:return: True si la partie est terminée, False sinon.
	"""
    return get_nb_empty_rooms(plateau) == 0  # Si le nombre de tuiles libres est égal à 0, la partie est terminée.


# Fonction de la partie 1
def get_score(plateau):
    """
	Retourne le score du plateau

	:param plateau: Un dictionnaire correspondant à un plateau de jeu.

	:return: un entier correspondant au score du plateau.
	"""
    score = 0

    for i in range(0, len(plateau['tiles'])):
        score += plateau['tiles'][i]  # Ajout du score de la tuile courante au score général.

    return score
