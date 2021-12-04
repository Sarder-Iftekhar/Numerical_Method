import numpy as np
import matplotlib.pyplot as plt

m = np.array([[2.00, 7.2], [4.25, 7.1], [5.25, 6.0], [7.81, 5.0], [9.20, 3.5], [10.60, 5.0]])
print("m", m)


def lagrange(points, x):
    sum = 0
    n = len(points)
    for i in range(n):
        xi, yi = points[i]

        def L(i):

            Lx = 1
            for j in range(n):
                if i != j:
                    xj, yj = points[j]

                    Lx *= float(x - xj) / float(xi - xj)

            return Lx

        sum += yi * L(i)
    print("sum", sum)
    return sum


print("m", m)
z = []

for k in range(13):
    z.append([k, np.round(lagrange(m, k), 10)])
z = np.array(z)
print(z)

plt.plot(z[:, 0], z[:, 1], 'b')
plt.show()
