import math

# maximum iterations and tolerance
N_MAX = 500
TOL   = 1e-6

def fval(x):
    """Compute f(x) = 4x + sin(x) - exp(x).
    return 4*x + math.sin(x) - math.exp(x)

def dfval(x):
    """Compute f'(x) = 4 + cos(x) - exp(x)."""
    return 4 + math.cos(x) - math.exp(x)

def newton_raphson(f, df, x0, tol=TOL, max_iter=N_MAX):
    """
    Find a root of f using Newton–Raphson starting from x0.
    Prints iteration, x_k, f(x_k), and relative error each step.
    Returns (root, iterations).
    """
    xk = x0
    print("iter.\t      x_k\t\t   f(x_k)\t     rel. error")
    for k in range(1, max_iter+1):
        fxk = f(xk)
        dfxk = df(xk)
        if dfxk == 0:
            raise ZeroDivisionError(f"Zero derivative at x = {xk}, aborting.")
        
        x_next = xk - fxk/dfxk
        # avoid division by zero in error
        err = abs(x_next - xk) / abs(x_next) if x_next != 0 else abs(x_next - xk)
        
        print(f"{k:3d}\t {x_next:.16f}\t{f(x_next):.16f}\t{err:.12f}")
        
        if err < tol:
            print(f"\nConverged to {x_next:.12f} in {k} iterations.\n")
            return x_next, k
        
        xk = x_next

    raise RuntimeError(f"Did not converge within {max_iter} iterations.")

if __name__ == "__main__":
    # Example 1: start at x0 = 0.5
    print("Example 1: x0 = 0.5")
    root1, it1 = newton_raphson(fval, dfval, x0=0.5)

    # Example 2: start at x0 = 2.0
    print("Example 2: x0 = 2.0")
    root2, it2 = newton_raphson(fval, dfval, x0=2.0)
