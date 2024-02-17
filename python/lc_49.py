"""
49.  Group Anagrams

Given an array of strings strs, 
group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging 
the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""
from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    """
    Create a key in a map using the sorted string.
    The value of the key is a list of strings with the same 
    sorted string.

    Example:
    {
        'aet': ['eat', 'tea', 'ate'],
        'ant': ['tan', 'nat'],
        'abt': ['bat']
    }
    """
    mp = defaultdict(list)

    for s in strs:
        _sorted = ''.join(sorted(s))
        if _sorted in mp:
            mp[_sorted].append(s)
        else:
            mp[_sorted] = [s]

    return list(mp.values())

ex_in = [
    ["eat","tea","tan","ate","nat","bat"],
    [""],
    ["a"]
]

for ex in ex_in:
    print(groupAnagrams(ex))
