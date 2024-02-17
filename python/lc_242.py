"""
242. Valid Anagram

Given two strings s and t, 
return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging 
the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""

def isAnagram(s: str, t: str) -> bool:
    """
    Checks if word 's' has the same letters as 't',
    regardless of arrangement.
    Uses HashMap method: key -> letter, value -> count.
    """
    s_dict = {}
    t_dict = {}

    for letter in s:
        if letter in s_dict.keys():
            s_dict[letter] += 1
        else:
            s_dict[letter] = 1
    
    for letter in t:
        if letter in t_dict.keys():
            t_dict[letter] += 1
        else:
            t_dict[letter] = 1

    return s_dict == t_dict


example_inputs = [
    ('anagram', 'nagaram'),
    ('rat', 'car')
]

example_outputs = [True, False]

for ex_input, ex_output in zip(example_inputs, example_outputs):
    print(ex_output == isAnagram(ex_input[0], ex_input[1]))
