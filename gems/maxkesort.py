def maxkeshift_sort(arr):
    result = []

    while arr:
        maximum = max(arr)
        result.append(maximum)
        arr.remove(maximum)

    return result[::-1]

print(maxkeshift_sort([1,5,3,5,356,76,24,764,546,645,654,35,234,556,8,4,6,4,6,5,6,3,6,3,5,6,7,7,5,4,2,45,736,8265,286,5268,865,56,86,86,5682,286,2865,286,268,2865,268,568,56,345,435,345,2,25]))
