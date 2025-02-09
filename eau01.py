"""
Ce script génère et affiche toutes les combinaisons possibles de deux nombres distincts entre 00 et 99.
- Chaque combinaison est affichée sous la forme '00 01', '00 02', ..., '98 99'.
- Les nombres sont affichés dans l'ordre croissant et séparés par des espaces.
"""

# Fonction
def generate_combinations() -> list[str]:
    """
    Génère toutes les combinaisons double de deux chiffres distincts dans l'ordre croissant.
    """
    combinations = []
    for first_number in range(0, 100):  # Parcourt les chiffres de 0 à 9
        for second_number in range(first_number + 1, 100): 
            combinations.append(f"{first_number:02} {second_number:02}")
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