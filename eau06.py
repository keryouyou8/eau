"""
Ce script permet de retourner une chaîne de caractère avec une alternance de majuscules et minuscules.
- L'utilisateur doit fournir exactement un argument (chaîne de caractère).
- En cas d'erreur dans les arguments, affiche une erreur et quitte le programme.
"""

import sys


# Fonctions utilisées
def alternate_case(args: list[str]) -> str:
    """
    Retourne une chaîne de caractère avec une alternance de majuscules et minuscules.
    """
    result_string = ""
    alternate_index = 0
    for char in args[0]:
        if ("A" <= char <= "Z") or ("a" <= char <= "z"):
            alternate_index += 1
            if alternate_index % 2 == 0:
                result_string += char.lower()
            else:
                result_string += char.upper()
        else:
            result_string += char
    return result_string

# Gestion d'erreur
def is_digit(arg: str) -> bool:
    """
    Vérifie si un caractère est un chiffre.
    """
    for char in arg:
        if not ("0" <= char <= "9"):
            return False
    return True

def validate_arguments(args: list[str]) -> bool:
    """
    Verifie les arguments pour l'exercice.
    """
    if len(args) != 1:
        print(f"error: Vous avez fourni {len(args)} argument(s). Il faut un unique arguments, sous forme de chaîne de caractère !")
        return False
    if is_digit(args[0]):
        print(f"error: L'argument '{args[0]}' est uniquement composé de chiffres. Il doit contenir des lettres.")
        return False
    return True

# Parsing
def get_arguments() -> list[str]:
    """
    Récupère les arguments passés en ligne de commande (exclut le nom du script).
    """
    return sys.argv[1:]
    

# Résolution
def solve_alternate_case(args: list[str]) -> None:
    """
    Orchestre la résolution de l'exercice :
    - Valide les arguments passés.
    - Applique l’alternance majuscule/minuscule aux lettres de la chaîne.
    - Affiche le résultat transformé ou un message d'erreur en cas de problème.
    """
    if not validate_arguments(args):
        sys.exit(1)
    result = alternate_case(args)
    display_result(result)


# Affichage du résultat
def display_result(result: str) -> None:
    """
    Affiche le résultat de l'exercice.
    """
    print(result)


# Exécution du programme
if __name__ == "__main__":
    args = get_arguments()
    solve_alternate_case(args)

