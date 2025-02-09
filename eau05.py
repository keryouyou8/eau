"""
Ce script détermine si une chaîne de caractère se trouve dans une autre.
- L'utilisateur doit fournir exactement deux arguments (chaînes de caractères).
- Affiche 'true' si la deuxième chaîne est contenue dans la première, 'false' sinon.
- En cas d'erreur dans les arguments, affiche une erreur et quitte le programme.
"""

import sys


# Fonctions utilisées
def contains_substring(args: list[str]) -> bool:
    """
    Vérifie si une chaîne est contenue dans une autre.
    """
    main_string = args[0]
    substring = args[1]
    if len(main_string) < len(substring):
        return False
    for i in range(len(main_string) - len(substring) + 1):
        if main_string[i:i+len(substring)] == substring:
            return True
    return False


# Gestion d'erreur
def validate_arguments(args: list[str]) -> bool:
    """
    Verifie les arguments pour l'exercice.
    """
    if len(args) != 2:
        print(f"error: Vous avez fourni {len(args)} argument(s). Il faut exactement deux arguments !")
        return False
    return True


# Parsing
def get_arguments() -> list[str]:
    """
    Récupère les arguments passés en ligne de commande (exclut le nom du script).
    """
    return sys.argv[1:]


# Résolution
def solve_contains_substring(args: list[str]) -> None:
    """
    Orchestre la résolution de l'exercice:
    - Valide les arguments.
    - Verifie que la sous chaîne existe dans la chaîne principale.
    - Affiche le résultat.
    """
    if not validate_arguments(args):
        sys.exit(1)
    result = contains_substring(args)
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
    solve_contains_substring(args)
