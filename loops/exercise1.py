# Import de la bibliothèque random pour générer des nombres aléatoires
import random


# Définition de la fonction deviner_le_nombre()
def deviner_le_nombre():
    # Génération aléatoire d'un nombre mystère entre 1 et 100 inclus
    nombre_mystere = random.randint(1, 100)

    # Affichage d'un message pour demander à l'utilisateur de deviner le nombre mystère et lui indiquer le nombre de tentatives disponibles
    print("Devinez le nombre mystère entre 1 et 100. Vous avez 5 tentatives.")

    # Boucle for pour gérer les 5 tentatives
    for tentative in range(1, 6):
        # Construction du message pour l'utilisateur indiquant le numéro de la tentative
        message = "Tentative {}: Entrez votre estimation : ".format(tentative)
        # L'utilisateur entre sa supposition
        guess = int(input(message))

        # Vérification si la supposition de l'utilisateur est égale au nombre mystère
        if guess == nombre_mystere:
            # Si la supposition est correcte, affichage des félicitations et fin du jeu
            print("Félicitations ! Vous avez deviné le nombre mystère :", nombre_mystere)
            return
        # Si la supposition est incorrecte, vérification si elle est trop petite
        elif guess < nombre_mystere:
            # Affichage que le nombre mystère est plus grand
            print("Le nombre mystère est plus grand.")
        # Si la supposition est incorrecte et pas trop petite, elle est trop grande
        else:
            # Affichage que le nombre mystère est plus petit
            print("Le nombre mystère est plus petit.")

        # Calcul des tentatives restantes
        tentatives_restantes = 5 - tentative
        # Affichage du nombre de tentatives restantes
        print("Il vous reste", tentatives_restantes, "tentatives.")

    # Si l'utilisateur épuise toutes ses tentatives, affichage du nombre mystère et fin du jeu
    print("Vous avez épuisé toutes vos tentatives. Le nombre mystère était :", nombre_mystere)


# Appel de la fonction deviner_le_nombre() pour démarrer le jeu
deviner_le_nombre()
