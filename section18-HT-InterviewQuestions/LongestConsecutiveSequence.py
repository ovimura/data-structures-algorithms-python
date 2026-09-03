def longest_consecutive_sequence(arr):
    s = set(arr)
    if len(s) == 0:
        return 0
    m1 = min(s)
    m2 = max(s)
    longest = -1
    r = 0
    while m1<=m2:
        if m1 in s:
            r += 1
        else:
            r = 0
        longest = r if r > longest else longest
        m1 += 1
    return longest



print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""