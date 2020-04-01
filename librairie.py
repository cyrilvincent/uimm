def fact(n):
    res = 1
    while n >= 1:
        res = res * n
        n = n - 1
    return res

def sumarithmetique(n):
    res = 0
    for i in range(n+1):
        res = res + i
    return res

def impots(salaire):
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
    return impots
