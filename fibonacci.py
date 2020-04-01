def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        res1 = 1
        res2 = 0
        res = 0
        for i in range(2,n+1):
            res = res1 + res2
            print(res2, res1, res)
            res2 = res1
            res1 = res
        return res

print(fibonacci(15))
