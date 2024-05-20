"""
There are n kids with candies. You are given an integer array candies, 
where each candies[i] represents the number of candies the ith kid has, 
and an integer extraCandies, 
denoting the number of extra candies that you have.

Return a boolean array result of length n, 
where result[i] is true if, 
after giving the ith kid all the extraCandies, 
they will have the greatest number of candies among all the kids, 
or false otherwise.

Note that multiple kids can have the greatest number of candies.
"""
def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    res = []
    for i in range(len(candies)):
        candies[i] += extraCandies
        if candies[i] == max(candies):
            res.append(True)
        else:
            res.append(False)
        candies[i] -= extraCandies
    return res

def kidsWithCandies_betterSolution(candies: list[int], extraCandies: int) -> list[bool]:
    res = []
    max_candies = max(candies)
    for candy in candies:
        if candy + extraCandies >= max_candies:
            res.append(True)
        else:
            res.append(False)
    return res

inputs = [
    [[2,3,5,1,3], 3],
    [[4,2,1,1,2], 1],
    [[12,1,12], 10]
]

outputs = [
    [True,True,True,False,True],
    [True,False,False,False,False],
    [True,False,True]
]

for i, o in zip(inputs, outputs):
    print(kidsWithCandies_betterSolution(i[0], i[1]) == o)
