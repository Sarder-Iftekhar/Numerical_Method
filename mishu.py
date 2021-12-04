xl = float(input("Lower limit: "))
xu = float(input("Upper limit: "))
xt = float(input("True value: "))
es = float(input("Error tolerance e_s: "))
max_itr = int(input("Maximum Iteration number: "))
n = int(input("Height power: "))
coefficient = []
for i in range(n+1):
    data = float(input("Enter coefficient value: "))
    coefficient.append(data)


def func(x):
    j = 0
    f = 0
    while j <= n:
        f = f + coefficient[j]*(x**j)
        j = j+1
        return f

func()