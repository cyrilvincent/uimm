# Fonctions
# Faire la fonction add(i,j) qui retourne i+j
# Faire la fonction max(i,j) qui retourne i si i >j, j sinon
# Faire la fonction isEven(i) qui retourne True ou False si i est pair ou impair
# Faire la fonction isBissextile(i) qui retourne True si i est bissextile
# Faire la fonction fact(n) qui retourne n!

def add(i,j):
    return i + j

def max(i,j):
    if i > j:
        return i
    else:
        return j

def isEven(i):
    if i % 2 == 0:
        return True
    else:
        return False

def isBissextile(i):
    if (i % 4 == 0 and not i % 100 == 0) or i % 400 == 0:
        return True
    else:
        return False

def fact(n):
    res = 1
    for i in range(n, 0, -1):
        res = res * i
    return res

print(fact(5))