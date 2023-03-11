
def decaler_message(message):
    """
    Cette fonction prend en entrée un message et un décalage, et renvoie le message décalé
    dans l'alphabet en tenant compte du dépassement (z décalé vers la droite revient sur a, 
    et a décalé vers la gauche revient sur z).
    """
    # Créer une liste de toutes les lettres de l'alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Initialiser la variable qui contiendra le message décalé
    message_decale = ''
    
    # Parcourir chaque caractère dans le message
    for caractere in message:
        # Si le caractère est une lettre de l'alphabet, le décaler
        if caractere in alphabet:
            # Trouver l'indice du caractère dans l'alphabet
            indice_caractere = alphabet.index(caractere)
            # Décaler l'indice du caractère en fonction du décalage
            indice_decale = (indice_caractere + 3) % len(alphabet)
            # Récupérer la lettre décalée correspondante dans l'alphabet
            lettre_decalee = alphabet[indice_decale]
            # Ajouter la lettre décalée au message décalé
            message_decale += lettre_decalee
        # Si le caractère n'est pas une lettre de l'alphabet, le conserver tel quel
        else:
            message_decale += caractere
    
    # Renvoyer le message décalé
    print ("le message crypté est : ", message_decale)
    return message_decale

decaler_message (input("Taper le message à encrypter sans majuscule : "))