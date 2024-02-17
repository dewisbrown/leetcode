"""
1. Two Sum

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
"""

def twoSum(nums: list[int], target: int) -> list[int]:
    """
    Returns the indices of two numbers whose sum is equal to the target.
    """
    m = {}
    n = len(nums)

    # Create dict where key=number in nums and value=index of number
    for i in range(n):
        m[nums[i]] = i

    # Iterate through array and check if the difference exists in the dict
    for i in range(n):
        diff = target - nums[i]
        if m.__contains__(diff) and m[diff] != i:
            return [i, m[diff]]

ex_in = [
    [[2,7,11,15], 9],
    [[3,2,4], 6],
    [[3,3], 6],
    [[2,5,5,11], 10]
]

ex_out = [
    [0,1],
    [1,2],
    [0,1],

]

for ex in ex_in:
    print(twoSum(ex[0], ex[1]))
