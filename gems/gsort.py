import time
import random
import sort
import ssort


rang = int(input("Number of elements: "))
runs = 10

original = [random.randint(1, rang) for _ in range(rang)]

def benchmark(function, arr):
    times = []

    for _ in range(runs):
        data = arr.copy()

        start = time.perf_counter()
        function(data)
        end = time.perf_counter()

        times.append(end - start)

    return sum(times) / len(times)


t1 = benchmark(sort.sorting, original)
t2 = benchmark(ssort.selection_sort, original)

print(f"Makeshift sorting:   {t1:.8f} seconds")
print(f"Selection sort:   {t2:.8f} seconds")
