def triangle(a,b,c):
    if a + b > c and a + c > b and b + c > a: #le triangle peut exister
        if a==b==c:
            print("le triangle est équilatéral")
        elif a == b or b == c or a == c:
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 :
                print("le triange est rectangle et isocèle")
            else :
                print("le triangle est isocèle mais pas rectangle")
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 :
            print("le triangle est rectangle mais non isocèle")
        else:
            print("le triangle est quelconque")
    else:
        print("impossible de construire un triangle avec ces longueurs")

triangle(eval(input('longueur de a : ')),eval(input('longueur de b : ')),eval(input('longueur de c : 4')))