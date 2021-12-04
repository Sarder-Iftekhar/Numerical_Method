def f(x):
    return (x ** 2 - 11)


def bisection_method(a, b, tol):
    if f(a) * f(b) > 0:
        # end function, no root.
        print("No root found.")
    else:
        while (b - a) / 2.0 > tol:
            midpoint = (a + b) / 2.0
            if f(midpoint) == 0:
                return (midpoint)  # The midpoint is the x-intercept/root.
            elif f(a) * f(midpoint) < 0:  # Increasing but below 0 case
                b = midpoint
            else:
                a = midpoint

        return (midpoint)


answer = bisection_method(-1, 5, 0.0001)

print("Answer:", round(answer, 3))

