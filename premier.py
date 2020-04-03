# Créer la fonction estPremier(n) qui renvoie 1 si n est premier 0 sinon
# estPremier(7) => 1
# estPremier(8) => 0
# %
# Un nombre premier est un nombre divisible uniquement par 1 et par lui même
# 0 et 1 ne sont pas premier
# 2,3,5,7,11,13,17,...
# Un nombre n n'est pas premier s'il possède un diviseur entre 2 et n-1

# Créer la fonction afficherPremiers(n) et qui affiche tous les nombres premiers entre 2 et n
# afficherPremiers(10) => 2,3,5,7

# Faire la fonction cryptage qui crypte un nombre par sa clé, vérifier que la clé est un nombre premier
# cryptage(100,7) => 700
# cryptage(100,8) => -1
# decryptage(700, 7) => 100

# range(2,5) => 2,3,4

def estPremier(n):
    if n < 2:
        return 0
    else:
        for i in range(2,n):
            if n % i == 0:
                return 0
        return 1

def affichePremiers(n):
    for i in range(2,n):
        if estPremier(i) == 1:
            print(i)

def cryptage(msg, key):
    if estPremier(key):
        return msg * key
    else:
        return -1

def decryptage(msg, key):
    if estPremier(key):
        return msg/key
    else:
        return -1

s ="toto toto "
res = s.replace(" ","")
print(res)
print(estPremier(2))
affichePremiers(6700417)

message = 100
key = 6700417
messagecrypte = cryptage(message, key)
print(messagecrypte)
message = decryptage(messagecrypte, key)
print(message)
