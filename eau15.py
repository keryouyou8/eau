"""
        Eau : ok

Ce script affiche un message de célébration indiquant la fin de l’Épreuve de l’Eau.
- L'utilisateur peut fournir un adjectif décrivant son expérience.
- Si aucun adjectif n'est fourni, le script utilise "technique" par défaut.
"""

import sys


# Fonctions utilisées
def generate_victory_message(adjective: str) -> str:
    """
    Génère le message de victoire avec l'adjectif fourni.
    """
    return f"J’ai terminé l’Épreuve de l’Eau et c’était {adjective}."


# Gestion d'erreur
def validate_arguments(args: list[str]) -> bool:
    """
    Vérifie que les arguments sont valides (0 ou 1 seul argument accepté).
    """
    if len(args) > 1:
        print("error: Trop d'arguments fournis. Fournissez un seul adjectif ou aucun.")
        return False
    return True


# Parsing
def get_arguments() -> list[str]:
    """
    Récupère les arguments passés en ligne de commande (exclut le nom du script).
    """
    return sys.argv[1:]


# Résolution
def solve_victory_message(args: list[str]) -> None:
    """
    Orchestre la génération et l’affichage du message de victoire.
    - Valide les arguments.
    - Génère et affiche le message.
    """
    if not validate_arguments(args):
        sys.exit(1)

    adjective = args[0] if len(args) == 1 else "technique"
    result = generate_victory_message(adjective)
    display_result(result)


# Affichage du résultat
def display_result(result: str) -> None:
    """
    Affiche le message de victoire.
    """
    print(result)


# Exécution du programme
if __name__ == "__main__":
    args = get_arguments()
    solve_victory_message(args)
