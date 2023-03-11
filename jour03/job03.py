def afficher_nombres():                     # on créé une fonction 
    for i in range(101):                    # pour tout i de 0 à 100
        if i not in [26, 37, 88]:           # condition : si i =/= de 26 37 et 88 
            print(i)                        # alors afficher i

afficher_nombres()                          # appel de la fonction
