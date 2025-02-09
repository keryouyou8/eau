"""
Ce script affiche les arguments passés en ligne de commande dans l'ordre inverse, un par ligne.
- En cas d'absence d'arguments ou d'erreur, il retourne 'error'.
"""

import sys


# Utilitaire pour aider à resoudre
def reverse_list(args: list[str]) -> list[str]:
    """
    Inverse l'ordre des éléments d'une liste.
    """
    reversed_args = []
    for i in range(len(args) -1, -1, -1):
        reversed_args.append(args[i])
    return reversed_args


# Gestion d'erreur
def validate_arguments(args: list[str]) -> bool:
    """
    Vérifie que le nombre d'arguments est suffisant.
    """
    if len(args) < 2:
        print(f"error: Vous avez fourni {len(args)} argument(s). Il faut au minimum deux arguments.")
        return False
    return True


# Parsing
def get_arguments() -> list[str]:
    """
    Extrait les arguments passés en ligne de commande (en excluant le nom du script).
    """
    return sys.argv[1:]


# Résolution
def solve_reversed_list(args: list[str]) -> None:
    """
    Orchestre la résolution du programme :
    - Valide les arguments.
    - Inverse les arguments.
    - Affiche les arguments inversés.
    """
    if not validate_arguments(args):
        return
    reversed_args = reverse_list(args)
    display_arguments(reversed_args)


# Affichage du résultat
def display_arguments(args: list[str]) -> None:
    """
    Affiche les éléments d'une liste, un par ligne.
    """
    for arg in args:
        print(arg)


# Exécution du programme
if __name__ == "__main__": # Pour éviter que tout le fichier s'exécute si on l'importe
    args = get_arguments()
    solve_reversed_list(args)