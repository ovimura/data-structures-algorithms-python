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
a.sort()
print(a)

b = sorted(a)

print(b)
print(bs(a, 5))

c = [(1, 4), (7, 11), (0, 1), (6, 2)]
c.sort(key=lambda x: x[0])
print(c)


d = {1: 'y'}
d[3] = "n"
print(d)
del d[1]
print(d)