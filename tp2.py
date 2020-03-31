# Afficher les entiers de 0 à 1000 inclus
# Afficher les chiffres de 3 en 3 entre 0 et 100
# Afficher les puissances de 2 de 0 à 16 2**8=256 2**16=65536
# Afficher un compte à rebours  10,9,8,....,1,0 BOOM
# Difficile : Afficher n! avec n = entier et 5! = 5*4*3*2*1 = 120

i = 0
while i<=1000:
    print(i)
    i = i + 1

i = 0
while i<100:
    print(i)
    i = i + 3

i = 0
while i<=16:
    print(2 ** i)
    i += 1

i = 10
while i >= 0:
    print(i)
    i -= 1
print("BOOOOM")

n = 5


