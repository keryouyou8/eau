"""
        Majuscule :

Ce script permet de retourner une chaîne de caractère avec une  majuscule en première lettre de chaque mot et le reste en minuscule.
- L'utilisateur doit fournir exactement un argument (chaîne de caractère).
- En cas d'erreur dans les arguments, affiche une erreur et quitte le programme.
"""

import sys


# Fonctions utilisées
def capitalize_words(args: list[str]) -> str:
    """
    Retourne une chaîne de caractère avec une majuscule en première lettre de chaque mot et le reste en minuscule.
    """
    result_string = []
    word = ""
    for char in args[0]:
        if char in [" ", "\t", "\n"]:
            if word:
                word = word[0].upper() + word[1:].lower()
                result_string.append(word)
                word = ""
        else:
            word += char
    if word:
        word = word[0].upper() + word[1:].lower()
        result_string.append(word)
    return " ".join(result_string)


# Gestion d'erreur
def is_digit(arg) -> bool:
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
def solve_capitalize_word(args: list[str]) -> None:
    """
    Orchestre la résolution de l'exercice :
    - Valide les arguments passés.
    - Applique une majuscule en première lettre de chaque mot et le reste en minuscule.
    - Affiche le résultat.
    """
    if not validate_arguments(args):
        sys.exit(1)
    result = capitalize_words(args)
    display_result(result)

# Affichage du résultat
def display_result(result: str) -> None:
    """
    Affiche le résultat de la transformation.
    """
    print(result)

# Exécution du programme
if __name__ == "__main__":
    args = get_arguments()
    solve_capitalize_word(args)