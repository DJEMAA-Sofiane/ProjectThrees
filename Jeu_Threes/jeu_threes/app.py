from game.play import create_new_play
from life_cycle.play import restore_game, save_game, cycle_play
from ui.user_entries import get_user_menu

None
def threes():
    """
    Permet de d'enchaîner les parties du jeu Threes. Comprend aussi les interactions avec le menu
    (sauvegarde/restauration/création/reprise d'une partie ou quitter le jeu).
    """
    user_menu = get_user_menu(None)        # Affichage du menu et saisie d'un choix utilisateur.
    partie = menu_action(None, user_menu)  # Exécution du choix utilisateur.

    while user_menu != 'Q':                # Tant que le joueur ne veut pas quitter le jeu, on continue le cycle de jeu.

        game_finished = cycle_play(partie)

        if game_finished:                        # Si game_finished == True, la partie est terminée. Affichage du score + retour au menu.
            print("Partie terminée ! Votre score est:", partie['score'])
            user_menu = get_user_menu(None)
        else:                                    # game_finished == False, menu demandé. Mise en pause et affichage.
            user_menu = get_user_menu(partie)

        partie = menu_action(partie, user_menu)  # Actualisation de la partie avec le choix utilisateur.


def menu_action(partie, user_menu):
    """
    Permet de gérer les actions du joueur dans le menu.

    :param partie: Une partie de jeu en cours (voir game/play/create_new_play) ou None sinon.
    :param user_menu:n Un caractère correspondant au choix du joueur dans le menu.

    :return: La partie passée en argument (choix 'S', 'C' et 'Q') ou une partie restaurée (choix 'L')
             ou une nouvelle partie (choix 'N').
    """
    if user_menu == 'L':                                 # Le joueur veut restaurer une partie.
        print("\nPartie restorée. C'est parti !\n")
        partie = restore_game()
    elif user_menu == 'N':                               # Le joueur veut créer une nouvelle partie.
        print("\nCréation d'une nouvelle partie. C'est parti !\n")
        partie = create_new_play()
    elif user_menu == 'S':                               # Le joueur veut sauvegarder la partie en cours.
        print("\nPartie sauvegardée !\n")
        save_game(partie)
    elif user_menu == 'C':                               # Le joueur veut reprendre la partie en cours.
        print("\nReprise de la partie en cours.\n")
    else:                                                # Le joueur veut quitter le jeu.
        print("\nA bientôt sur le jeu Threes !\n")

    return partie


threes()
