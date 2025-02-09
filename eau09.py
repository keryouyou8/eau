"""
        Entre min et max :

Ce script affiche toutes les valeurs comprises entre deux nombres dans l’ordre croissant. Min inclus, max exclus.
- L'utilisateur doit fournir exactement deux arguments (nombres entiers).
- En cas d'erreur dans les arguments, affiche une erreur et quitte le programme.
"""

import sys


# Fonctions utilisées
def between_numbers(args: list[str]) -> str:
    """
    Retourne toutes les valeurs comprises entre deux nombres dans l'ordre croissant.
    """
    first_number = int(args[0])
    second_number = int(args[1])
    if first_number > second_number:
        min_number, max_number = second_number, first_number
    else:
        min_number, max_number = first_number, second_number

    numbers = []
    for i in range (min_number, max_number):
        numbers.append(str(i))
    return numbers
    
# Gestion d'erreur
def is_digit(arg) -> bool:
    """
    Vérifie si un caractère est un chiffre.
    """
    if arg[0] == "-":
        arg = arg[1:]
    if not arg:
        return False
    for char in arg:
        if not ("0" <= char <= "9"):
            return False
    return True

def validate_arguments(args):
    """
    Verifie les arguments pour l'exercice.
    """
    if len(args) != 2:
        print(f"error: Vous avez fourni {len(args)} argument(s). Il faut exactement deux arguments !")
        sys.exit(1)
    if not is_digit(args[0]):
        print(f"error: L'argument en premier '{args[0]}', doit être un nombre entier.")
        sys.exit(1)
    if not is_digit(args[1]):
        print(f"error: L'argument en deuxième '{args[1]}', doit être un nombre entier.")
        sys.exit(1)
    return True


# Parsing
def get_arguments():
    """
    Récupère les arguments passés en ligne de commande (exclut le nom du script).
    """
    return sys.argv[1:]


# Résolution
def solve_between_numbers(args):
    """
    Orchestre la résolution de l'exercice:
    - Valide les arguments.
    - Retourne toutes les valeurs comprises entre deux nombres dans l'ordre croissant.
    - Affiche le résultat.
    """
    if not validate_arguments(args):
        sys.exit(1)
    result = between_numbers(args)
    display_result(result)


# Affichage du résultat
def display_result(result):
    """
    Affiche le résultat.
    """
    print(" ".join(result))


# Exécution du programme
if __name__ == "__main__":
    args = get_arguments()
    solve_between_numbers(args)