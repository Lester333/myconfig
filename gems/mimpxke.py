def maxke(arr):
    res=[]
    while arr:
        maxim = max(arr)
        print(maxim)
        res.append(maxim)
        arr.remove(maxim)
    res.reverse()
    return res

print(maxke([1,5,3,7,5,3,567,35,7,4,6,3,65,24,67,876,1,1,2,2,3,3,4,21,3,123]))
