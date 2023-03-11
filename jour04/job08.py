L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
i = 0
while i < len(L):
    if L[i] % 2 != 0:
        del L[i]
    else :
        i +=1
print(L)
somme=sum(L)
print (somme)