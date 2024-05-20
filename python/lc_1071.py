"""
For two strings s and t, we say "t divides s" if and only if 
s = t + t + t + ... + t + t 
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, 
return the largest string x such that x divides both str1 and str2.
"""
def gcdOfStrings(str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        from math import gcd
        return str1[:gcd(len(str1), len(str2))]
        

inputs = [
        ['ABCABC', 'ABC'],
        ['ABABAB', 'ABAB'],
        ['LEET', 'CODE']
]

outputs = [
        'ABC',
        'AB',
        ''
]

for i, o in zip(inputs, outputs):
        print(gcdOfStrings(i[0], i[1]) == o)
