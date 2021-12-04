n = int(input("Height power: "))
xl = float(input("Lower limit: "))

xu = float(input("Upper limit: "))
xt = float(input("True value: "))
es = float(input("Error tolerance e_s: "))
max_itr = int(input("Maximum Iteration number: "))

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


def bi_section(xl, xu):
    ea = 9999
    a = 1
    while (a < max_itr) and (ea >= es):
        xr = float(((func(xl) * xu) - (xl * func(xu))) / (func(xl) - func(xu)))
        ea = float(abs((xu-xl)/(xl+xu)))
        et = float(abs(((xt - xr)/xt)))
        print("Iteration ", a, "XL= ", round(k, 4), " Xu= ", round(m, 4), " Xr=", round(xr, 4), " Epsilon_a= ", round(ea, 4), " Epsilon_true= ", round(et, 4))
        if(func(xl) * func(xr)) < 0:
            xu = xr
        elif func(xl) * func(xr) > 0:
            xl = xr
        elif func(xl) * func(xr) == 0:
            return xr
        a = a+1
    return xr


Final_answer = bi_section(xl, xu)
print("The root is:  ", Final_answer)











