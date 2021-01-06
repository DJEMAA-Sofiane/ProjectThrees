import os
import sys

my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(my_path + '/../')

from game.play import init_play
from tiles.tiles_acces import get_value, is_room_empty
from tiles.tiles_moves import *


# module jeu_threes/tiles/tiles_moves
def test_get_free_space():
    plateau = init_play()

    lig, col = get_free_space(plateau)

    assert is_room_empty(plateau, lig, col)

    plateau = {'n': 4,
               'nb_cases_libres': 1,
               'tiles': [6, 2, 3, 12, 2, 6, 2, 12, 2, 2, 12, 1, 12, 12, 12, 0]
               }

    lig, col = get_free_space(plateau)

    assert lig == 3 and col == 3  # Vérification que les coordonnées de la case libre correspondent bien à celles de l'unique case libre disponible.
    assert is_room_empty(plateau, lig, col)

    print("Test de la fonction get_free_space: Ok")


# module jeu_threes/tiles/tiles_moves
def test_get_tile():
    plateau = init_play()

    tile = get_tile(plateau, 2)

    assert tile['val'] == 2
    # Vérification de la validité des coordonnées
    assert 0 <= tile['lig'] < plateau['n']
    assert 0 <= tile['col'] < plateau['n']

    plateau = {'n': 4,
               'nb_cases_libres': 1,
               'tiles': [6, 2, 3, 12, 2, 6, 2, 12, 2, 2, 12, 1, 12, 12, 12, 0]
               }

    tile = get_tile(plateau, 1)

    assert tile['val'] == 1
    assert tile['lig'] == 3  # Vérification de la ligne
    assert tile['col'] == 3  # Vérification de la colonne

    print("Test de la fonction get_tile: Ok")


# module jeu_threes/tiles/tiles_moves
def test_get_next_alea_tiles():
    plateau = init_play()

    tiles = get_next_alea_tiles(plateau, "init")

    # Vérification de l'existence de deux tuiles de valeurs 1 et 2.
    # On ne revérifie pas les coordonnées car elles sont déjà vérifiées dans les autres fonctions de test unitaire.
    assert tiles['0']['val'] == 1
    assert tiles['1']['val'] == 2
    assert tiles['check']

    plateau = {'n': 4,
               'nb_cases_libres': 1,
               'tiles': [6, 2, 3, 12, 2, 6, 2, 12, 2, 2, 12, 1, 12, 12, 12, 0]
               }

    tiles = get_next_alea_tiles(plateau, "encours")

    # Vérification de l'existance d'une seule tuile dont la valeur est comprise entre 1 et 3 (inclus).
    assert 1 <= tiles['0']['val'] <= 3
    assert not tiles['check']

    print("Test de la fonction get_next_alea_tiles: Ok")


# module jeu_threes/tiles/tiles_moves
def test_put_next_tiles():
    plateau = init_play()

    tiles = get_next_alea_tiles(plateau, "init")  # Tests avec le mode 'init'
    put_next_tiles(plateau, tiles)

    assert not is_room_empty(plateau, tiles['0']['lig'], tiles['0']['col'])
    assert not is_room_empty(plateau, tiles['1']['lig'], tiles['1']['col'])

    tiles = get_next_alea_tiles(plateau, "encours")  # Tests avec le mode 'encours'
    put_next_tiles(plateau, tiles)

    assert not is_room_empty(plateau, tiles['0']['lig'], tiles['0']['col'])

    print("Test de la fonction put_next_tiles: Ok")


