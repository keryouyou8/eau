"""
        Par ordre Ascii :

Ce script trie une liste de caractère selon leur ordre dans la table ASCII.
- L'utilisateur doit fournir au moins deux arguments (nombres entiers).
- En cas d'erreur dans les arguments, le programme affiche 'error' et quitte.
"""

import sys


# Fonctions utilisées
def ascii_sort(strings: list[str]) -> list[str]:
    """
    Trie une liste de chaînes de caractères selon leur ordre dans la table ASCII.
    Utilise l'algorithme de tri par sélection :
    - Trouve la plus petite chaîne à chaque étape et la place au début de la partie non triée.
    """
    length = len(strings)

    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if strings[j] < strings[min_index]:
                min_index = j
        if min_index != i:
            strings[i], strings[min_index] = strings[min_index], strings[i]

    return strings


# Gestion d'erreur
def validate_arguments(args : list[str]) -> bool:
    """
    Vérifie que les arguments sont valides.
    """
    if len(args) < 2:
        print(f"error: Vous avez fourni {len(args)} argument(s). Il faut au moins deux arguments !")
        return False
    return True


# Parsing
def get_arguments() -> list[str]:
    """
    Récupère les arguments passés en ligne de commande (exclut le nom du script
    """
    return sys. argv[1:]


# Résolution
def solve_ascii_sort(args : list[str]) -> None:
    """
    Orchestre la résolution de l'exercice:
    - Valide les arguments.
    - Trie les chaînes de caractères selon leur ordre dans la table ASCII.
    - Affiche le résultat.
    """
    if not validate_arguments(args):
        sys.exit(1)
    result = ascii_sort(args)
    display_result(result)


# Affichage du résultat
def display_result(result : list[str]) -> None:
    """
    Affiche le résultat de l'exercice.
    """
    print(" ".join(result))


# Exécution du programme
if __name__ == "__main__":
    args = get_arguments()
    solve_ascii_sort(args)
