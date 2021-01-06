import os
import sys

my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(my_path + '/../')

from game.play import create_new_play
from life_cycle.cycle_game import is_game_over, get_score

from tiles.tiles_acces import is_room_empty
from tiles.tiles_moves import get_free_space, get_next_alea_tiles, put_next_tiles, play_move

from ui.play_display import full_display
from ui.user_entries import get_user_move

from json import dump, loads


# Fonction de la partie 3
def cycle_play(partie):
    """
    Permet de jouer au jeu Threes.

    Séquencement des actions de cette fonction:
    1 - Affichage du plateau de jeu
    2 - Affichage de la valeur de la tuile suivante
    3 - Saisie du mouvemement proposé par le joueur ; deux cas possibles:
        * jouer le coup du joueur courant, mettre à jour le score et revenir au point 1.
        * retourner False si le menu est demandé.
    4 - Retourne True si la partie est terminée.

    :param partie: Une partie de jeu en cours (voir game/play/create_new_play) ou None sinon.
    :return: True si la partie est terminée, False si le menu est demandé.
    """
    assert not partie is None, "Erreur: Aucune partie n'est en cours."     # Vérification qu'une partie est en cours.

    plateau = partie['plateau']

    while not is_game_over(plateau):

        full_display(plateau)                                              # Affichage du plateau de jeu.

        if len(partie['next_tile']) == 0:                                  # Vérification qu'une tuile n'est pas déjà stockée.
            partie['next_tile'] = get_next_alea_tiles(plateau, "encours")  # Dans ce cas, on tire une nouvelle tuile et on la stocke dans la partie.

        next_tile = partie['next_tile']['0']

        print("La valeur de la tuile suivante est:", next_tile['val'])     # Affichage de la valeur de la tuile.

        move = get_user_move()                                             # Récupération du mouvement du joueur.

        if move != 'm':                                                    # Vérification que le joueur ne demande pas le menu principal.

            play_move(plateau, move)

            if not is_room_empty(plateau, next_tile['lig'], next_tile['col']):       # Si les coordonnées de la prochaine tuile sont déjà prises
                next_tile['lig'], next_tile['col'] = get_free_space(plateau)         # suite au mouvement, on les redéfinit.

            put_next_tiles(plateau, partie['next_tile'])                             # Ajout de la tuile suivante.

            partie['next_tile'] = {}                                       # Réinitialisation de la tuile stockée pour permettre un nouveau tirage.
            partie['score'] = get_score(plateau)                           # Mise à jour du score.
        else:
            return False

    return True


# Fonction de la partie 3
def save_game(partie):
    """
    Permet de sauvegarder une partie dans le fichier 'game_saved.json'.

    :param partie: Une partie de jeu en cours (voir game/play/create_new_play) ou None sinon.
    """
    file = open("game_saved.json", 'w')

    dump(partie, file)  # Ecriture de la partie dans le fichier json.

    file.close()


# Fonction de la partie 3
def restore_game():
    """
    Restaure et retourne un partie sauvegardée dans le fichier 'game_saved.json'.
    Si aucune partie n'est enregistrée, une nouvelle partie est retournée.

    :return: Une partie de jeu (voir game/play/create_new_play).
    """
    file = open("game_saved.json", 'r')

    json_text = file.read()

    partie = create_new_play() if json_text == "" else loads(json_text)  # Chargement de la partie sauvegardée ou création d'une nouvelle.

    file.close()

    return partie
