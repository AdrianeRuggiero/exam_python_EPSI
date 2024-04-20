def decode_message(message):
    # Diviser la chaîne de nombres en une liste de nombres
    nombres = message.split()

    # Initialiser une chaîne vide pour stocker le message décodé
    message_decode = ""

    # Convertir chaque nombre selon la table ASCII
    for nombre in nombres:
        # Convertir le nombre en sa représentation ASCII correspondante
        caractere_ascii = chr(int(nombre))
        # Ajouter le caractère ASCII décodé à la chaîne de message décodé
        message_decode += caractere_ascii

    # Retourner le message décodé
    return message_decode


# Message encodé à décoder
message_code = "72 101 108 108 111 44 32 87 111 114 108 100"

# Appeler la fonction pour décoder le message
message_decode = decode_message(message_code)

# Afficher le message décodé
print("Le message décodé est :", message_decode)
