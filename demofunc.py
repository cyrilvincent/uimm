def hello():
    print("Hello World!")

def hellowithparam(word):
    print(f"Hello {word}")

def add(i, j):
    return i + j

def boucletoto(nb):
    for i in range(nb):
        hello()

hellowithparam("toto")
x = add(2,3)
print(x)
print(add(2,3))
boucletoto(10)