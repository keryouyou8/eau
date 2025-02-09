"""
Ce script détermine si une chaîne de caractères ne contient que des chiffres.
- L'utilisateur doit fournir exactement un argument.
- En cas d'erreur dans les arguments, affiche une erreur et quitte le programme.
"""

import sys


# Fonctions utilisées
def is_only_digits(arg: list[str]) -> bool:
    """
    Vérifie si tous les caractères sont des chiffres.
    """
    for char in arg[0]:
        if not ("0" <= char <= "9"):
            return False
    return True


# Gestion d'erreur
def validate_arguments(args: list[str]) -> bool:
    """
    Vérifie les arguments pour l'exercice.
    """
    if len(args) !=1:
        print(f"error: Vous avez fourni {len(args)} argument(s). Il faut un unique argument !")
        return False
    return True


# Parsing
def get_arguments() -> list[str]:
    """
    Récupère les arguments passés en ligne de commande (exclut le nom du script).
    """
    return sys.argv[1:]


# Résolution
def solve_is_only_digits(args: list[str]) -> None:
    """
    Résout l'exercice en cours.
    """
    if not validate_arguments(args):
        sys.exit(1)
    result = is_only_digits(args)
    display_result(result)


# Affichage du résultat
def display_result(result: bool) -> None:
    """
    Affiche 'true' ou 'false' comme chaîne.
    """
    print("true" if result else "false")


# Exécution du programme
if __name__ == "__main__":
    args = get_arguments()
    solve_is_only_digits(args)
