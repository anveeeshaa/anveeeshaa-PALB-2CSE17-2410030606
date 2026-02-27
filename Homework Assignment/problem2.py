def min_max(arr):
    mn = arr[0]
    mx = arr[0]
    
    for x in arr:
        if x < mn:
            mn = x
        if x > mx:
            mx = x
            
    return [mn, mx]

arr = [1, 4, 3, 5, 8, 6]
print(min_max(arr))
