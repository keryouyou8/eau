"""
Ce script affiche la plus petite différence entre deux nombres consécutifs dans une liste d'arguments passés par l'utilisateur.
- L'utilisateur doit fournir au moins deux arguments (nombres entiers).
- En cas d'erreur dans les arguments, il affiche error et quitte le programme.
"""

import sys


# Fonctions utilisées
def smallest_difference(numbers: list[int]) -> int:
    """
    Retourne la plus petite différence entre deux nombres consécutifs.
    """
    min_diff = numbers[1] - numbers[0]
    if min_diff < 0:
        min_diff = -min_diff
        
    for i in range(1,len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < 0:
            diff = -diff
        if diff < min_diff:
            min_diff = diff

    return min_diff

# Gestion d'erreur
def is_digit(arg: str) -> bool:
    """
    Vérifie si une chaîne représente un nombre entier valide.
    """
    if arg[0] == "-":
        arg = arg[1:]
    if not arg:
        return False
    for char in arg:
        if not ("0" <= char <= "9"):
            return False
    return True

def validate_arguments(args: list[str]) -> bool:
    """
    Vérifie les arguments pour l'exercice.
    """
    if len(args) < 2:
        print(f"error: Vous avez fourni {len(args)} argument(s). Il faut au moins deux arguments !")
        return False
    for arg in args:
        if not is_digit(arg):
            print(f"error: L'argument '{arg}', doit être un nombre entier.")
            return False
    return True

# Parsing
def get_arguments() -> list[str]:
    """
    Récupère les arguments passés en ligne de commande (exclut le nom du script).
    """
    return sys.argv[1:]

def convert_arguments(args: list[str]) -> list[int]:
    """
    Convertit une liste d'arguments en liste d'entiers.
    """
    return [int(arg) for arg in args]


# Résolution
def solve_smallest_difference(args: list[str]) -> None:
    """
    Orchestre la résolution de l'exercice:
    - Valide les arguments.
    - Cherche la plus petite différence entre deux nombres consécutifs.
    - Affiche le résultat.
    """
    if not validate_arguments(args):
        sys.exit(1)
    numbers = convert_arguments(args)
    result = smallest_difference(numbers)
    display_result(result)

# Affichage du résultat
def display_result(result: int) -> None:
    """
    Affiche la plus petite différence entre deux nombres consécutifs.
    """
    print(result)

# Exécution du programme
if __name__ == "__main__":
    args = get_arguments()
    solve_smallest_difference(args)