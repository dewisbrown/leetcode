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

    return [0]


ex_in = [
    [1,2,3,4],
    [-1,1,0,-3,3]
]

for ex in ex_in:
    print(productExceptSelf(ex))
