import csv
with open("house.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        s = int(row["surface"])
        l = int(row["loyer"])
        print(l / s)

# Faire une fonction displayLoyerPerM2(file) => afficher les loyers par m2
# Faire une fonction calcSurfaceMoyenne(file) => return surface moyenne 10,20,30 => 20
# Faire une fonction calcLoyerMoyen(file) => return loyer moyen 10,20,30 => 20
# Faire une fonction getLoyerPerM2(file) => 10,100 20,350 30,300 => [10, 17.5, 10]
# Calculer le loyer moyen par m2, le min , max