"""
Ce script calcule le N-ième terme de la suite de Fibonacci.
- L'utilisateur doit fournir un unique argument, entier positif (N >= 0).
- En cas d'erreur dans les arguments, le script retourne -1.
"""


import sys


# Fonctions utilisées
def fibonacci(n: int) -> int:
    """
    Calcule le N-ième terme de la suite de Fibonacci.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a = 0
    b = 1
    for i in range (2, n + 1):
        next_number = a + b
        a = b
        b = next_number
    return b


# Gestion d'erreur
def is_positive_integer(arg: str) -> bool:
    """
    Vérifie si une chaîne représente un entier positif.
    """
    if not arg:
        return False
    for char in arg:
        if not ("0" <= char <= "9"):
            return False
    return True


def validate_arguments(args: list[str]) -> bool:
    """
    Valide que les arguments sont corrects pour l'exercice.
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
def solve_fibonnaci(args: list[str]) -> None:
    """
    Orchestre la résolution du programme:
    - Valide l'argument.
    - Calcul le N-ième element de la suite Fibonacci.
    - Affiche l'élement selon l'index.
    """
    if not validate_arguments(args):
        display_result(-1)
        sys.exit(1)
    n = int(args[0])
    result = fibonacci(n)
    display_result(result)


# Affichage du résultat
def display_result(result: int) -> None:
    """
    Affiche le résultat final.
    """
    print(result)


# Exécution du programme
if __name__ == "__main__":
    args = get_arguments()
    solve_fibonnaci(args)