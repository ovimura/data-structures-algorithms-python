
def subarray_sum(nums, target):
    prefix_sums = {0: -1}
    s = 0
    for i, v in enumerate(nums):
        s += v
        q = s - target
        if q in prefix_sums.keys():
            print(q, ":", prefix_sums[q])
            return [prefix_sums[q]+1, i]
        if s not in prefix_sums.keys():
            prefix_sums[s] = i
    return []


nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""

