import math

def bisection_method(f, a, b, tol=0.0000001, max_iter=1000):
    steps = 0
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")
    while (b - a) / 2 > tol and steps < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        steps += 1
    return c, steps

def newton_raphson_method(f, df, x0, tol=0.0000001, max_iter=1000):
    steps = 0
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            break
        if dfx == 0:
            raise ZeroDivisionError("Derivative is zero.")
        x -= fx / dfx
        steps += 1
    return x, steps

def compare_methods(f, df, a, b, x0, tol=1e-6):
    try:
        root_bisect, steps_bisect = bisection_method(f, a, b, tol)
    except Exception as e:
        root_bisect, steps_bisect = None, str(e)
    
    try:
        root_newton, steps_newton = newton_raphson_method(f, df, x0, tol)
    except Exception as e:
        root_newton, steps_newton = None, str(e)

    return {
        "Bisection Method": {"Root": root_bisect, "Steps": steps_bisect},
        "Newton-Raphson Method": {"Root": root_newton, "Steps": steps_newton},
    }


# Examples


# Function and its derivative
def f(x):
    return x**3 - 2*x - 5

def df(x):
    return 3*x**2 - 2



# Testing the newton raphson method
result = newton_raphson_method(f, df, x0=2.5)
print(result)



# Comparing bisection method to newton raphson method using a different value for initial iteration
result_compare = compare_methods(f, df, a=2, b=3, x0=2.5)
print(result_compare)
