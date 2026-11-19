
import time

def makeshift(arr):
    result = []
    while arr:
        minimum = min(arr)
        result.append(minimum)
        arr.remove(minimum)
    return result

arr = list(range(5000, 0, -1))

start = time.perf_counter()
arr = makeshift(arr)
end = time.perf_counter()

print(f"Python: {end - start:.6f} seconds")

