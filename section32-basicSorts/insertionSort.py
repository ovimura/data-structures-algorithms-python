def insertion_sort(arr):
    for i in range(1, len(arr)):
        t = arr[i]
        j = i-1
        while t < arr[j] and j >= 0:
            arr[j+1] = arr[j]
            arr[j] = t
            j -= 1
    return arr



print(insertion_sort([4,2,6,5,1,3]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """

