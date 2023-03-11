for lettre in range(ord('z'), ord('a')-1, -1):
    #ord caractères > codes ASCII // range (start,stop,step)
    print(chr(lettre), end=' ')
    #print equivalent display // chr codes ASCII > caractères

    #littéralement pour les "lettres" situées entres les codes ASCII de 'z' et 'a'-1 (pout inclure le a)
    #avec un pas de -1, afficher les caractères des 'lettres' et finir quand la série est finie (' ')