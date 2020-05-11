x = int(input("X: "))
y = int(input("Y: "))
if x > 0:
    print("x est positif")
    if y > 0:
        print("y est positif")
elif x < 0:
    print("x est négatif")
else:
    print("x est = 0")