# module jeu_threes/tiles/tiles_moves
def test_line_pack():
    tiles = [0, 2, 0, 0,
             0, 2, 3, 3,
             0, 2, 2, 0,
             0, 0, 0, 0]

    plateau = {'n': 4, 'nombre_cases_libres': 10, 'tiles': tiles}

    # Vérification du tassement de la ligne 1 vers la gauche.
    line_pack(plateau, 1, 0, 1)
    assert get_value(plateau, 1, 0) == 2
    assert get_value(plateau, 1, 1) == 3
    assert get_value(plateau, 1, 2) == 3
    assert get_value(plateau, 1, 3) == 0

    # Vérification du tassement de la ligne 1 vers la gauche.
    line_pack(plateau, 1, 2, 1)
    assert get_value(plateau, 1, 0) == 2
    assert get_value(plateau, 1, 1) == 3
    assert get_value(plateau, 1, 2) == 0
    assert get_value(plateau, 1, 3) == 0

    # Vérification du tassement de la ligne 1 vers la gauche.
    line_pack(plateau, 1, 2, 1)
    assert get_value(plateau, 1, 0) == 2
    assert get_value(plateau, 1, 1) == 3
    assert get_value(plateau, 1, 2) == 0
    assert get_value(plateau, 1, 3) == 0

    # Vérification du tassement de la ligne 1 vers la droite.
    line_pack(plateau, 1, 3, 0)  # Vers la droite
    assert get_value(plateau, 1, 0) == 0
    assert get_value(plateau, 1, 1) == 2
    assert get_value(plateau, 1, 2) == 3
    assert get_value(plateau, 1, 3) == 0

    # Vérification du tassement de la ligne 2 vers la droite.
    line_pack(plateau, 2, 2, 0)
    assert get_value(plateau, 2, 0) == 0
    assert get_value(plateau, 2, 1) == 0
    assert get_value(plateau, 2, 2) == 2
    assert get_value(plateau, 2, 3) == 0

    print("Test de la fonction line_pack: Ok")


# module jeu_threes/tiles/tiles_moves
def test_column_pack():
    tiles = [0, 1, 0, 0,
             0, 2, 3, 3,
             0, 4, 2, 0,
             0, 3, 4, 0]

    plateau = {'n': 4, 'nombre_cases_libres': 2, 'tiles': tiles}

    # Vérification du tassement de la colonne 1 vers le haut.
    column_pack(plateau, 1, 0, 1)
    assert get_value(plateau, 0, 1) == 2
    assert get_value(plateau, 1, 1) == 4
    assert get_value(plateau, 2, 1) == 3
    assert get_value(plateau, 3, 1) == 0

    # Vérification du tassement de la colonne 2 vers le haut.
    column_pack(plateau, 2, 2, 1)
    assert get_value(plateau, 0, 2) == 0
    assert get_value(plateau, 1, 2) == 3
    assert get_value(plateau, 2, 2) == 4
    assert get_value(plateau, 3, 2) == 0

    # Vérification du tassement de la colonne 2 vers le bas.
    column_pack(plateau, 2, 2, 0)
    assert get_value(plateau, 0, 2) == 0
    assert get_value(plateau, 1, 2) == 0
    assert get_value(plateau, 2, 2) == 3
    assert get_value(plateau, 3, 2) == 0

    # Vérification du tassement de la colonne 3 vers le bas.
    column_pack(plateau, 3, 3, 0)
    assert get_value(plateau, 0, 2) == 0
    assert get_value(plateau, 1, 2) == 0
    assert get_value(plateau, 2, 2) == 3
    assert get_value(plateau, 3, 2) == 0

    print("Test de la fonction column_pack: Ok")


# module jeu_threes/tiles/tiles_moves
def test_is_fusion_possible():
    assert is_fusion_possible(1, 2)
    assert is_fusion_possible(2, 1)
    assert is_fusion_possible(3, 3)
    assert is_fusion_possible(6, 6)

    assert not is_fusion_possible(1, 3)
    assert not is_fusion_possible(6, 2)
    assert not is_fusion_possible(6, 3)

    print("Test de la fonction is_fusion_possible: Ok")


# module jeu_threes/tiles/tiles_moves
def test_line_move():
    tiles = [1, 2, 1, 0,
             0, 2, 3, 3,
             0, 2, 2, 2,
             6, 12, 0, 0]

    plateau = {'n': 4, 'nombre_cases_libres': 5, 'tiles': tiles}

    # Vérification avec une fusion (1, 2).
    line_move(plateau, 0, 1)  # Mouvement de la ligne 0 vers la gauche.
    assert get_value(plateau, 0, 0) == 3
    assert get_value(plateau, 0, 1) == 1
    assert get_value(plateau, 0, 2) == 0
    assert get_value(plateau, 0, 3) == 0

    # Vérification avec une fusion de deux multiples de 3 identiques.
    line_move(plateau, 1, 0)  # Mouvement de la ligne 1 vers la droite.
    assert get_value(plateau, 1, 0) == 0
    assert get_value(plateau, 1, 1) == 0
    assert get_value(plateau, 1, 2) == 2
    assert get_value(plateau, 1, 3) == 6

    # Vérification avec la non fusion de deux nombres différents multiples de 3.
    line_move(plateau, 3, 1)  # Mouvement de la ligne 3 vers la gauche.
    assert get_value(plateau, 3, 0) == 6
    assert get_value(plateau, 3, 1) == 12
    assert get_value(plateau, 3, 2) == 0
    assert get_value(plateau, 3, 3) == 0

    # Vérification avec la non fusion de deux nombres identiques non multiples de 3.
    line_move(plateau, 2, 0)  # Mouvement de la ligne 2 vers la droite.
    assert get_value(plateau, 2, 0) == 0
    assert get_value(plateau, 2, 1) == 2
    assert get_value(plateau, 2, 2) == 2
    assert get_value(plateau, 2, 3) == 2

    print("Test de la fonction line_move: Ok")


