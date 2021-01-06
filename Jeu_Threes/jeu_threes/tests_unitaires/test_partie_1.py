import os
import sys

my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(my_path + '/../')

print(my_path)

from game.play import init_play

from tiles.tiles_acces import *
from tiles.tiles_moves import get_nb_empty_rooms

from life_cycle.cycle_game import is_game_over, get_score
from ui.play_display import simple_display


# module jeu_threes/game/play
def test_init_play():
    plateau = init_play()

    # Comme on construit le tableau à la main, il est préférable de vérifier qu'il est bien correct.
    assert len(plateau['tiles']) == 16, "Erreur, le plateau n'est pas initialisé à 16 cases."

    print("Test de la fonction init_play: Ok")


# module jeu_threes/tiles/tile_acces
def test_check_indice():
    plateau = init_play()

    assert check_indice(plateau, 0)
    assert check_indice(plateau, 3)
    assert not (check_indice(plateau, 10))
    assert not (check_indice(plateau, 4))
    assert not (check_indice(plateau, -1))

    print("Test de la fonction check_indice: Ok")


# module jeu_threes/tiles/tile_acces
def test_check_room():
    plateau = init_play()

    assert check_room(plateau, 2, 1)
    assert check_room(plateau, 3, 3)
    assert not (check_room(plateau, 10, 2))
    assert not (check_room(plateau, -1, 3))

    print("Test de la fonction check_room: Ok")


# module jeu_threes/tiles/tile_acces
def test_get_value():
    plateau = {'n': 4,
               'nombre_cases_libres': 6,
               'tiles': [6, 2, 3, 2, 0, 2, 6, 2, 0, 2, 2, 0, 1, 0, 0, 0]
    }

    assert get_value(plateau, 0, 0) == 6
    assert get_value(plateau, 2, 3) == 0
    assert get_value(plateau, 1, 3) == 2
    assert get_value(plateau, 3, 0) == 1

    # get_value(plateau, 18, 3) renvoie une erreur.

    print("Test de la fonction get_value: Ok")


# module jeu_threes/tiles/tile_acces
def test_set_value():
    plateau = init_play()

    set_value(plateau, 0, 0, 1)

    assert get_value(plateau, 0, 0) == 1
    assert plateau["nombre_cases_libres"] == 15

    set_value(plateau, 1, 2, 0)

    assert get_value(plateau, 1, 2) == 0
    assert plateau["nombre_cases_libres"] == 15

    set_value(plateau, 2, 3, 6)

    assert get_value(plateau, 2, 3) == 6
    assert plateau["nombre_cases_libres"] == 14

    # set_value(plateau, 18, 3, 1) renvoie une erreur.

    print("Test de la fonction set_value: Ok")


# module jeu_threes/tiles/tile_acces
def test_is_room_empty():
    plateau = init_play()

    set_value(plateau, 0, 1, 2)
    set_value(plateau, 1, 1, 1)
    set_value(plateau, 1, 2, 0)

    assert not (is_room_empty(plateau, 0, 1))
    assert not (is_room_empty(plateau, 1, 1))
    assert is_room_empty(plateau, 1, 2)
    assert is_room_empty(plateau, 3, 2)

    # is_room_empty(15, 2) renvoie une erreur.

    print("Test de la fonction is_room_empty: Ok")


# module jeu_threes/tiles/tiles_moves
def test_get_nb_empty_rooms():
    plateau = {'n': 4,
               'nb_cases_libres': 5,
               'tiles': [6, 2, 3, 0, 2, 6, 2, 0, 2, 2, 0, 1, 0, 0, 0]
               }

    nb_cases_libres = get_nb_empty_rooms(plateau)

    assert nb_cases_libres == 6
    assert plateau['nombre_cases_libres'] == 6

    print("Test de la fonction get_nb_empty_rooms: Ok")


# module jeu_threes/life_cycle/cycle_game
def test_is_game_over():
    plateau = {'n': 4,
               'nb_cases_libres': 6,
               'tiles': [6, 2, 3, 2, 0, 2, 6, 2, 0, 2, 2, 0, 1, 0, 0, 0]}

    assert not (is_game_over(plateau))

    plateau = {'n': 4,
               'nb_cases_libres': 0,
               'tiles': [6, 2, 3, 2, 12, 2, 6, 2, 6, 2, 2, 12, 1, 6, 3, 1]}

    assert is_game_over(plateau)

    print("Test de la fonction is_game_over: Ok")


# module jeu_threes/life_cycle/cycle_game
def test_get_score():
    plateau = init_play()

    assert get_score(plateau) == 0

    plateau = {'n': 4,
               'nb_cases_libres': 0,
               'tiles': [6, 2, 3, 2, 12, 2, 6, 2, 6, 2, 2, 12, 1, 6, 3, 1]}

    assert get_score(plateau) == 68

    print("Test de la fonction get_score: Ok")


# module jeu_threes/ui/play_display
def test_play_display():
    plateau = init_play()

    # Affichage attendu:
    #   0   0   0   0
    #   0   0   0   0
    #   0   0   0   0
    #   0   0   0   0
    simple_display(plateau)

    plateau['tiles'] = [12, 3, 6, 0, 3, 12, 1, 2, 48, 12, 96, 1, 192, 6, 3, 3]

    # Affichage attendu:
    #  12   3   6   0
    #   3  12   1   2
    #  48  12  96   1
    # 192   6   3   3
    simple_display(plateau)

    print("Test de la fonction play_display: Ok")


# Lancement des tests concernant la fonction init_play (partie 1)
test_init_play()

# Lancement des tests concernant la fonction check_indice (partie 1)
test_check_indice()

# Lancement des tests concernant la fonction check_room (partie 1)
test_check_room()

# Lancement des tests concernant la fonction get_value (partie 1)
test_get_value()

# Lancement des tests concernant la fonction set_value (partie 1)
test_set_value()

# Lancement des tests concernant la fonction is_room_empty (partie 1)
test_is_room_empty()

# Lancement des tests concernant la fonction get_nb_empty_rooms (partie 1)
test_get_nb_empty_rooms()

# Lancement des tests concernant la fonction is_game_over (partie 1)
test_is_game_over()

# Lancement des tests concernant la fonction get_score (partie 1)
test_get_score()

# Lancement des tests concernant la fonction play_display (partie 1)
test_play_display()