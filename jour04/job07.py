L = [8, 24,48,2,16]
for v in range(len(L)):
    L[v] %= 3
compteur_multiple_de_3= L.count(0)
print(L)
print (compteur_multiple_de_3)
