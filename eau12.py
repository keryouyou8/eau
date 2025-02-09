"""
        Tri à bulle :

Ce script trie une liste de nombres à l'aide de l'algorithme du tri à bulle.
- L'utilisateur doit fournir au moins deux arguments (nombres entiers).
- En cas d'erreur dans les arguments, le programme affiche 'error' et quitte.
"""

import sys


# Fonctions utilisées
def bubble_sort(numbers: list[int]) -> list[int]:
    """
    Trie une liste de nombres avec l'algorithme du tri à bulle.
    """
    length = len(numbers)

    for i in range(length - 1):
        swapped = False
        for j in range(length - i - 1):
            if numbers[j + 1] < numbers[j]:
                numbers[j + 1], numbers[j] = numbers[j], numbers[j + 1]
                swapped = True
        if not swapped:
            break

    return numbers


# Gestion d'erreur
def is_digit(arg : str) -> bool:
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

def validate_arguments(args : list[str]) -> bool:
    """
    Vérifie que les arguments sont valides.
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
    Récupère les arguments passés en ligne de commande (exclut le nom du script
    """
    return sys. argv[1:]

def convert_arguments(args : list[str]) -> list[int]:
    """
    Convertit une liste d'arguments en liste d'entiers.
    """
    return [int(arg) for arg in args]

# Résolution
def solve_bubble_sort(args : list[str]) -> None:
    """
    Orchestre la résolution de l'exercice :
    - Valide les arguments.
    - Applique le tri à bulle sur la liste d’entiers.
    - Affiche le résultat.
    """
    if not validate_arguments(args):
        sys.exit(1)
    numbers = convert_arguments(args)
    result = bubble_sort(numbers)
    display_result(result)


# Affichage du résultat
def display_result(result : list[int]) -> None:
    """
    Affiche le résultat de l'exercice.
    """
    print(" ".join(str(number) for number in result))


# Exécution du programme
if __name__ == "__main__":
    args = get_arguments()
    solve_bubble_sort(args)