def cac():
    n = eval(input("Quel nombre de valeurs voulez vous dans la liste ? "))
    L = list(range(0 , n))
    print (L[1])
    L[3] = L[2]+L[4]
    print (L[n-1])
    print (L)
cac()