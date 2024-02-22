"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums,
return the length of the longest consecutive
elements in sequence.

You must write an algorithm that runs in O(n) time.
"""
def longestConsecutive(nums: list[int]) -> int:
    nums_set = set(nums)
    longest = 0

    for n in nums:
        # check if n is the start of a sequence (checks if number has a left neighbor)
        if (n - 1) not in nums_set:
            length = 0
            # count sequence of numbers from there (look for right neighbors continuously)
            while n + length in nums_set:
                length += 1
            longest = max(length, longest)

    return longest

ex_in = [
    [0,3,7,2,5,8,4,6,0,1],
    [100,4,200,1,3,2]
]

for ex in ex_in:
    print(longestConsecutive(ex))
