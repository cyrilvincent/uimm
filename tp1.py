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
