def selection_sort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < min_idx:
                min_idx = j
        if i != min_idx:
            t = arr[j]
            arr[i] = arr[min_idx]
            arr[min_idx] = t
    return arr


print(selection_sort([4,2,6,5,1,3]))

 

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """

