maliste = [1,1,-2,5.55,99,-7,100,55,40,38]
# print(maliste)
# for value in maliste:
#     print(f"value={value}")

# range(5) <=> [0,1,2,3,4]
# range(10,-1,-3) <=> [10,7,4,1]
# for i in range(10,-1,-3):
#     print(i)

# for value in maliste:
#     print(value)

print(sum(maliste))

def somme(l):
    res = 0
    for i in l:
        res = res + i
    return res

print(somme(maliste))
print(somme(range(10000)))
print(len(range(10000)))
