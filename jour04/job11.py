régale_toi = input("taper une série de caractère séparé par des espaces : ")    # classique input
Ls = (régale_toi.split())                                                       # transforme l'input en list
L = [int(x) for x in Ls]                                                        # converti les string en integer
print (L)                                                                       # la liste est créée
n = 0
while n < len(L):
    L[n] += 1
    n += 1
print (L)
