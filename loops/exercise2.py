# Définition de la fonction afficher_pyramide()
def afficher_pyramide():
    # Demander à l'utilisateur la hauteur de la pyramide et convertir la saisie en entier
    hauteur = int(input("Entrez la hauteur de la pyramide : "))

    # Vérifier si la hauteur est valide
    if hauteur <= 0:
        # Si la hauteur est inférieure ou égale à zéro, afficher un message d'erreur
        print("La hauteur doit être un entier positif.")
    else:
        # Si la hauteur est valide, dessiner la pyramide
        for i in range(1, hauteur + 1):
            # Pour chaque ligne de la pyramide, imprimer des espaces pour la marge à gauche
            print(" " * (hauteur - i), end="")
            # Imprimer des étoiles pour former la partie centrale de la pyramide
            print("*" * (2 * i - 1))


# Appeler la fonction afficher_pyramide() pour exécuter le code
afficher_pyramide()
