import time  #Used to measure how long an operation takes.
import matplotlib.pyplot as plt  #Used for plotting graphs
import math  #Provides mathematical functions like sqrt() for primality testing.

# Efficient cube root finder using binary search
def cube_root(n):
    start_time = time.time() #start timing
    steps = 0 #step counter
    is_negative = n < 0 #check if number is negative
    n = abs(n) #work with the absolute value

    low, high = 0, n
    if n < 1:
        high = 1 # Edge case for small positive numbers like 0.1

    # Binary search for cube root
    while high - low > 1e-6:  # Stop when precision is good enough
        steps += 1
        mid = (low + high) / 2
        if mid**3 > n:
            high = mid  # Too high
        else:
            low = mid   # Too low or just right

    duration = time.time() - start_time
    result = -low if is_negative else low  # Flip result if original was negative
    return result, steps, duration

# Testing cube root for increasing number sizes
def test_cube_root():
    digit_counts = range(1, 11)  # Test for 1-digit to 10-digit numbers
    steps_list = []
    times_list = []

    for digits in digit_counts:
        number = int('9' * digits)  # e.g., 9, 99, 999, etc.
        _, steps, duration = cube_root(number)
        steps_list.append(steps)
        times_list.append(duration)

    # Graph: steps vs number of digits
    plt.figure(figsize=(12, 5))  #creates a side-by-side plot.
    plt.subplot(1, 2, 1)
    plt.plot(digit_counts, steps_list, marker='o')
    plt.title("Steps vs Digits (Cube Root)")
    plt.xlabel("Number of Digits")
    plt.ylabel("Steps")  #Shows how many steps the algorithm takes as the number of digits increases.

    # Graph: time vs number of digits
    plt.subplot(1, 2, 2)
    plt.plot(digit_counts, times_list, marker='o', label="Python")
    # Placeholder comparison: simulated C time (faster by ~10x)
    plt.plot(digit_counts, [t / 10 for t in times_list], marker='x', label="C (estimated)")
    plt.title("Time vs Digits (Cube Root)")
    plt.xlabel("Number of Digits")
    plt.ylabel("Time (s)")
    plt.legend()  #Shows execution time in Python.
    plt.tight_layout()
    plt.show()

# Efficient primality test
def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True  #Uses trial division up to the square root of n.
                 #Skips even numbers after 2 for efficiency.


# Test primality and sum primes
def test_primality():
    start_time = time.time()
    prime_sum = 0
    for i in range(3, 1001):
        if is_prime(i):
            prime_sum += i   #Runs is_prime() for all numbers from 3 to 1000.
                             #Sums all primes found.

  
    print(f"Sum of primes between 3 and 1000: {prime_sum}")
    duration = time.time() - start_time
    print(f"Time taken (Python): {duration:.6f} seconds")
    print(f"Estimated C time: {duration/10:.6f} seconds")  # Assuming ~10x faster in C

# Run all tests
if __name__ == "__main__":
    test_cube_root()
    test_primality()
