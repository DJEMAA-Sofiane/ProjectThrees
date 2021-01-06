import os
import sys

my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(my_path + '/../')

from tiles.tiles_acces import get_value
from termcolor import colored


# Fonction de la partie 1
def simple_display(plateau):
    """
    Affichage simple, sans formatage, de la grille du plateau passé en paramètre.
    Les valeurs sont alignées et affichées en colonne.

    :param plateau: Un dictionnaire correspondant à un plateau de jeu.
    """
    display = ""
    n = plateau['n']

    for row in range(0, n):

        for column in range(0, n):
            display += str(get_value(plateau, row, column)).rjust(4)  # Ajout de la tuile courante avec un espacement
                                                                      # supplémentaire (rjust) pour l'alignement.
        display += "\n"

    print(display)


def full_display(plateau):

    n = plateau['n']
    background = colored('  ', "grey", "on_grey")
    chars_per_line = 9 * n + 2

    for row in range(0, n):

        space_line, number_line = background, background  # Initialisation a 'background' (gris).

        for column in range(0, n):  # Construction des lignes contenant les tuiles.

            value = get_value(plateau, row, column)

            if value == 0 or value == 1:

                space_line += colored(' ' * 7, "blue", "on_blue")
                number_line += colored(str(value).rjust(4) + ' '.rjust(3), "grey", "on_blue")

            elif value == 2:

                space_line += colored(' ' * 7, "red", "on_red")
                number_line += colored(str(value).rjust(4) + ' '.rjust(3), "grey", "on_red")

            else:
                space_line += colored(' ' * 7, "white", "on_white")
                number_line += colored(str(value).rjust(4) + ' '.rjust(3), "grey", "on_white")

            space_line += background
            number_line += background

        print(colored(' ' * chars_per_line, "grey", "on_grey"))

        for i in range(0, 3):  # Assemblage des lignes créées.
            print(space_line if i != 1 else number_line)

    print(colored(' ' * chars_per_line, "grey", "on_grey"))  # Ajout de la ligne de background manquante.

