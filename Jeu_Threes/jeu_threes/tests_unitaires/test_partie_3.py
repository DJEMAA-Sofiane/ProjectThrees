import os
import sys

my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(my_path + '/../')

from ui.user_entries import get_user_move, get_user_menu
from game.play import create_new_play
from life_cycle.play import save_game, restore_game


# module jeu_threes/game/play
def test_create_new_play():

    partie = create_new_play()

    tiles = partie['plateau']['tiles']

    value1, value2 = False, False
    for i in range(0, len(tiles)):

        if tiles[i] == 1:
            value1 = True
        elif tiles[i] == 2:
            value2 = True

    assert value1 and value2     # Vérification de la présence des tuiles de départ de valeur 1 et 2.
    assert partie['score'] == 3  # Vérification du score de départ.

    print("Test de la fonction create_new_play: Ok")


# module jeu_threes/ui/user_entries
def test_get_user_move():
    # Pour faire les tests de la fonction, retirez les '#' en début de ligne
    # là où il y a des assertions et effectuez les saisies demandées.

    # assert get_user_move() == 'h'  # Saisir h. La fonction doit retourner h.
    # assert get_user_move() == 'h'  # Saisir H. La fonction doit retourner h.
    # assert get_user_move() == 'b'  # Saisir 3 puis e puis b. La fonction doit retourner b.
    # assert get_user_move() == 'b'  # Saisir 3 puis e puis B. La fonction doit retourner b.

    # Note: On vérifie aussi d et g pour vérifier qu'on peut bien faire tous les mouvements (h, b, d, g).

    # assert get_user_move() == 'd'  # Saisir d. La fonction doit retourner d.
    # assert get_user_move() == 'g'  # Saisir g. La fonction doit retourner g.

    print("Test de la fonction get_user_move: Ok")


# module jeu_threes/ui/user_entries
def test_get_user_menu():
    # Pour faire les tests de la fonction, retirez les '#' en début de ligne
    # là où il y a des assertions et effectuez les saisies demandées.

    # Cas n°1: Aucune partie n'est en cours (partie = None).
    # assert get_user_menu(None) == 'N'  # Saisir N. La fonction doit retourner N.
    # assert get_user_menu(None) == 'N'  # Saisir n. La fonction doit retourner N.
    # assert get_user_menu(None) == 'L'  # Saisir 5 puis x puis B puis l. La fonction doit retourner L.
    # assert get_user_menu(None) == 'Q'  # Saisir c puis C puis q. La fonction doit retourner Q.
    # assert get_user_menu(None) == 'L'  # Saisir s puis S puis L. La fonction doit retourner L.

    # Cas n°2: Une partie est en cours (partie != None).

    partie = create_new_play()

    # assert get_user_menu(partie) == 'N'  # Saisir N. La fonction doit retourner N.
    # assert get_user_menu(partie) == 'N'  # Saisir n. La fonction doit retourner N.
    # assert get_user_menu(partie) == 'L'  # Saisir 5 puis x puis B puis l. La fonction doit retourner L.
    # assert get_user_menu(partie) == 'Q'  # Saisir 4 puis a puis q. La fonction doit retourner Q.
    # assert get_user_menu(partie) == 'C'  # Saisir c. La fonction doit retourner C.
    # assert get_user_menu(partie) == 'S'  # Saisir s. La fonction doit retourner S.

    print("Test de la fonction get_user_menu: Ok")


# module jeu_threes/life_cycle/play
def test_save_game():
    # Test avec la sauvegarde d'une partie en cours.
    partie = {"plateau": {"n": 4, "nombre_cases_libres": 6, "tiles": [6, 2, 3, 2, 0, 2, 1, 2, 6, 2, 0, 0, 0, 6, 1, 1]},
              "next_tile": {"mode": "encours", '0': {"val": 3, "lig": 0, "col": 1}, "check": True},
              "score": 34}

    save_game(partie)

    # Le fichier 'game_saved.json' doit contenir:
    #
    # partie = {"plateau": {"n": 4, "nombre_cases_libres": 6, "tiles": [6, 2, 3, 2, 0, 2, 1, 2, 6, 2, 0, 0, 0, 6, 1, 1]},
    #           "next_tile": {"mode": "encours", '0': {"val": 3, "lig": 0, "col": 1}, "check": True},
    #           "score": 34}

    # Note: Le formatage n'est pas pris en compte dans le fichier, il a pour seul but de faciliter la lecture.

    print("Test de la fonction save_game: Ok")


# module jeu_threes/life_cycle/play
def test_restore_game():
    partie = {"plateau": {"n": 4, "nombre_cases_libres": 6, "tiles": [6, 2, 3, 2, 0, 2, 1, 2, 6, 2, 0, 0, 0, 6, 1, 1]},
              "next_tile": {"mode": "encours", '0': {"val": 3, "lig": 0, "col": 1}, "check": True},
              "score": 34}

    save_game(partie)  # Sauvegarde de la partie

    assert partie == restore_game()  # Vérification que la partie restaurée correspond à celle sauvegardée.

    print("Test de la fonction restore_game: Ok")


# Lancement des tests concernant la fonction create_new_play (partie 3)
test_create_new_play()

# Lancement des tests concernant la fonction get_user_move (partie 3)
test_get_user_move()

# Lancement des tests concernant la fonction get_user_menu (partie 3)
test_get_user_menu()

# Lancement des tests concernant la fonction save_game (partie 3)
test_save_game()

# Lancement des tests concernant la fonction restore_game (partie 3)
test_restore_game()