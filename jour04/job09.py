L = [8,24,27,48,2,16,9,102,7,84,91]

minimum=maximum=L[0]

for element in L:
    if element < minimum :
        minimum = element
    elif element > maximum :
        maximum = element
        
print("minimum : ",minimum,"maximum : ", maximum)

