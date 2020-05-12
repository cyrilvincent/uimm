# Une nombre premier est un nombre divisible uniquement par 1 et lui-même
# Le premier nombre premier est 2
# 2,3,5,7,11,13,17,19
# La fonction isPrime(x) qui retourne True si x est premier
# Afficher les 1000 premiers nombres premiers

# fibonacci(n) :
# fibonacci(0) = 0
# fibonacci(1) = 1
# fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)
# fibonacci(2) = f(1) + f(0) = 1 + 0 = 1

# Impots
# 14 % pour la fraction supérieure à 10 064 € et inférieure ou égale à 27 794 €
# 30 % pour la fraction supérieure à 27 794 € et inférieure ou égale à 74 517 €
# 41 % pour la fraction supérieure à 74 517 € et inférieure ou égale à 157 806 €
# 45 % pour la fraction supérieure à 157 806 €
# 15064€ sur vos 10064€ vous payez 0% d'impots, vous payez 14% de 15064-10064=5000 soit 700€ soit 700/15064 = 4.6%
# 160000€ sur 10064=>0% sur 27794-10064=>14% sur 74517-27794=>30% sur 157806-74517=>41% sur 160000-157806=>45%
# Faire la fonction calcImpots(revenuNet) => montant à payer
# Puis calculer le % réel d'impôts

def isPrime(x):
    if x < 2:
        return False
    else:
        for i in range(2,x):
            if x % i == 0:
                return False
        return True

print(isPrime(7919))
print(isPrime(8))
for i in range(2,1000):
    if isPrime(i) == True:
        print(i)

def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        res1 = 1
        res2 = 0
        for i in range(2, x+1):
            res = res1 + res2
            res2 = res1
            res1 = res
        return res

print(fibonacci(16))

def calcImpots(salaire):
    if salaire < 10064:
        return 0
    elif salaire < 27794:
        return (salaire - 10064) * 0.14
    elif salaire < 74517:
        return (27794 - 10064) * 0.14 + (salaire - 27794) * 0.3
    elif salaire < 157806:
        return (27794 - 10064) * 0.14 + (74517 - 27794) * 0.3 + (salaire - 74517) * 0.41
    else:
        return (27794 - 10064) * 0.14 + (74517 - 27794) * 0.3 + (157806 - 74517) * 0.41 + (salaire - 157806) * 0.45

impots = calcImpots(1219 * 12 * 0.8)
print(impots, (impots / (1219*12)) * 100)
impots = calcImpots(2000 * 12 * 0.8)
print(impots, (impots / (2000*12)) * 100)
impots = calcImpots(3500 * 12 * 0.8)
print(impots, (impots / (3500*12)) * 100)
impots = calcImpots(10000 * 12 * 0.8)
print(impots, (impots / (10000*12)) * 100)
impots = calcImpots(15000 * 12 * 0.8)
print(impots, (impots / (15000*12)) * 100)



