"""
151. Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces
or multiple spaces between two words.

The returned string should only have a single space separating the words.
Do not include any extra spaces.
"""
def reverseWords(s: str) -> str:
    # s.split()      -> Split s by whitespace
    # [::-1]        -> reverse list
    # ' '.join()    -> build string with space 
    #                  in between each element of string list
    return ' '.join(s.split()[::-1])

ins = [
    "the sky is blue",
    "  hello world  ",
    "a good   example"
]

outs = [
    "blue is sky the",
    "world hello",
    "example good a"
]

for i, o in zip(ins, outs):
    print(reverseWords(i) == o)
