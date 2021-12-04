
import numpy as np

a = np.array([[1, 2, 1],
              [3, 8, 1],
              [0, 4, 1]])

b = np.array([2, 12, 2])

b = b.reshape(-1, 1)

a_b = np.hstack([a, b])
# print
n = len(a)
i = 0
j = 0
k = 0
e = np.eye(3)
while i < n:
    j = i+1
    while j < n:
        i_d = np.eye(3)
        k = (a[j, i]/a[i, i])
        i_d[j, i] = (-1*k)
        a = i_d.dot(a)
        e = e.dot(i_d)
        j = j+1
    i = i+1
l = e.dot(-1)
u = a.copy()


d = np.ones(n, float)
d = d.reshape(-1, 1)
x = 0
y = 0

for x in range(n):
    su = b[x]
    for y in range(0, x):
        su = su - l[x, y] * d[y]
    d[x] = su

x = np.zeros(n, float)
k = n - 1
p = n - 1
q = n - 1
g = n - 1
while k >= 0:
    s = d[k]
    while g > p:
        s = s - (u[k, g] * x[g])
        g = g - 1
        q = 1
    if p == q:
        p = -1
    x[k] = s / u[k, k]
    k = k - 1

print("L = ", l)
print("\nU = ", u)
print("\n")
for i in range(n):
    print("d = ", i, d[i])

print("\n")
for k in range(n):
    print("x = ", k, x[k])
