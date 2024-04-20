def etudiants_note(dictionnaire_notes):
    # Initialise un dictionnaire vide pour stocker les étudiants sélectionnés
    etudiants_selectionnes = {}

    # Parcourt chaque paire clé-valeur dans le dictionnaire de notes
    for nom, note in dictionnaire_notes.items():
        # Vérifie si la note de l'étudiant est supérieure ou égale à 15
        if note >= 15:
            # Si oui, ajoute l'étudiant et sa note au dictionnaire des étudiants sélectionnés
            etudiants_selectionnes[nom] = note

    # Retourne le dictionnaire des étudiants sélectionnés
    return etudiants_selectionnes


# Dictionnaire de notes des étudiants
dictionnaire_notes = {
    "Alice": 18,
    "Bob": 12,
    "Charlie": 16,
    "David": 14,
    "Eva": 19
}

# Appel de la fonction pour sélectionner les étudiants ayant une note supérieure ou égale à 15
etudiants_selectionnes = etudiants_note(dictionnaire_notes)

# Affichage du nouveau dictionnaire avec les étudiants sélectionnés
print("Étudiants avec une note moyenne supérieure ou égale à 15 :")
print(etudiants_selectionnes)