# module jeu_threes/tiles/tiles_moves
def test_column_move():
    tiles = [1, 2, 2, 6,
             2, 2, 3, 3,
             0, 3, 6, 6,
             6, 12, 3, 6]

    plateau = {'n': 4, 'nombre_cases_libres': 5, 'tiles': tiles}

    # Vérification avec une fusion (1, 2).
    column_move(plateau, 0, 1)  # Mouvement de la colonne 0 vers le haut.
    assert get_value(plateau, 0, 0) == 3
    assert get_value(plateau, 1, 0) == 0
    assert get_value(plateau, 2, 0) == 6
    assert get_value(plateau, 3, 0) == 0

    # Vérification avec une fusion de deux multiples de 3 identiques.
    column_move(plateau, 3, 0)  # Mouvement de la colonne 3 vers le bas.
    assert get_value(plateau, 0, 3) == 0
    assert get_value(plateau, 1, 3) == 6
    assert get_value(plateau, 2, 3) == 3
    assert get_value(plateau, 3, 3) == 12

    # Vérification avec la non fusion de deux nombres différents multiples de 3.
    column_move(plateau, 1, 0)  # Mouvement de la colonne 1 vers le bas.
    assert get_value(plateau, 0, 1) == 2
    assert get_value(plateau, 1, 1) == 2
    assert get_value(plateau, 2, 1) == 3
    assert get_value(plateau, 3, 1) == 12

    # Vérification avec la non fusion de deux nombres identiques non multiples de 3.
    column_move(plateau, 1, 1)  # Mouvement de la colonne 1 vers le bas.
    assert get_value(plateau, 0, 1) == 2
    assert get_value(plateau, 1, 1) == 2
    assert get_value(plateau, 2, 1) == 3
    assert get_value(plateau, 3, 1) == 12

    print("Test de la fonction column_move: Ok")


# module jeu_threes/tiles/tiles_moves
def test_lines_move():
    tiles = [1, 2, 0, 2,
             3, 3, 6, 6,
             2, 2, 2, 2,
             6, 6, 2, 1]

    plateau = {'n': 4, 'nombre_cases_libres': 1, 'tiles': tiles}

    lines_move(plateau, 1)  # Mouvement de toutes les lignes vers la gauche.

    moved_tiles = [3, 0, 2, 0,
                   6, 6, 6, 0,
                   2, 2, 2, 2,
                   12, 2, 1, 0]

    # Vérification des résultats.
    for i in range(0, len(moved_tiles)):
        assert moved_tiles[i] == plateau['tiles'][i]

    lines_move(plateau, 0)  # Mouvement de toutes les lignes vers la droite (sans fusion).

    moved_tiles = [0, 3, 0, 2,
                   0, 6, 6, 6,
                   2, 2, 2, 2,
                   0, 12, 2, 1]

    # Vérification des résultats.
    for i in range(0, len(moved_tiles)):
        assert moved_tiles[i] == plateau['tiles'][i]

    moved_tiles = [0, 0, 3, 2,
                   0, 0, 6, 12,
                   2, 2, 2, 2,
                   0, 0, 12, 3]

    lines_move(plateau, 0)  # Mouvement de toutes les lignes vers la droite (avec fusion).

    # Vérification des résultats.
    for i in range(0, len(moved_tiles)):
        assert moved_tiles[i] == plateau['tiles'][i]

    print("Test de la fonction lines_move: Ok")


