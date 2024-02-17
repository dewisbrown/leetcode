"""
217. Contains Duplicate

Given an integer array nums, return true if any value 
appears at least twice in the array, 
and return false if every element is distinct.
"""

example_inputs = [
    [1,2,3,1],
    [1,2,3,4],
    [1,1,1,3,3,4,3,2,4,2],
]

example_outputs = [True, False, True]

def containsDuplicate(nums: list[int]) -> bool:
    """
    Checks for duplicates in array.
    """
    s = set()
    for num in nums:
        if num in s:
            return True
        s.add(num)
    return False


# Test example inputs
for nums, output in zip(example_inputs, example_outputs):
    print(output == containsDuplicate(nums))
