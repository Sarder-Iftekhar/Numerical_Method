def gauss_seidel (n, a, b, xo, k):
    k = 1
    x = [0 for x in range(n)]

    # print(x)
    # print(a)
    # print(b)
    # print(xo)

    while k <= n:
        # print("Iteration", k)
        sum1 = 0
        for i in range(n):
            # print("Finding x", i)
            for j in range(i):
                sum1 = sum1 + a[i][j] * x[j]
                # print(sum1)
            for j in range(i+1, n):
                sum1 = sum1 + a[i][j] * xo[j]
                # print(sum1)
            x[i] = float((-sum1 + b[i]) / a[i][i])
            # print(sum1)
            sum1 = 0
        print("Iteration", k, x);
        k = k+1
        for i in range(n):
            xo[i] = x[i]
        # print(x)


def main():
    n = int(input())

    a = [[0 for x in range(n)] for y in range(n)]  # Inner []: number of elements in each row; outer []: number of rows

    for i in range(n):
        for j in range(n):
            a[i][j] = float(input())
    print(a)

    b = [0 for x in range(n)]
    for i in range(n):
        b[i] = float(input())
    print(b)

    xo = [0 for y in range(n)]
    for i in range(n):
        xo[i] = float(input())
    print(xo)

    k = int(input())

    gauss_seidel(n, a, b, xo, k)


if __name__ == '__main__':
    main()