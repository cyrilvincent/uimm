import math
import matplotlib.pyplot as plt
# pip install matplotlib

l = []
for i in range(6280):
    l.append(math.sin(i/1000))

print(l)

plt.plot(l)
plt.show()


