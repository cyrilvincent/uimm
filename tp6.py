# Créer une liste avec vos 10 valeurs
# Refaire la fonction somme et tester
# Faire la fonction moyenne
# Refaire la fonction max => [0,1,-5,99,1] => 99; [-2,-3,-1,-99] => -1
# Refaire la fonction min => -5

maliste = [1,1,-2,5.55,99,-7,100,55,40,38]

def somme(l):
    res = 0
    for i in l:
        res = res + i
    return res

print(somme(maliste))

def max(l):
    res = -99999999999 #l[0]
    for i in l:
        if i > res:
            res = i
    return res

def min(l):
    res = 9999999999999
    for i in l:
        if i < res:
            res = i
    return res

def moyenne(l):
    return somme(l) / len(l)

print(min(maliste))
print(moyenne(maliste))
#toto
