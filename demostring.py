s = "aBcD"
print(s.lower())
print(s.upper())
print(s.capitalize())
s = "   abcd   "
print(s.strip())

x = 1
y = 2
z = 3
if x > y:
    print("X > Y")
    if z > x:
        print("Z > X")
    else:
        print("X >= Z")
elif x < y:
    print("X < Y")
else:
    print("X == Y")

# si y > x et z > y
if y > x and z > y:
    print("AND")

if y > x or z > y:
    print("OR")
