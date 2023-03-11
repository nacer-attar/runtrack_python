def comparaison(nombre):
    if nombre > 0 :
        print ("le nombre est positif")
    elif nombre < 0 :
        print ("le nombre est négatif")
    else :
        print ("t'abuses tu le vois que c'est égal à 0")

comparaison(eval(input("tapes un entier réel : ")))