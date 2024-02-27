"""
739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days 
you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    """
    Iterate temperatures in reverse, use stack to keep count of
    next warmer day.
    """
    n = len(temperatures)
    stack = []
    res = [0] * n

    for i in range(n - 1, -1, -1):
        while stack and temperatures[i] >= temperatures[stack[-1]]:
            stack.pop()

        if stack:
            res[i] = stack[-1] - i

        stack.append(i)

    return res


ex_in = [
    [73,74,75,71,69,72,76,73],
    [30,40,50,60],
    [30,60,90]
]

ex_out = [
    [1,1,4,2,1,1,0,0],
    [1,1,1,0],
    [1,1,0]
]

for ex, ex_o in zip(ex_in, ex_out):
    print(dailyTemperatures(ex) == ex_o)
