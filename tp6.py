# Créer une liste avec 10 entiers dont certains sont redondants
# Créer la fonction createEvens(10) => return [0,2,4,6,8]
# Créer la fonction filterEven([1,2,3,4,5]) => return [2,4]
# Créer la fonction multiRemove([1,2,5,3,5,4], 5) => return [1,2,3,4]



def createEvens(n):
    res = []
    for i in range(0,n,2):
        res.append(i)
    return res

print(createEvens(100))

def filterEven(l):
    res = []
    for val in l:
        if val % 2 == 0:
            res.append(val)
    return res

def multiRemove(l, n):
    c = l.count(n)
    for i in range(c):
        l.remove(n)
    return l

l1 = [1,0,2,5,99,5,7,5,63,10]
res = filterEven(l1)
print(res)
res = multiRemove(l1, 5)
print(res)