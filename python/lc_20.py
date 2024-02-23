"""
20. Valid Parenthesis

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.
"""
def isValid(s: str) -> bool:
    """
    Uses stack to check for valid parenthesis.
    """
    para = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = []

    for c in s:
        if c in para.keys() and len(stack) == 0:
            return False
        elif c in para.values():
            stack.append(c)
        elif stack.pop() != para[c]:
            return False
    if len(stack) > 0:
        return False
    return True

ex_in = [
    '()',
    '()[]{}',
    '(]',
    '){'
]

for ex in ex_in:
    print(isValid(ex))