# module jeu_threes/tiles/tiles_moves
def test_columns_move():
    tiles = [1, 2, 0, 2,
             2, 3, 6, 1,
             0, 6, 2, 3,
             6, 6, 2, 3]

    plateau = {'n': 4, 'nombre_cases_libres': 2, 'tiles': tiles}

    columns_move(plateau, 1)  # Mouvement de toutes les colonnes vers le haut.

    moved_tiles = [3, 2, 6, 3,
                   0, 3, 2, 3,
                   6, 12, 2, 3,
                   0, 0, 0, 0]

    # Vérification des résultats.
    for i in range(0, len(moved_tiles)):
        assert moved_tiles[i] == plateau['tiles'][i]

    columns_move(plateau, 0)  # Mouvement de toutes les colonnes vers le bas.

    moved_tiles = [0, 0, 0, 0,
                   3, 2, 6, 3,
                   0, 3, 2, 3,
                   6, 12, 2, 3]

    # Vérification des résultats.
    for i in range(0, len(moved_tiles)):
        assert moved_tiles[i] == plateau['tiles'][i]

    columns_move(plateau, 0)  # Mouvement de toutes les colonnes vers le bas.

    moved_tiles = [0, 0, 0, 0,
                   0, 2, 6, 0,
                   3, 3, 2, 3,
                   6, 12, 2, 6]

    # Vérification des résultats.
    for i in range(0, len(moved_tiles)):
        assert moved_tiles[i] == plateau['tiles'][i]

    print("Test de la fonction columns_move: Ok")


# module jeu_threes/tiles/tiles_moves
def test_play_move():
    tiles = [1, 2, 0, 2,
             2, 3, 6, 1,
             0, 6, 2, 3,
             6, 6, 2, 1]

    plateau = {'n': 4, 'nombre_cases_libres': 2, 'tiles': tiles}

    play_move(plateau, 'g')  # Mouvement vers la gauche.

    moved_tiles = [3, 0, 2, 0,
                   2, 3, 6, 1,
                   6, 2, 3, 0,
                   12, 2, 1, 0]

    # Vérification des résultats.
    for i in range(0, len(moved_tiles)):
        assert moved_tiles[i] == plateau['tiles'][i]

    play_move(plateau, 'd')  # Mouvement vers la droite.

    moved_tiles = [0, 3, 0, 2,
                   2, 3, 6, 1,
                   0, 6, 2, 3,
                   0, 12, 2, 1]

    # Vérification des résultats.
    for i in range(0, len(moved_tiles)):
        assert moved_tiles[i] == plateau['tiles'][i]

    play_move(plateau, 'h')  # Mouvement vers le haut.

    moved_tiles = [2, 6, 6, 3,
                   0, 6, 2, 3,
                   0, 12, 2, 1,
                   0, 0, 0, 0]

    # Vérification des résultats.
    for i in range(0, len(moved_tiles)):
        assert moved_tiles[i] == plateau['tiles'][i]

    play_move(plateau, 'b')  # Mouvement vers le bas.

    moved_tiles = [0, 0, 0, 0,
                   2, 6, 6, 3,
                   0, 6, 2, 3,
                   0, 12, 2, 1]

    # Vérification des résultats.
    for i in range(0, len(moved_tiles)):
        assert moved_tiles[i] == plateau['tiles'][i]

    print("Test de la fonction play_move: Ok")


# Lancement des tests concernant la fonction get_free_space (partie 2)
test_get_free_space()

# Lancement des tests concernant la fonction get_tile (partie 2)
test_get_tile()

# Lancement des tests concernant la fonction get_next_alea_tiles (partie 2)
test_get_next_alea_tiles()

# Lancement des tests concernant la fonction put_next_tiles (partie 2)
test_put_next_tiles()

# Lancement des tests concernant la fonction line_pack (partie 2)
test_line_pack()

# Lancement des tests concernant la fonction column_pack (partie 2)
test_column_pack()

# Lancement des tests concernant la fonction is_fusion_possible (partie 2)
test_is_fusion_possible()

# Lancement des tests concernant la fonction line_move (partie 2)
test_line_move()

# Lancement des tests concernant la fonction column_move (partie 2)
test_column_move()

# Lancement des tests concernant la fonction lines_move (partie 2)
test_lines_move()

# Lancement des tests concernant la fonction columns_move (partie 2)
test_columns_move()

# Lancement des tests concernant la fonction play_move (partie 2)
test_play_move()