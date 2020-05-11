# Créer la variable year = 2020
# Saisir votre année de naissance dans une variable entière
# Afficher votre année de naissance
# Afficher votre age de l'année en cours (year)
# Afficher votre age de l'année prochaine
# Afficher le modulo 2 de votre age
year = 2020
birth = int(input("Veuillez saisir votre année de naissance: "))
age = year - birth
print(f"Vous avez {age} ans")
print(f"L'année prochaine vous aurez {age + 1} ans")
print(age % 2)

# Afficher si votre age est pair ou impair
# Afficher votre catégorie d'age (<2 BB, <12 Enfant, < 18 Ado, <62 Adulte, Retraité)
# Affichée si votre année de naissance est bissextile d'après wikipedia

if age % 2 == 0:
    print("Votre age est pair")
else:
    print("Votre age est impair")

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

if (birth % 4 == 0 and not birth % 100 == 0) or (birth % 400 == 0):
    print("Vous êtes né une année bissextile")
else:
    print("Vous êtes né une année non bissextile")
