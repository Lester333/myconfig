def main(arr):
    result = []

    while arr:
        minimum = min(arr)
        result.append(minimum)
        arr.remove(minimum)
    
    arr=result
    return arr

if __name__ == "__main__":
    print(main([9,8,7,6,5,4,3,2,1]))
