
xl = float(input("Lower limit: "))
xu = float(input("Upper limit: "))
xt = float(input("True value: "))
es = float(input("Error tolerance e_s: "))
max_itr = int(input("Maximum Iteration number: "))
n = int(input("Height power: "))
coefficient = []
for i in range( n +1):
    data = float(input("Enter coefficient value: "))
    coefficient.append(data)


def func(x):
    j = 0
    f = 0
    while j <= n:
        f = f + coefficient[j ] *( x* *j)
        j = j+ 1
        return f


def bisection_method(a, b):
    global midpoint
    if f(a) * f(b) > 0:
        # end function, no root.
        print("No root found.")
    else:
        while (b - a) / 2.0 > tol:
            midpoint = (a + b) / 2.0
            if f(midpoint) == 0:
                return midpoint  # The midpoint is the x-intercept/root.
            elif f(a) * f(midpoint) < 0:  # Increasing but below 0 case
                b = midpoint
            else:
                a = midpoint

        return midpoint


answer = bisection_method(Xl,Xu)

print("Answer:", round(answer, 3))
