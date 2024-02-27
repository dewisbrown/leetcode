"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to 
generate all combinations of well-formed parentheses.
"""
def generateParenthesis(n: int) -> list[str]:
    """
    Use backtracking.
    """
    stack = []
    ans = []

    def backtrack(o, c):
        if o == c == n:
            ans.append(''.join(stack))
            return

        if o < n:
            stack.append('(')
            backtrack(o + 1, c)
            stack.pop()

        if c < o:
            stack.append(')')
            backtrack(o, c + 1)
            stack.pop()

    backtrack(0, 0)
    return ans

# Add contents of stack when open and closed parentheses counts
# are equal to n.
#
# Conditions for adding parentheses:
# - Add open parentheses if open count is less than n.
# - Add closed parentheses if closed count is less than open count.
#
# Backtrack by popping the character after the recursive call.

ex_in = [3, 1]
for ex in ex_in:
    print(generateParenthesis(ex))
