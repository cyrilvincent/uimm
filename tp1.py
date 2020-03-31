# Créer tp1
# Créer une variable annee = 2020
# Saisir votre année de naissance
# Afficher votre age
# Afficher votre age + 1
# Afficher le reste de la division entière par 2 de votre age (22 % 2 => 0)

annee = 2020
naissance = input("Saisir votre année de naissance: ")
naissance = int(naissance)
print(naissance)
age = annee - naissance
print(f"Vous avez {age} ans")
age2 = age + 1
print(f"L'année prochaine vous aurez {age2} ans")
print(age % 2)

# Marquer si vous avez un age pair ou non
# Marquer si l'année de votre naissance est bisextile
# Marque votre trange d'age bb <2, enfant <12 ado <18 adulte <62 retraité >62
if age % 2 == 0:
    print("Votre age est pair")
else:
    print("Votre age est impair")
if (naissance % 4 == 0 and naissance % 100 != 0) or (naissance % 400 == 0) :
    print("Vous êtes né une année bisextile")
if age < 2:
    print("Vous êtes un BB")
elif age < 12:
    print("Vous êtes un enfant")
elif age < 18:
    print("Vous êtes un ado")
elif age < 62:
    print("Vous êtes un adulte")
else:
    print("Vous êtes un retraité")



