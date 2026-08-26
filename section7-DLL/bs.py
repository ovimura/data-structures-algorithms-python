def bs(arr, t):
    l = 0
    r = len(arr)-1
    while l <= r:
        m = (r+l) // 2
        if arr[m] == t:
            return m
        elif arr[m] < t:
            l += 1
        else:
            r -= 1
    return -1


a = [1, 2, 3, 4, 5]

print(bs(a, 5))