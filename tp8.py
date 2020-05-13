# Lire mesures.csv
# Récupérer les valeurs AT,VT,AM,VM dans des listes
# Pour AM et VM calculer la moyenne (100,0), le min (1,-240), le max (200,+240)
# Afficher AM et VM
# Detecter les erreurs abs(VM - VT) > 1 : afficher ces erreurs
import csv

with open("mesures.csv") as f:
    reader = csv.DictReader(f)
    AT = []
    AM = []
    VT = []
    VM = []
    for row in reader:
        AT.append(float(row["AT"]))
        AM.append(float(row["AM"]))
        VT.append(float(row["VT"]))
        VM.append(float(row["VM"]))

print(AT)
print(AM)
print(VT)
print(VM)

print(min(AM), max(AM), sum(AM)/len(AM))
print(min(VM), max(VM), sum(VM)/len(VM))

for i in range(len(VM)):
    error = abs(VM[i] - VT[i])
    if error > 1:
        print(i, VM[i], VT[i], error)


