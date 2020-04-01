n = 1
# n! = 3*2*1 = 6
res = 1
while n >= 1:
    res = res * n
    n = n - 1
print(res)

n = 5
res = 0
for i in range(n + 1):
    res = res + i
print(res)
