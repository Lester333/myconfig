import random

rang = int(input("Number of elements: "))

random = [random.randint(1, rang) for _ in range(rang)]

arr=random.copy()

def makeshift_sort(array):
    result = []

    while array:
        minimum = min(array)
        maximum = max(array)
        result.append(minimum)
        result.append(maximum)
        array.remove(minimum)
        array.remove(maximum)

    return result
print(makeshift_sort(arr))
