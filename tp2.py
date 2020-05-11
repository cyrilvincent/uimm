# While
# Faire une boucle de 0 à 1000 avec un pas de 3
# Afficher les puissances de 2 entre 0 et 16
# Afficher un compte à rebours de 10 à 0 inclus
# Afficher la factorielle de n : n! = n * (n - 1)! : 5! = 5 * 4 * 3 * 2 * 1 = 120, 4! = 4 * 3 * 2 * 1 = 24

i = 0
while i < 1000:
    print(i)
    i += 3

for i in range(1000):
    print(i)

i = 0
while i <= 16:
    print(2 ** i)
    i += 1

for i in range(17):
    print(2 ** i)

i = 10
while i >= 0:
    print(i)
    i -= 1

for i in range(10,-1,-1):
    print(i)

n = int(input("N: ")) # 5! = 5 * 4 * 3 * 2 * 1
i = n
res = 1
while i >= 1 :
    res = res * i
    i = i - 1
print(res)

res = 1
for i in range(n,0,-1):
    res = res * i

print(res)

# Refaire le tp2 avec un for
