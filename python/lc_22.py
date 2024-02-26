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
    backtrack(n, 0, 0, stack, ans)
    return ans

# Add contents of stack when open and closed parentheses counts
# are equal to n.
#
# Conditions for adding parentheses:
# - Add open parentheses if open count is less than n.
# - Add closed parentheses if closed count is less than open count.
#
# Backtrack by popping the character after the recursive call.
def backtrack(n: int, open_count: int, closed_count: int, stack: list[str], ans: list[list[str]]) -> None:
    if open_count == n and closed_count == n:
        # add contents of stack to result list
        ans.append(stack)
        stack.clear()
        return

    if open_count < n:
        stack.append('(')
        backtrack(n, open_count + 1, closed_count, stack, ans)

    if closed_count < n:
        stack.append(')')
        backtrack(n, open_count, closed_count + 1, stack, ans)


ex_in = [3, 1]
for ex in ex_in:
    print(generateParenthesis(ex))
