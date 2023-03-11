def bien_manger(type,saison):
    if type == "fruit" and saison == "hiver":
        print("orange, mandarine, kiwi")
    elif type == "fruit" and saison == "été":
        print("poire, fraise, cassis")
    elif type == "légume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "légume" and saison == "été":
        print("artichaud, aubergine, navet")
    else:
        print ("apparement le printemps et l'automne rien ne pousse")
        
bien_manger(input("fruit ou légume ?  "),input("quelle saison ?  "))