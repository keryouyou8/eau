"""
        Prochain nombre premier :

Ce script affiche le premier nombre premier strictement supérieur au nombre donné en argument.
- L'utilisateur doit fournir un unique argument, entier positif (N >= 0).
- En cas d'erreur dans les arguments, le script retourne -1.
"""

import sys


# Fonctions utilisées
def is_prime(number: int) -> bool:
    """
    Vérifie si un nombre donné est premier.
    """
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def find_next_prime(number:int) -> int:
    """
    Trouve le premier nombre premier strictement supérieur au nombre donné.
    """
    number += 1
    while not is_prime(number):
        number += 1
    return number


# Gestion d'erreur
def is_positive_integer(string: str) -> bool:
    """
    Vérifie si une chaîne représente un entier positif.
    """
    if not string:
        return False
    for char in string:
        if not ("0" <= char <= "9"):
            return False
    return True


def validate_arguments(args: list[str]) -> bool:
    """
    Valide les arguments pour l'exercice.
    """
    if len(args) != 1:
        print(f"error: Vous avez fourni {len(args)} argument(s). Il faut un unique argument.")
        return False
    if not is_positive_integer(args[0]):
        print(f"error: L'argument '{args[0]}' n'est pas valide. Il doit s'agir d'un entier positif (N=0,1,2,3,…).")
        return False
    return True


# Parsing
def get_arguments() -> list[str]:
    """
    Récupère les arguments passés en ligne de commande.
    """
    return sys.argv[1:]
    

# Résolution
def solve_next_prime(args: list[str]) -> None:
    """
    Orchestre la résolution de l'exercice :
    - Valide l'argument (doit être un entier positif).
    - Recherche le premier nombre premier strictement supérieur à l'argument donné.
    - Affiche le résultat ou -1 en cas d'erreur.
    """

    if not validate_arguments(args):
        display_result(-1)
        sys.exit(1)
    number = int(args[0])
    next_prime = find_next_prime(number)
    display_result(next_prime)


# Affichage du résultat
def display_result(next_prime: int) -> None:
    """
    Affiche le résultat final.
    """
    print(next_prime)


# Exécution du programme
if __name__ == "__main__":
    args = get_arguments()
    solve_next_prime(args)