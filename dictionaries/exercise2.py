def trier_produits_rupture(base_de_donnees_produits):
    # Initialise une liste vide pour stocker les produits en rupture de stock
    produits_rupture_stock = []

    # Parcourt les clés triées du dictionnaire de la base de données des produits
    for produit_id in sorted(base_de_donnees_produits.keys()):
        # Récupère les informations du produit correspondant à l'identifiant
        produit_info = base_de_donnees_produits[produit_id]
        # Vérifie si la quantité du produit est égale à zéro (rupture de stock)
        if produit_info["quantite"] == 0:
            # Si oui, ajoute le prix et l'identifiant du produit à la liste des produits en rupture de stock
            produits_rupture_stock.append((produit_info["prix"], produit_id))

    # Trie la liste des produits en rupture de stock par prix, de manière décroissante
    produits_rupture_stock.sort(reverse=True)

    # Crée une liste de dictionnaires contenant l'identifiant et le prix de chaque produit en rupture de stock
    produits_rupture_stock_tries = [
        {"id": produit[1], "prix": produit[0]}  # Crée un dictionnaire avec les clés "id" et "prix"
        for produit in produits_rupture_stock   # Pour chaque produit dans la liste triée
    ]

    # Retourne la liste des produits en rupture de stock triés par prix
    return produits_rupture_stock_tries


# Exemple de base de données des produits (identifiant: {"prix": prix, "quantite": quantite})
base_de_donnees_produits = {
    1: {"prix": 10, "quantite": 0},
    2: {"prix": 20, "quantite": 3},
    3: {"prix": 15, "quantite": 0},
    4: {"prix": 25, "quantite": 0},
    5: {"prix": 20, "quantite": 1},
    6: {"prix": 15, "quantite": 0}
}

# Appel de la fonction pour trier les produits en rupture de stock
produits_rupture_stock_tries = trier_produits_rupture(base_de_donnees_produits)

# Affichage des produits en rupture de stock triés par prix
print("Produits en rupture de stock triés par prix :")
for produit in produits_rupture_stock_tries:
    print("Produit ID:", produit["id"], "- Prix:", produit["prix"])
