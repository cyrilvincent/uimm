import matplotlib.pyplot as plt
import csv

# File > Settings > Project > Project Interpreter
# Cliquer sur l'icone +, Saisir Matplotlib, sélectionner et installer

#plt.plot(range(100), range(100))
#plt.scatter(range(100), range(100))
#plt.show()

with open("house.csv") as f:
    reader = csv.DictReader(f)
    surfaces = []
    loyers = []
    for row in reader:
        s = float(row["surface"])
        l = float(row["loyer"])
        surfaces.append(s)
        loyers.append(l)
print(surfaces)
print(loyers)

plt.scatter(surfaces, loyers)
#plt.plot(surfaces, loyers)
plt.show()