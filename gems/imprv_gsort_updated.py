import random
import statistics
import time


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
            if arr[i] < arr[min_index]:
                min_index = i
            if arr[i] > arr[max_index]:
                max_index = i

        arr[left], arr[min_index] = arr[min_index], arr[left]
        arr[right], arr[max_index] = arr[max_index], arr[right]

        left += 1
        right -= 1

    return arr

def merge_sort(arr):
    n = len(arr)
    source = arr.copy()
    target = [None] * n

    width = 1

    while width < n:
        for left in range(0, n, width * 2):
            mid = min(left + width, n)
            right = min(left + width * 2, n)

            i, j, k = left, mid, left

            while i < mid and j < right:
                if source[i] <= source[j]:
                    target[k] = source[i]
                    i += 1
                else:
                    target[k] = source[j]
                    j += 1
                k += 1

            while i < mid:
                target[k] = source[i]
                i += 1
                k += 1

            while j < right:
                target[k] = source[j]
                j += 1
                k += 1

        source, target = target, source
        width *= 2

    return source

def timsort(arr):
    return sorted(arr)

# ==========================
# Input helpers
# ==========================

def get_positive_int(prompt, default=None):
    while True:
        value = input(prompt).strip()

        if not value and default is not None:
            return default

        try:
            value = int(value)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if value > 0:
            return value

        print("Please enter a number greater than zero.")


def choose_input_type():
    options = {
        "1": "Random",
        "2": "Sorted",
        "3": "Reverse",
        "4": "Duplicate",
        "5": "All",
    }

    print("\n========== INPUT DATA TYPE ==========")
    print("1. Random    - randomly ordered values")
    print("2. Sorted    - already sorted values")
    print("3. Reverse   - reverse-sorted values")
    print("4. Duplicate - many repeated values")
    print("5. All       - benchmark all four types")

    while True:
        choice = input("Choose input type [1-5]: ").strip()

        if choice in options:
            return options[choice]

        print("Invalid choice. Enter a number from 1 to 5.")


# ==========================
# User configuration
# ==========================

n = get_positive_int("Number of elements: ")
runs = get_positive_int("Benchmark repetitions [5]: ", default=5)
input_type = choose_input_type()


# ==========================
# Array generation
# ==========================

# Sorted and Reverse use the same values as Random, but in a different order.
random_data = [random.randint(1, n) for _ in range(n)]

# Use a small value range to create many duplicates (about 5% of n values).
duplicate_range = max(1, n // 20)

all_datasets = {
    "Random": random_data,
    "Sorted": sorted(random_data),
    "Reverse": sorted(random_data, reverse=True),
    "Duplicate": [random.randint(1, duplicate_range) for _ in range(n)],
}

if input_type == "All":
    selected_datasets = list(all_datasets)
else:
    selected_datasets = [input_type]

expected_results = {
    dataset_name: sorted(all_datasets[dataset_name])
    for dataset_name in selected_datasets
}


# ==========================
# Benchmark configuration
# ==========================

algorithms = [
    ("Makeshift Sort", makeshift_sort),
    ("Selection Sort", selection_sort),
    ("Double Selection", d_selection_sort),
    ("Merge Sort", merge_sort),
    ("Timsort", timsort)
]

# Store separate timings for every algorithm and input type.
results = {
    name: {dataset_name: [] for dataset_name in selected_datasets}
    for name, _ in algorithms
}

# In All mode, also store the sum of the four sorting times for each run.
total_results = {name: [] for name, _ in algorithms}


# ==========================
# Benchmark
# ==========================

for run in range(runs):
    # Randomize which algorithm runs first to reduce order bias.
    current_algorithms = algorithms.copy()
    random.shuffle(current_algorithms)

    for name, function in current_algorithms:
        combined_time = 0.0

        # In All mode, each algorithm sorts all four datasets consecutively.
        for dataset_name in selected_datasets:
            # Copying happens before the timer, so preparation is not measured.
            data = all_datasets[dataset_name].copy()

            start = time.perf_counter()
            result = function(data)
            elapsed = time.perf_counter() - start

            # Correctness checks are deliberately outside the timed section.
            if result != expected_results[dataset_name]:
                raise RuntimeError(
                    f"{name} produced an incorrect result for {dataset_name}!"
                )

            results[name][dataset_name].append(elapsed)
            combined_time += elapsed

        total_results[name].append(combined_time)


# ==========================
# Results
# ==========================

def print_stats(times):
    print(f"  Median: {statistics.median(times):.8f} s")
    print(f"  Mean:   {statistics.mean(times):.8f} s")
    print(f"  Min:    {min(times):.8f} s")


print("\n========== BENCHMARK RESULTS ==========")
print(f"Elements: {n}")
print(f"Repetitions: {runs}")
print(f"Input type: {input_type}")

for dataset_name in selected_datasets:
    print(f"\n--- {dataset_name} ---")

    for name, _ in algorithms:
        print(f"{name}:")
        print_stats(results[name][dataset_name])

if input_type == "All":
    print("\n--- Combined time (all four datasets) ---")
    print("Sum of the four sorting times in each run:")

    for name, _ in algorithms:
        print(f"{name}:")
        print_stats(total_results[name])
