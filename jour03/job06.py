s = "abcdefghijklmnopqrstuvwxyz" * 10        # La chaîne de caractères

n = 1                                        # Le nombre de caractères pour la première ligne
i = 0                                        # L'indice de départ pour récupérer les caractères

while i+n <= len(s):
    print(s[i:i+n])                          # Affiche la sous-chaîne de longueur n à partir de l'indice i
    i += n                                   # Avance l'indice de départ
    n += 1                                   # Incrémente le nombre de caractères pour la ligne suivante