def draw_rectangle(n):
    # Dessine la première ligne du rectangle avec des tirets et des barres verticales
    print("+" ,"-" * (n-2),"+")

    # Dessine les lignes du milieu avec des # et des espaces
    for i in range(n-2):
        print("|", "#" * (n-3-i) + " "+ "#" * i,"|")
    # Dessine la dernière ligne du rectangle avec des tirets et des barres verticales
    print("+" ,"-" * (n-1),"+")

# Exemple d'utilisation
draw_rectangle(eval(input("taille de tapis : ")))