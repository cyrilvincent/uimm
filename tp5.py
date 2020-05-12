# Créer une liste avec 10 entiers l1 = [1,2,99,....]
# Créer la fonction sum(l) => la somme des éléments de l
# Créer la fonction average(l) => la moyenne, en sachant que len(l) => longueur
# Créer la fonction min(l) => min
# Créer la fonction max(l) => max

def sum(l):
    res = 0
    for val in l:
        res += val
    return res

def average(l):
    return sum(l)/len(l)

def max(l):
    res = l[0]
    for val in l:
        if val > res:
            res = val
    return res

def max(l):
    res = l[0]
    for val in l:
        if val < res:
            res = val
    return res

l1 = [1,0,2,5,99,-5,7,-80,63,10]
print(sum(l1))
print(average(l1))
print(max(l1))
