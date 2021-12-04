# Find the root of the equation -10x^2 - 4x + 1 = 0
# We take the following parameters as input; Hence have addressed them as global variables
x_l = -1
x_u = -2
epsilon_s = -2
x_true = -1


def func(x):  # This function returns the value of f(x) at x
    fun = -10 * pow(x, 2) - 4 * x + 1
    return fun


def bisection(a, b):  # This function implements the bisection algorithm
    epsilon_a = 9999

    while epsilon_a >= epsilon_s:  # Condition when we will terminate the algorithm (when epsilon_s < epsilon_a)
        # Finding x_r, epsilon_s, epsilon_a for current iteration
        x_r = float((a + b) / 2)
        epsilon_a = float(abs((a - b) / (a + b)))
        epsilon_t = abs((x_true - x_r) / x_true)

        # printing x_l, x_u, x_r, epsilon_s, epsilon_t
        print(" x_l = ", a, " x_u = ", b, " x_r = ", x_r, " epsilon_a = ", epsilon_a, " epsilon_t = ", epsilon_t)

        #  finding x_u, x_l for next iteration (step 3 in the algorithm)
        if func(a) * func(x_r) < 0:
            b = x_r

        elif func(a) * func(x_r) > 0:
            a = x_r

        elif func(a) * func(x_r) == 0:
            return x_r

    return x_r


def main():
    # Taking inputs
    global x_l
    x_l = float(input())

    global x_u
    x_u = float(input())

    global epsilon_s
    epsilon_s = float(input())

    global x_true
    x_true = float (input())

    # code for taking list(array) as an input
#   global coefficients
#   coefficients = [float(x) for x in input().split()]

    # code for printing list (array)
#   for x in range(len(coefficients)):
#        print(coefficients[x])

    ans = bisection(x_l, x_u)
    print("The estimated root is = ", ans)


if __name__ == '__main__':
    main()