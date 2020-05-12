import csv


# Faire une fonction displayLoyerPerM2(file) => afficher les loyers par m2
# Faire une fonction calcSurfaceMoyenne(file) => return surface moyenne 10,20,30 => 20
# Faire une fonction calcLoyerMoyen(file) => return loyer moyen 10,20,30 => 20
# Faire une fonction getLoyerPerM2(file) => 10,100 20,350 30,300 => [10, 17.5, 10]
# Calculer le loyer moyen par m2, le min , max

def displayLoyerPerM2(file):
    with open(file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            s = int(row["surface"])
            l = int(row["loyer"])
            print(l / s)

#displayLoyerPerM2("house.csv")

def calcSurfaceMoyenne(file):
    with open(file) as f:
        reader = csv.DictReader(f)
        res = 0
        nb = 0
        for row in reader:
            s = int(row["surface"])
            res += s
            nb += 1
        return res / nb

print(calcSurfaceMoyenne("house.csv"))

def calcLoyerMoyen(file):
    with open(file) as f:
        reader = csv.DictReader(f)
        res = 0
        nb = 0
        for row in reader:
            s = int(row["loyer"])
            res += s
            nb += 1
        return res / nb

print(calcLoyerMoyen("house.csv"))

def getLoyerPerM2(file):
    res = []
    with open(file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            s = int(row["surface"])
            l = int(row["loyer"])
            res.append(l / s)
    return res

def sum(l):
    res = 0
    for val in l:
        res += val
    return res

def average(l):
    return sum(l)/len(l)

l = getLoyerPerM2("house.csv")
print(average(l))
