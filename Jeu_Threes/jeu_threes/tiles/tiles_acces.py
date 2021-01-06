# Fonction de la partie 1
def check_indice(plateau, indice):
    """
	Permet de vérifier si un indice correspond à un indice valide de case pour le plateau.

	:param plateau: Un dictionnaire correspondant à un plateau de jeu.
	:param indice: Un entier correspondant à l'indice à tester.

	:return: True si l'indice est compris entre 0 et n-1 où n correspond à la valeur associée à la clé 'n' dans le plateau et False sinon.
	"""
    return 0 <= indice and indice < plateau['n']


# Fonction de la partie 1
def check_room(plateau, lig, col):
    """
	Permet de vérifier si les coordonnées (lig, col) correspondent à une case du plateau.

	:param plateau: Un dictionnaire correspondant à un plateau de jeu.
	:param lig: Un entier correspondant au numéro de la ligne.
	:param col: Un entier correspondant au numéro de la colonne.

	:return: True si lig et col sont des indices valides et False sinon.
	"""
    return check_indice(plateau, lig) and check_indice(plateau, col)


# Fonction de la partie 1
def get_value(plateau, lig, col):
    """
	Permet de récupérer, dans un plateau, la valeur de la case de coordonnées (lig, col).
	Cette fonction renvoie une erreur si les coordonnées de la case sont invalides.

	:param plateau: Un dictionnaire correspondant à un plateau de jeu.
	:param lig: Un entier correspondant au numéro de la ligne.
	:param col: Un entier correspondant au numéro de la colonne.

	:return: Un entier correspondant à la valeur de la case à la position (lig, col).
	"""
    assert check_room(plateau, lig, col), "Erreur: les coordonnées de la tuile sont invalides."

    indice = (plateau['n'] * lig) + col   # Calcul de l'indice à partir de lig et col.

    return plateau['tiles'][indice]


# Fonction de la partie 1
def set_value(plateau, lig, col, val):
    """
	Affecte la valeur 'val' dans la case de coordonnées (lig, col) du plateau et met à jour le nombre de cases libres.
	Cette fonction renvoie une erreur si les coordonnées de la case sont invalides.

	:param plateau: Un dictionnaire correspondant à un plateau de jeu.
	:param lig: Un entier correspondant au numéro de la ligne.
	:param col: Un entier correspondant au numéro de la colonne.
	:param val: Un entier correspondant à la valeur à affecter.
	"""
    assert check_room(plateau, lig, col), "Erreur: les coordonnées de la tuile sont invalides."
    assert val >= 0, "Erreur, la valeur à affecter doit être supérieure ou égale à 0."

    tiles = plateau['tiles']

    indice = (plateau['n'] * lig) + col  # Calcul de l'indice à partir de lig et col.

    if val == 0 and tiles[indice] != 0:  # Si la case devient vide après l'affectation et qu'elle ne l'était pas avant.
        plateau["nombre_cases_libres"] += 1  # On augmente de 1 le nombre de cases vides.

    elif val != 0 and tiles[indice] == 0:  # Si la case était vide et qu'elle ne le sera plus suite à l'affectation.
        plateau["nombre_cases_libres"] -= 1  # On diminue de 1 le nombre de cases vides.

    tiles[indice] = val


# Fonction de la partie 1
def is_room_empty(plateau, lig, col):
    """
	Permet de vérifier si une case du tableau est libre ou non.
	Cette fonction renvoie une erreur si les coordonnées de la case sont invalides.

	:param plateau: Un dictionnaire correspondant à un plateau de jeu.
	:param lig: Un entier correspondant au numéro de la ligne.
	:param col: Un entier correspondant au numéro de la colonne.

	:return: True si la case est libre, False sinon.
	"""
    assert check_room(plateau, lig, col), "Erreur: les coordonnées de la tuile sont invalides."

    return get_value(plateau, lig, col) == 0  # Vérification que la valeur de la tuile vaut 0. Si c'est le cas, la case est vide.
