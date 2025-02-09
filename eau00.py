"""
Ce script affiche toutes les combinaisons possibles de trois chiffres distincts dans l'ordre croissant.
- Chaque combinaison est affichée sous forme de triplet, séparée par des virgules.
"""

# Fonction utilsées
def generate_combinations() -> list[str]:
    """
    Génère toutes les combinaisons de trois chiffres distincts dans l'ordre croissant.
    """
    combinations = []
    for first_number in range(0, 10):  # Parcourt les chiffres de 0 à 9
        for second_number in range(first_number + 1, 10):  # Commence après 'a'
            for third_number in range(second_number + 1, 10):  # Commence après 'b'
                combinations.append(f"{first_number}{second_number}{third_number}")
    return combinations


# Résolution
def solve_combinations() -> None:
    """
    Orchestre la résolution de l'exécution :
    - Génère les combinaisons.
    - Affiche les combinaisons générées.
    """
    combinations = generate_combinations()
    display_combinations(combinations)


# Affichage du résultat
def display_combinations(combinations: list[str]) -> None:
    """
    Affiche une liste de combinaisons, séparées par des virgules.
    """
    print(", ".join(combinations))


# Exécution du programme
if __name__ == "__main__": # Pour éviter que tout le fichier s'exécute si on l'importe
    solve_combinations()