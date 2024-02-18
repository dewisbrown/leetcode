"""
238. Product of Array Except Self

Given an integer array nums, return an array answer 
such that answer[i] is equal to the product 
of all the elements of nums except nums[i].

The product of any prefix or suffix of nums 
is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time 
and without using the division operation.
"""
def productExceptSelf(nums: list[int]) -> list[int]:
    """
    
    """
    n = len(nums)
    res = [0] * n
    prefix = 1
    postfix = 1

    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    
    for i in range((n - 1), -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res


ex_in = [
    [1,2,3,4],
    [-1,1,0,-3,3]
]

for ex in ex_in:
    print(productExceptSelf(ex))
