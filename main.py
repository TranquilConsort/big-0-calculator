from math import log
from simpleeval import simple_eval

# For O(n!)
def factorial(stop):
    a = 1
    b = 2
    while True:
        aa = b * a
        bb = b + 1
        if aa > stop:
            break
        a = aa
        b = bb
    ans = b - 1
    return ans

# For 2n
def exponential(arg):
    a = log(arg, 2)
    ans = int(a)
    return ans


# For n3
def cubic(arg):
    a = arg ** (1 / 3)
    b = format(a, "4.3e")
    ans = b
    return ans

# For n2
def quadratic(arg):
    a = arg ** (1 / 2)
    b = format(a, "4.3e")
    ans = b
    return ans

# For nlogn
def log_linear(arg):
    def f(x):
        return x * log(x, 2)

    a = 1
    b = 2 ** 1023
    for i in range(2000):
        c = (a + b) / 2
        if f(c) > arg:
            b = c
        elif f(c) < arg:
            a = c
        else:
            break
        if abs(b - a) < 1e-9:
            break
    ans = format(c, "4.3e")
    return ans

# For n
def linear(arg):
    b = arg
    ans = format(b, "4.3e")
    return ans

# For √n
def square_root(arg):
    b = arg ** 2
    ans = format(b, "4.3e")
    return ans

# For logn
def logarithmic(arg):
    if arg > 1023:
        c = format(arg, "4.3e")
        ans = f"2^({c})"
    else:
        b = 2 ** (arg)
        ans = format(b, "4.3e")
    return ans

if __name__ == "__main__":
    try:
        while True:
            option = input(
                "\na = logn\tb = √n\tc = n\td = nlogn\te = n2\tf = n3\tg = 2n\th = n!\ti = across all algorithms\tj = multiple inputs across all algorithms\nChoose one from the options above: ")

            option = option.lower()

            if option != "j":
                x = simple_eval(input("Enter the value of x: "))

            if option == "a":
                print(f"Largest size of n = {logarithmic(x)}")

            elif option == "b":
                print(f"Largest size of n = {square_root(x)}")

            elif option == "c":
                print(f"Largest size of n = {linear(x)}")

            elif option == "d":
                print(f"Largest size of n = {log_linear(x)}")

            elif option == "e":
                print(f"Largest size of n = {quadratic(x)}")

            elif option == "f":
                print(f"Largest size of n = {cubic(x)}")

            elif option == "g":
                print(f"Largest size of n = {exponential(x)}")

            elif option == "h":
                print(f"Largest size of n = {factorial(x)}")

            elif option == "i":
                print(
                    f"log(n) = {logarithmic(x)}\t√n = {square_root(x)}\tn = {linear(x)}\tnlogn = {log_linear(x)}\tn2 = {quadratic(x)}\tn3 = {cubic(x)}\t2n = {exponential(x)}\tn! = {factorial(x)}")

            elif option == "j":
                a = simple_eval(input("How many inputs: "))
                myList = []
                for i in range(a):
                    b = simple_eval(input(f"Enter no {i + 1} value: "))
                    myList.append(b)
                print("")
                for i in range(a):
                    x = myList[i]
                    neat = format(x, "4.3e")
                    print(
                        f"{i + 1}. For {neat}: log(n) = {logarithmic(x)}\t√n = {square_root(x)}\tn = {linear(x)}\tnlogn = {log_linear(x)}\tn2 = {quadratic(x)}\tn3 = {cubic(x)}\t2n = {exponential(x)}\tn! = {factorial(x)}")

            else:
                print(f"{option} is not a valid option.")

    except Exception as e:
        print(f"{e}.Input a valid number e.g 12, 20000, 7*10**20")