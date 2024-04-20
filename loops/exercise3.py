# Définition de la fonction trouver_plus_grand_nombre()
def trouver_plus_grand_nombre():
    # Demander à l'utilisateur d'entrer trois nombres et les convertir en nombres flottants
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
    nombre3 = float(input("Entrez le troisième nombre : "))

    # Comparer les trois nombres pour trouver le plus grand
    if nombre1 >= nombre2 and nombre1 >= nombre3:
        plus_grand_nombre = nombre1
    elif nombre2 >= nombre1 and nombre2 >= nombre3:
        plus_grand_nombre = nombre2
    else:
        plus_grand_nombre = nombre3

    # Afficher le plus grand nombre trouvé
    print("Le plus grand nombre est :", plus_grand_nombre)


# Appeler la fonction trouver_plus_grand_nombre() pour exécuter le code
trouver_plus_grand_nombre()
