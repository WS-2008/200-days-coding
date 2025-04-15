def nth_root(x, n, precision=0.00001):
    if x < 0 and n % 2 == 0:
        return "The given number doesn't have an even root."
    
    low = 0
    high = max(1, x)
    
    guess = (low + high) / 2
    while abs(guess**n - x) > precision:
        if guess**n < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
    
    return guess

