import random
import time

# ─── 1. Generate 1 000 Sensor Data Points ────────────────────────────────────────
def generate_sensor_data(n=1000, low=0.0, high=100.0):
    """Return a list of n random floats between low and high."""
    return [random.uniform(low, high) for _ in range(n)]

sensor_data = generate_sensor_data(1000)
search_target = sensor_data[random.randint(0, len(sensor_data)-1)]

# ─── 2. Sorting Algorithms ───────────────────────────────────────────────────────

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

def merge_sort(arr):
    a = arr.copy()
    if len(a) <= 1:
        return a
    mid = len(a)//2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]; i += 1
        else:
            a[k] = right[j]; j += 1
        k += 1
    while i < len(left):
        a[k] = left[i]; i += 1; k += 1
    while j < len(right):
        a[k] = right[j]; j += 1; k += 1
    return a

def quick_sort(arr):
    # Uses extra memory but nice one-liner style
    if len(arr) <= 1:
        return arr.copy()
    pivot = arr[len(arr)//2]
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

# ─── 3. Searching Algorithms ────────────────────────────────────────────────────

def linear_search(arr, target):
    for idx, val in enumerate(arr):
        if val == target:
            return idx
    return -1

def binary_search(arr, target):
    a = arr.copy()
    low, high = 0, len(a)-1
    while low <= high:
        mid = (low + high)//2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# ─── 4. Performance Testing ─────────────────────────────────────────────────────

def time_function(fn, *args, repeats=1):
    """Return average runtime of fn(*args) over given repeats."""
    total = 0.0
    for _ in range(repeats):
        start = time.time()
        fn(*args)
        total += (time.time() - start)
    return total / repeats

def test_sorting(data):
    print("Sorting Performance on 1 000 sensor readings:")
    for sort_fn in [bubble_sort, insertion_sort, merge_sort, quick_sort]:
        t = time_function(sort_fn, data, repeats=3)
        print(f" • {sort_fn.__name__:13s}: {t:.5f} s")

def test_searching(data, target):
    print("\nSearching Performance (looking for one random reading):")
    t_lin = time_function(linear_search, data, target, repeats=10)
    print(f" • linear_search : {t_lin:.6f} s")
    sorted_data = sorted(data)
    t_bin = time_function(binary_search, sorted_data, target, repeats=10)
    print(f" • binary_search : {t_bin:.6f} s")

if __name__ == "__main__":
    test_sorting(sensor_data)
    test_searching(sensor_data, search_target)

