from random import randint

import os
import sys

my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(my_path + '/../')

from tiles.tiles_acces import is_room_empty, set_value

########################################################
###                    PARTIE 1                      ###
########################################################


# Fonction de la partie 1
def get_nb_empty_rooms(plateau):
    """
	Met à jour le dictionnaire plateau avec le nombre de case(s) libre(s) du plateau.

	:param plateau: Un dictionnaire correspondant à un plateau de jeu.

	:return: Un entier correspondant au nombre de cases libres du plateau.
	"""
    empty_rooms = 0

    for i in range(0, len(plateau['tiles'])):     # Boucle de calcul du nombre de cases vides.

        if plateau['tiles'][i] == 0:
            empty_rooms += 1

    plateau['nombre_cases_libres'] = empty_rooms  # Mise à jour de nombre de cases vides.

    return empty_rooms


########################################################
###                    PARTIE 2                      ###
########################################################


# Demander s'il faut vérifier ou non qu'il existe un espace libre.
# Si c'est le cas, penser à ajouter un commentaire dans la fonction de tests unitaires.

# Fonction de la partie 2
def get_free_space(plateau):
    """
    Retourne un tuple représentant une case vide aléatoire de la grille d'un plateau de jeu.

    :param plateau: Un dictionnaire correspondant à un plateau de jeu.

    :return: Deux entiers correspondant aux coordonnées d'une case vide (= dont la valeur vaut 0).
    """
    # La recherche de coordonnées doit se faire entre 0 et la taille du plateau - 1. Or, la recherche d'un nombre
    # aléatoire se fait entre deux bornes incluses c'est pour cela qu'on retire 1 à la borne supérieure.
    n = plateau['n'] - 1
    lig, col = randint(0, n), randint(0, n)

    while not is_room_empty(plateau, lig, col):  # Tant qu'une case vide n'a pas été trouvée, on en recherche une.
        lig, col = randint(0, n), randint(0, n)

    return lig, col


# Fonction de la partie 2
def get_tile(plateau, value):
    """
    Retourne une tuile sous la forme d'un dictionnaire. Les clés sont les suivantes:
    - val -> La valeur de la tuile.
    - lig -> La ligne où se situe la tuile.
    - col -> La colonne où se situe la tuile.
    Les valeurs lig et col sont définies aléatoirement.

    :param plateau: Un dictionnaire correspondant à un plateau de jeu.
    :param value: Un entier correspondant à la valeur de la tuile.

    :return: Une tuile sous la forme d'un dictionnaire.
    """
    lig, col = get_free_space(plateau)  # Récupération d'une case vide (ligne, colonne).
    return {'val': value, 'lig': lig, 'col': col}


# Fonction de la partie 2
def get_next_alea_tiles(plateau, mode):
    """
    Retourne un dictionnaire contenant une ou deux tuile(s) dont la position (lig, col) est tirée
    aléatoirement et correspond à un emplacement libre du tableau.

    Clés du dictionnaire:
    - mode -> Le mode de génération des tuiles (string).
    - check -> True si la partie est terminée, False sinon (booléen).
    - 0 et/ou 1 -> Les tuiles générées sous la forme d'un dictionnaire.

    :param plateau: Un dictionnaire correspondant à un plateau de jeu.
    :param mode: Une chaine de caractère correspondant au mode de génération des tuiles.

    Modes disponibles:
    - 'init' -> Un dictionnaire contenant deux tuiles de valeur 1 et 2 est retourné. Utilisé lors de l'initialisation du jeu.
    - 'encours' -> Un dictionnaire contenant une tuile de valeur comprise entre 1 et 3 est retourné. Utilisé en cours de jeu.

    Pour ces deux modes, les positions des tuiles sont tirées aléatoirement.

    :return: Un dictionnaire contenant les informations.
    """
    tiles = {"mode": mode}

    if mode == "init":
        tiles['0'] = get_tile(plateau, 1)
        tiles['1'] = get_tile(plateau, 2)
    elif mode == "encours":
        tiles['0'] = get_tile(plateau, randint(1, 3))

    tiles['check'] = get_nb_empty_rooms(plateau) - 1 != 0  # A vérifier
    return tiles


