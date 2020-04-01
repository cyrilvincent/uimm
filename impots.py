# Jusqu'à 10 064 euros	0 %
# de 10 064 à 27 794 euros	14 %
# de 27 794 à 74 517 euros	30 %
# de 74 517 à 157 806 euros	41 %
# Supérieur à 157 806 euros	45 %

salaire = 17500000
impots = 0
seuil1 = 10065

if salaire < seuil1:
    impots = 0
elif salaire < 27794:
    impots = (salaire - seuil1) * 0.14
elif salaire < 74517:
    impots = (27794 - seuil1) * 0.14 + (salaire - 27794) * 0.3
elif salaire < 157806:
    impots = (27794 - seuil1) * 0.14 + (74517 - 27794) * 0.3 + (salaire - 74517) * 0.41
else:
    impots = (27794 - seuil1) * 0.14 + (74517 - 27794) * 0.3 + (157806 - 74517) * 0.41 + (salaire - 157806) * 0.45

print(f"Impôts {impots:.0f}€")
reel = impots * 100 / salaire
print(f"Taux d'imposition {reel:.2f}%")

