"""
150. Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents
an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""
def evalRPN(self, tokens: list[str]) -> int:
    stack = []
    return 0



ex_in = [
    ["2","1","+","3","*"], # ((2 + 1) * 3)
    ["4","13","5","/","+"],
    ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
]

# for ex in ex_in:
#     print(evalRPN(ex))
