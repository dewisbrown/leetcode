"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, 
return the k most frequent elements. 
You may return the answer in any order.
"""
def topKFrequent(nums: list[int], k: int) -> list[int]:
    """
    Using a map to keep count of occurences of each number,
    create a list of lists where the index is equal to the frequency 
    of a number, and the list at the index is which numbers occur 
    at that frequency in nums.
    """
    mp = {}

    # Create list of n + 1 (0 -> n) empty lists
    buckets = [[] for i in range(len(nums) + 1)]

    # Count occurences of each number in nums
    for n in nums:
        mp[n] = 1 + mp.get(n, 0)

    # Add number to list at index == occurence count
    for n, c in mp.items():
        buckets[c].append(n)

    # Iterate over buckets in reverse order and add to ans list
    ans = []
    for i in range(len(nums), 0, -1):
        # If buckets[i] is empty, loop will continue to next index
        for n in buckets[i]:
            ans.append(n)
            if len(ans) == k:
                return ans

ex_in = [
    [[1,1,1,2,2,3], 2],
    [[1], 1]
]

for ex in ex_in:
    print(topKFrequent(ex[0], ex[1]))
