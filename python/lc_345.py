"""
345. Reverse Vowels of a String

Given a string s, 
reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', 
and they can appear in both lower and upper cases, more than once.
"""
def reverseVowels(s: str) -> str:
    vowels = [
        'a', 'e', 'i', 'o', 'u',
        'A', 'E', 'I', 'O', 'U'
    ]
    m = []
    for letter in s:
        if letter in vowels:
            m.append(letter)
    
    # Stack solution
    res = ''
    for letter in s:
        if letter in vowels:
            res += m.pop()
        else:
            res += letter
    
    return res


ins = [
    'hello',
    'leetcode'
]

outs = [
    'holle',
    'leotcede'
]

for i, o in zip(ins, outs):
    print(reverseVowels(i) == o)