# Fonction de la partie 2
def put_next_tiles(plateau, tiles):
    """
    Permet de placer une ou deux tuiles dans un plateau de jeu.

    :param plateau: Un dictionnaire correspondant à un plateau de jeu.
    :param tiles: Un dictionnaire sous la forme de celui renvoyé par la fonction get_next_alea_tiles
    """
    # Quelque soit le mode spécifié, on a toujours au moins une tuile.
    # On peut donc l'ajouter dans tous les cas.
    set_value(plateau, tiles['0']['lig'], tiles['0']['col'], tiles['0']['val'])

    if tiles['mode'] == "init":  # Dans le cas du mode 'init', on doit ajouter une deuxième tuile.
        set_value(plateau, tiles['1']['lig'], tiles['1']['col'], tiles['1']['val'])


# Fonction de la partie 2
def line_pack(plateau, num_li, debut, sens):
    """
    Tasse les tuiles d'une ligne dans un sens donné.

    :param plateau: Un dictionnaire correspondant à un plateau de jeu.
    :param num_li: Un entier correspondant à l'indice de la ligne à tasser.
    :param debut: Un entier correspondant à l'indice à partir duquel se fait le tassement.
    :param sens: Un entier correspondant au sens du tassement: 1 vers la gauche, 0 vers la droite.
    """
    tiles = plateau['tiles']

    lig = num_li * plateau['n']  # Récupération de l'indice de la ligne dans la grille.
    i = debut  # Indice à partir duquel s'effectue le tassement dans la ligne.

    if sens == 1:
        # On part de 'debut' dans la ligne et on décale tous les autres éléments vers la gauche.
        while i < plateau['n'] - 1:
            tiles[lig + i] = tiles[lig + i + 1]  # L'élément courant prend la valeur de l'élément suivant (i + 1).
            i += 1

        set_value(plateau, num_li, 3, 0)  # Comme on décale vers la gauche, la dernière case de la ligne devient vide.

    elif sens == 0:
        # On part de 'debut' dans la ligne et on décale tous les autres éléments vers la droite.
        while i > 0:
            tiles[lig + i] = tiles[lig + i - 1]  # L'élément courant prend la valeur de l'élément précédent (i - 1).
            i -= 1

        set_value(plateau, num_li, 0, 0)  # Comment on décale vers la droite, la première case de la ligne devient vide.


# Fonction de la partie 2
def column_pack(plateau, num_col, debut, sens):
    """
    Tasse les tuiles d'une ligne dans un sens donné.

    :param plateau: Un dictionnaire correspondant à un plateau de jeu.
    :param num_col: Un entier correspondant à l'indice de la colonne à tasser.
    :param debut: Un entier correspondant à l'indice à partir duquel se fait le tassement.
    :param sens: Un entier correspondant au sens du tassement: 1 vers le haut, 0 vers le bas.
    """
    n = plateau['n']
    tiles = plateau['tiles']

    i = debut

    if sens == 1:
        # On part l'indice de la case de 'tassement' et on écrase la valeur courante par la suivante.
        # La valeur suivante correspond à la valeur de la colonne 'num_col' à la ligne suivante (i + n).
        # Le décalage se fait du bas vers le haut.
        while i < n - 1:
            tiles[i*n + num_col] = tiles[n*(i + 1) + num_col]
            i += 1  # Passage à la valeur de la colonne 'num_col' de la ligne suivante.

        set_value(plateau, 3, num_col, 0)  # Comme on décale vers le haut, la dernière case de la colonne devient vide.

    elif sens == 0:
        # On part de l'indice de la case de 'tassement' et on écrase la valeur courante par la précédente.
        # La valeur précédente correspond à la valeur de la colonne 'num_col' de la ligne précédente (i - n).
        # Le décalage se fait du haut vers le bas.
        while i > 0:
            tiles[i*n + num_col] = tiles[n*(i - 1) + num_col]
            i -= 1

        set_value(plateau, 0, num_col, 0)  # Comme on décale vers le bas, la première case de la colonne devient vide.


