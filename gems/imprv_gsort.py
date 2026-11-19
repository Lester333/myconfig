import time
import random
import statistics


# ==========================
# Sorting algorithms
# ==========================

def makeshift_sort(arr):
    result = []

    while arr:
        minimum = min(arr)
        result.append(minimum)
        arr.remove(minimum)

    return result


def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

def d_selection_sort(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        min_index, max_index = left, right
        if arr[min_index] > arr[max_index]:
            arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
        for i in range(left + 1, right):
            if arr[i] < arr[min_index]: min_index = i
            if arr[i] > arr[max_index]: max_index = i
        arr[left], arr[min_index] = arr[min_index], arr[left]
        arr[right], arr[max_index] = arr[max_index], arr[right]
        left += 1
        right -= 1
    return arr


# ==========================
# User configuration
# ==========================

n = int(input("Number of elements: "))

runs_input = input("Benchmark repetitions [5]: ").strip()
runs = int(runs_input) if runs_input else 5

if n <= 0 or runs <= 0:
    raise ValueError("Both values must be positive integers.")


# ==========================
# Array generation
# ==========================

original = [random.randint(1, n) for _ in range(n)]

# Reference result for correctness verification
expected = sorted(original)


# ==========================
# Benchmark
# ==========================

algorithms = [
    ("Makeshift Sort", makeshift_sort),
    ("Selection Sort", selection_sort),
    ("Double Selection", d_selection_sort)
]

results = {
    name: [] for name, _ in algorithms
}

for run in range(runs):

    # Randomize algorithm execution order
    current_algorithms = algorithms.copy()
    random.shuffle(current_algorithms)

    for name, function in current_algorithms:

        # Prepare input outside the timed section
        data = original.copy()

        start = time.perf_counter()
        result = function(data)
        end = time.perf_counter()

        elapsed = end - start

        # Verify correctness outside the timed section
        if result != expected:
            raise RuntimeError(f"{name} produced an incorrect result!")

        results[name].append(elapsed)


# ==========================
# Results
# ==========================

print("\n========== BENCHMARK RESULTS ==========")
print(f"Elements: {n}")
print(f"Repetitions: {runs}\n")

for name, times in results.items():

    print(f"{name}:")
    print(f"  Median: {statistics.median(times):.8f} s")
    print(f"  Mean:   {statistics.mean(times):.8f} s")
    print(f"  Min:    {min(times):.8f} s")
    print()
