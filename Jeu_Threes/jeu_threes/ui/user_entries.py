# Fonction de la partie 3
def get_user_move():
    """
    Saisit et retourne le coup joué par le joueur parmi les choix suivants:
    - 'h': haut
    - 'b': bas
    - 'd': droite
    - 'g': gauche
    - 'm': menu principal
    Les majuscules sont autorisées mais le coup sera retourné en minuscule.

    :return: Un caractère correspondant au coup saisi (en minuscule).
    """
    moves = ['h', 'b', 'd', 'g', 'm']

    # Début de la construction du message.
    message = "Saisissez un des coups suivants:"
    message += "\n'h' pour 'Haut'"
    message += "\n'b' pour 'Bas'"
    message += "\n'd' pour 'Droite'"
    message += "\n'g' pour 'Gauche'"
    message += "\n'm' pour 'Menu principal'"
    message += "\nNote: La saisie des coups en majuscule est autorisée."
    # Fin de la construction du message.

    print(message)
    move = input().lower()
    while not move in moves:  # Tant que le choix de l'utilisateur n'est pas un choix valide, on refait une saisie.
        print(message)
        move = input().lower()

    print("Coup saisi: '" + move + "'")
    return move


# On pouvait aussi faire cette fonction à l'aide d'un dictionnaire (clé = choix, valeur = description)
# mais pour un coût en temps plus important.

# Fonction de la partie 3
def get_user_menu(partie):
    """
    Saisit et retourne le choix du joueur dans le menu principal parmi les choix suivants:
    - 'N' : Commencer une nouvelle partie
    - 'L' : Charger une partie
    - 'S' : Sauvegarder la partie en cours
    - 'C' : Reprendre la partie en cours
    - 'Q' : Teminer le jeu

    :param partie: Une partie de jeu en cours (voir game/play/create_new_play) ou None sinon.
    :return: Un caractère correspondant au choix du joueur (en majuscule).
    """
    possible_choices = ['N', 'L', 'Q']

    # Début de la construction du menu.
    user_menu = "\nMenu principal:\n"
    user_menu += "\n'N' : Commencer une nouvelle partie"
    user_menu += "\n'L' : Charger une partie"

    if partie is not None:

        possible_choices.append('S')
        possible_choices.append('C')

        user_menu += "\n'S' : Sauvegarder la partie en cours"
        user_menu += "\n'C' : Reprendre la partie en cours"

    user_menu += "\n'Q' : Teminer le jeu"
    # Fin de la construction du menu.

    print(user_menu)

    user_choice = input().upper()
    while not user_choice in possible_choices:  # Tant que le choix de l'utilisateur n'est pas un choix valide, on refait une saisie.

        print(user_menu)
        user_choice = input().upper()

    return user_choice
