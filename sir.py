# Find the root of the equation -10x^2 - 4x + 1 = 0

x_l = float(input())
x_u = float(input())
epsilon_s = float(input())


def func(x):  # This function returns the value of f(x) at x
    fun = -10 * pow(x, 2) - 4 * x + 1
    return fun


def bisection(a, b):  # This function implements the bisection algorithm
    epsilon_a = 9999

    while epsilon_a >= epsilon_s:  # Condition when we will terminate the algorithm (when epsilon_s < epsilon_a)
        # Finding x_r, epsilon_s, epsilon_a for current iteration
        x_r = float((a + b) / 2)
        epsilon_a = float(abs((a - b) / (a + b)))

        # printing x_l, x_u, x_r, epsilon_s, epsilon_t
        print(" x_l = ", a, " x_u = ", b, " x_r = ", x_r, " epsilon_a = ", epsilon_a)

        #  finding x_u, x_l for next iteration (step 3 in the algorithm)
        if func(a) * func(x_r) < 0:
            b = x_r

        elif func(a) * func(x_r) > 0:
            a = x_r

        elif func(a) * func(x_r) == 0:
            return x_r

    return x_r


ans = bisection(x_l, x_u)
print("The estimated root is = ", ans)

# code for taking list(array) as an input
n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

# code for printing list (array)
print(arr)