# Fonction de la partie 2
def is_fusion_possible(val1, val2):
    """
    Permet de savoir si deux valeurs peuvent fusionner en respectant les règles du jeu Threes.

    Rappel des règles de fusion:
    - Les tuiles de valeurs 1 et 2 ne peuvent fusionner qu'entre elles.
    - Une tuile dont la valeur est un multiple de 3 ne peut fusionner qu'avec une autre tuile de même valeur.

    :param val1: un entier correspondant à la première valeur à fusionner.
    :param val2: un entier correspondant à la seconde valeur à fusionner.
    :return: True si les deux valeurs peuvent fusionner, False sinon.
    """
    if val1 == 1 and val2 == 2:  # Fusion de tuiles de valeur 1 et 2.
        return True

    if val1 == 2 and val2 == 1:  # Fusion de tuiles de valeur 1 et 2.
        return True

    if val1 == val2 and val1 % 3 == 0 and val2 % 3 == 0:  # Fusion de deux tuiles de même valeur et multiples de 3.
        return True

    return False


# Fonction de la partie 2
def line_move(plateau, num_lig, sens):
    """
    Permet de déplacer les tuiles d'une ligne dans un sens donné en respectant les règles du jeu Threes.

    :param plateau: Un dictionnaire correspondant à un plateau de jeu.
    :param num_lig: Un entier correspondant à l'indice de la ligne où se fait le déplacement.
    :param sens: Un entier correspondant au sens du déplacement: 1 vers la gauche, 0 vers la droite.
    """
    n = plateau['n']
    tiles = plateau['tiles']

    lig = num_lig * n

    if sens == 1:  # Déplacement vers la gauche.

        i = 0
        while i < n - 1:  # Parcours de gauche à droite.

            if is_room_empty(plateau, num_lig, i):                        # Si présence d'une case vide

                line_pack(plateau, num_lig, i, sens)                      # Tassement vers la gauche.
                i = n                                                     # Sortie de la boucle.

            elif is_fusion_possible(tiles[lig + i], tiles[lig + i + 1]):  # Si une fusion est possible entre l'élément courant et l'élément suivant.

                tiles[lig + i] += tiles[lig + i + 1]                      # élément courant += élément suivant
                line_pack(plateau, num_lig, i + 1, sens)                  # Tassement vers la gauche en réponse à la fusion.

                i = n                                                     # Sortie de la boucle.

            else:
                i += 1                                                    # Itération suivante.

    elif sens == 0:  # Déplacement vers la droite.

        i = n - 1
        while i > 0:  # Parcours de droite à gauche.

            if is_room_empty(plateau, num_lig, i):                        # Si présence d'une case vide

                line_pack(plateau, num_lig, i, sens)                      # Tassement vers la droite.
                i = 0                                                     # Sortie de la boucle.

            elif is_fusion_possible(tiles[lig + i], tiles[lig + i - 1]):  # Si une fusion est possible entre l'élément courant et l'élément précédent.

                tiles[lig + i] += tiles[lig + i - 1]                      # élément courant += élément précédent
                line_pack(plateau, num_lig, i - 1, sens)                  # Tassement vers la droite en réponse à la fusion.

                i = 0                                                     # Sortie de la boucle.

            else:
                i -= 1                                                    # Itération suivante.


