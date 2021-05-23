import random
import matplotlib.pyplot as plt

x = []
y = []

for i in range(100):
    x.append(random.uniform(-1, 1))
    y.append(random.uniform(-1, 1))

plt.scatter(x, y, color='b', marker='.')
plt.show()
