def func(x):
    return (3*(x + 1)*(x - 1/2)*(x - 1))

def bisection(a, b, func):
    mid = (a + b) / 2
    if(abs(func(mid)) < 0.01):
        return mid
    else:
        if(func(mid) * func(a) > 0):
            return bisection(mid, b, func)
        else:
            return bisection(a, mid, func)

print(bisection(-10, 10, func))