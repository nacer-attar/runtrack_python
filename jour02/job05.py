def calcule(num1,operator,num2):
    if operator == '+':
        return (num1 + num2)
    elif operator == '-':
        return (num1 - num2)
    elif operator == '/':
        return (num1 / num2)
    elif operator == '%':
        return (num1 % num2)
    elif operator == '*':
        return (num1 * num2)
    else :
        print("opérateur invalide")
    return res
res=calcule(1,'/',2)
print (res)