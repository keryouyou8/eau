"""
Ce script affiche l’index de la première occurrence d’un élément recherché dans un tableau constitué des arguments passés en ligne de commande, à l’exception du dernier.
- Si l’élément n’est pas trouvé, il affiche -1.
- En cas d'erreur dans les arguments, il affiche error et quitte le programme.
"""

import sys


# Fonctions utilisées
def find_index(args: list[str]) -> int:
    """
    Retourne l'index de la première occurrence de l'élément recherché.
    """
    target = args[-1]
    for i in range(len(args) - 1):
        if args[i] == target:
            return i
    return -1


# Gestion d'erreur
def validate_arguments(args : list[str]) -> bool:
    """
    Vérifie qu'il y a au moins deux arguments.
    """
    if len(args) < 2:
        print(f"error: Vous avez fourni {len(args)} argument(s). Il faut au moins deux arguments !")
        return False
    return True

# Parsing
def get_arguments() -> list[str]:
    """
    Récupère les arguments passés en ligne de commande (exclut le nom du script).
    """
    return sys.argv[1:]


# Résolution
def solve_find_index(args: list[str]) -> None:
    """
    Orchestre la résolution de l'exercice:
    - Valide les arguments.
    - Cherche l'index de l'élément recherché.
    - Affiche le résultat.
    """
    if not validate_arguments(args):
        sys.exit(1)
    result = find_index(args)
    display_result(result)

# Affichage du résultat
def display_result(result: int) -> None:
    """
    Affiche l'index de l'élément recherché.
    """
    print(result)


# Exécution du programme
if __name__ == "__main__":
    args = get_arguments()
    solve_find_index(args)