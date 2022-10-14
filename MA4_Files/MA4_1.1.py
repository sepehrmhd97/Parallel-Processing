import math
import random
import matplotlib.pyplot as plt
import numpy as np

n = 100000
xlist = np.random.uniform(-1, 1, n)
ylist = np.random.uniform(-1, 1, n)

count_nc = 0
colors = ["red"] * n

for i in range(0,n):
    if (xlist[i]**2 + ylist[i]**2) <= 1:
        count_nc += 1
    else:
        colors[i] = "blue"

app_Pi = 4 * (count_nc/n)

    
print('Number of Points in the circle = {}' .format(count_nc))
print('Approximate Pi = {}' .format(app_Pi))
print('Builtin Constant Pi = {}' .format(math.pi))

plt.scatter(xlist, ylist, c=colors)
plt.show()

