def sqrt_approx(n, tolerance=1e-10):
    if n < 0:
        return "Invalid result. Cannot compute square root of negative number."
    guess = n / 2
    while abs(guess * guess - n) > tolerance:
        guess = (guess + n / guess) / 2
    return guess

def calculate_expression(x, y):
    value = x**2 - y**2
    if value < 0:
        return "The result under the square root is negative."
    return sqrt_approx(value)

