# These approximations for the trig and exponential functions only work for moderate values

# Approximate sin(x) using Taylor series
def sin(x, terms=10):
    result = 0
    sign = 1
    for n in range(terms):
        term = x**(2*n+1) / factorial(2*n+1)
        result += sign * term
        sign *= -1
    return result

# Approximate cos(x) using Taylor series
def cos(x, terms=10):
    result = 0
    sign = 1
    for n in range(terms):
        term = x**(2*n) / factorial(2*n)
        result += sign * term
        sign *= -1
    return result

# Approximate exp(x) using Taylor series
def exp(x, terms=20):
    result = 0
    for n in range(terms):
        result += x**n / factorial(n)
    return result

# Custom factorial function
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# Function and its derivative
def fval(x):
    return 4*x + sin(x) - exp(x)

def dfval(x):
    return 4 + cos(x) - exp(x)

# Newton-Raphson method
def newton_raphson(f, df, x0, tol=1e-6, max_iter=500):
    xk = x0
    print("iter.\t      x_k\t\t   f(x_k)\t     rel. error")
    for k in range(1, max_iter+1):
        fxk = f(xk)
        dfxk = df(xk)
        if dfxk == 0:
            print("Zero derivative. Stopping.")
            return None
        x_next = xk - fxk/dfxk
        err = abs(x_next - xk) / abs(x_next) if x_next != 0 else abs(x_next - xk)
        print(f"{k:3d}\t {x_next:.16f}\t{f(x_next):.16f}\t{err:.12f}")
        if err < tol:
            print(f"\nConverged to {x_next:.12f} in {k} iterations.\n")
            return x_next
        xk = x_next
    print("Did not converge.")
    return None


# Run an example
x0 = float(input("Enter initial guess: "))
newton_raphson(fval, dfval, x0)
