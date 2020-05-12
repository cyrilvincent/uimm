l1 = [2,8,0,12,99,-2,50]
print(l1)
print(l1[0])
l1[0] = 33
print(l1)
for val in l1:
    if val % 2 == 0:
        print(val)

def sum(l):
    res = 0
    for val in l:
        res = res + val
    return res

print(sum(l1))
print(sum([1,2,3]))

print(l1)
l1.append(999)
l1.insert(2,888)
l1.remove(12)
print(l1)
l1.count(888)
print(l1)
print(l1.count(888))


