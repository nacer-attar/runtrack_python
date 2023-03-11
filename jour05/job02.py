def draw_rectangle(width, height):
    # Dessine la première ligne du rectangle avec des tirets et des barres verticales
    print("|" ,"-" * width,"|")

    # Dessine les lignes du milieu avec des barres verticales et des espaces
    for i in range(height-2):
        print("|" + " "*(width+2) + "|")

    # Dessine la dernière ligne du rectangle avec des tirets et des barres verticales
    print("|" ,"-" * width,"|")

# Exemple d'utilisation
draw_rectangle(eval(input("longueur : ")), eval(input("largeur : ")))