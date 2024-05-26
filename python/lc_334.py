"""
334. Increasing Triplet Subsequence

Given an integer array nums,
return true if there exists a triple of indices (i, j, k) 
such that i < j < k and nums[i] < nums[j] < nums[k].

If no such indices exists, return false.
"""
def increasingTriplet(nums: list[int]) -> bool:
    return False

ins = [
    [1,2,3,4,5],
    [5,4,3,2,1],
    [2,1,5,0,4,6]
]

outs = [
    True, False, True
]

for i, o in zip(ins, outs):
    print(increasingTriplet(i) == o)