# Fonction de la partie 2
def column_move(plateau, num_col, sens):
    """
    Permet de déplacer les tuiles d'une colonne dans un sens donné en respectant les règles du jeu Threes.

    :param plateau: Un dictionnaire correspondant à un plateau de jeu.
    :param num_col: Un entier correspondant à l'indice de la colonne où se fait le déplacement.
    :param sens: Un entier correspondant au sens du déplacement: 1 vers le haut, 0 vers le bas.
    """
    n = plateau['n']
    tiles = plateau['tiles']

    if sens == 1:  # Déplacement vers le haut.

        i = 0
        while i < n - 1:  # Parcours de gauche à droite.

            if is_room_empty(plateau, i, num_col):                                      # Si présence d'une case vide

                column_pack(plateau, num_col, i, sens)                                  # Tassement vers le haut.
                i = n                                                                   # Sortie de la boucle.

            elif is_fusion_possible(tiles[i*n + num_col], tiles[n*(i + 1) + num_col]):  # Si une fusion est possible entre l'élément courant et l'élément suivant.

                tiles[i*n + num_col] += tiles[n*(i + 1) + num_col]                      # élément courant += élément suivant
                column_pack(plateau, num_col, i + 1, sens)                              # Tassement vers le haut en réponse à la fusion.

                i = n                                                                   # Sortie de la boucle.

            else:
                i += 1                                                                  # Itération suivante.

    elif sens == 0:  # Déplacement vers le bas.

        i = n - 1
        while i > 0:  # Parcours de droite à gauche.

            if is_room_empty(plateau, i, num_col):                                      # Si présence d'une case vide

                column_pack(plateau, num_col, i, sens)                                  # Tassement vers le bas.
                i = 0                                                                   # Sortie de la boucle.

            elif is_fusion_possible(tiles[i*n + num_col], tiles[n*(i - 1) + num_col]):  # Si une fusion est possible entre l'élément courant et l'élément précédent.

                tiles[i*n + num_col] += tiles[n*(i - 1) + num_col]                      # élément courant += élément précédent
                column_pack(plateau, num_col, i - 1, sens)                              # Tassement vers le bas en réponse à la fusion.

                i = 0                                                                   # Sortie de la boucle.

            else:
                i -= 1                                                                  # Itération suivante.


# Fonction de la partie 2
def lines_move(plateau, sens):
    """
    Permet de déplacer les tuiles de toutes les lignes du plateau dans le sens spécifié et en appliquant les règles du jeu Threes.

    :param plateau: Un dictionnaire correspondant à un plateau de jeu.
    :param sens: Un entier correspondant au sens du déplacement: 1 vers la gauche, 0 vers la droite.
    """
    for num_lig in range(0, plateau['n']):  # On prend toutes les lignes et on les bouge dans le sens donné.
        line_move(plateau, num_lig, sens)


# Fonction de la partie 2
def columns_move(plateau, sens):
    """
    Permet de déplacer les tuiles de toutes les colonnes du plateau dans le sens spécifié et en appliquant les règles du jeu Threes.

    :param plateau: Un dictionnaire correspondant à un plateau de jeu.
    :param sens: Un entier correspondant au sens du déplacement: 1 vers le haut, 0 vers le bas.
    """
    for num_col in range(0, plateau['n']):  # On prend toutes les colonnes et on les bouge dans le sens donné.
        column_move(plateau, num_col, sens)


# Demander s'il faut vérifier ou non que le sens est correct et corriger le dernier elif dans ce cas.

# Fonction de la partie 2
def play_move(plateau, sens):
    """
    Déplace les tuiles du plateau dans un sens donné en appliquant les règles du jeu Threes.

    Sens possibles:
    - 'b': bas
    - 'h': haut
    - 'd': droite
    - 'g': gauche

    :param plateau: Un dictionnaire correspondant à un plateau de jeu.
    :param sens: Un caractère correspondant au sens de déplacement.
    """
    if sens == 'b':
        columns_move(plateau, 0)  # Mouvement vers le bas
    elif sens == 'h':
        columns_move(plateau, 1)  # Mouvement vers le haut
    elif sens == 'd':
        lines_move(plateau, 0)    # Mouvement vers la droite
    elif sens == 'g':
        lines_move(plateau, 1)    # Mouvement vers la gauche

