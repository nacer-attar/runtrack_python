n= eval(input("Nombre de valeurs voulue dans la liste : "))
liste=list (range(n))
print (liste)
first = liste[0]
last  = liste[n-1]
liste[0]=last
liste[n-1]=first
print(liste)