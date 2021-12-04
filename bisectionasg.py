x_l = -1
x_u = -2
n = -1
epsilon_s = -2
num_iteration = -1
x_true = -1
coefficients = []


def func(x, p):
    i = 0
    fun = 0
    while i <= p:
        fun += coefficients[i]*pow(x, i)
        i = i+1
    return fun


def bisection(a, b):

    iteration = 1
    epsilon_a = 9999
    x_r = -1

    while epsilon_a >= epsilon_s and iteration <= num_iteration:
        x_r = float((a + b) / 2)
        epsilon_a = float(abs((a - b) / (a + b)))
        epsilon_t = abs((x_true - x_r) / x_true)

        print(" x_l = ", a, " x_u = ", b, " x_r = ", x_r, " epsilon_a = ", epsilon_a, " epsilon_t = ", epsilon_t)

        if func(a, n) * func(x_r, n) < 0:
            b = x_r

        elif func(a, n) * func(x_r, n) > 0:
            a = x_r

        elif func(a, n) * func(x_r, n) == 0:
            return x_r

        iteration = iteration + 1

    return x_r


def main():
    global n
    n = int(input())

    global x_l
    x_l = float(input())

    global x_u
    x_u = float(input())

    global num_iteration
    num_iteration = int(input())

    global epsilon_s
    epsilon_s = float(input())

    global x_true
    x_true = float(input())

    global coefficients
    coefficients = [float(x) for x in input().split()]

    for x in range(len(coefficients)):
        print(coefficients[x])

    ans = bisection(x_l, x_u)
    print("The estimated root is = ", ans)


if __name__ == '__main__':
    main()