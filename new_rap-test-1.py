import math

k = -1
w = 0
x_i = -1
epsilon_s = 0
maxitr = -2


def fun1(x_i):
    return float(8 * math.exp(-1 * k * x_i) * math.cos(w * x_i))


def fun2(x_i):
    return float((-8 * k * math.exp(-1*k*x_i)*math.cos(w*x_i)) - (8*w*math.exp(-1*k*x_i)*math.sin(w*x_i)))

def main():

    global k
    global w
    global x_i
    global epsilon_s
    global maxitr

    a = open("fhm135.txt", "r")
    k = float(a.readline())
    w = float(a.readline())
    x_i = float(a.readline())
    epsilon_s = float(a.readline())
    maxitr = int(a.readline())
    b = open("fhm135output.txt", "w")

    iteration = 1
    epsilon_a = 9999
    x = 0
    while epsilon_a >= epsilon_s and iteration <= maxitr:
        x = (x_i - (fun1(x_i) / fun2(x_i)))
        epsilon_a = abs(float(((x-x_i)/x)))
        print("iteration number ", iteration, " =  X_i =", x_i, " X_i+1 = ", x, ' epsilon_a =', epsilon_a)
        b.write("iteration number %d" % iteration)
        b.write(" =  X_i = %.16f" % x_i)
        b.write(" X_i+1 = %.16f" % x)
        b.write(" epsilon_a = %.16f \n" % epsilon_a)
        x_i = x
        iteration = iteration+1
    print("The estimated root is = ", x)
    b.write("\n \nThe estimated root is = %.16f" % x)
    a.close()
    b.close()


if __name__ == '__main__':
    main()
