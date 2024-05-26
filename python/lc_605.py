"""
You have a long flowerbed in which some of the plots are planted, 
and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, 
where 0 means empty and 1 means not empty, and an integer n, 
return true if n new flowers can be planted in the flowerbed 
without violating the no-adjacent-flowers rule and false otherwise.
"""
def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    # Edge cases
    if n == 0:
        return True
    if len(flowerbed) == 0:
        return False
    if len(flowerbed) == 1:
        return flowerbed[0] == 0

    # Not optimal solution, but works
    m = len(flowerbed)
    l = 0
    r = 0
    count = 0
    while l < m:
        if l == r:
            r += 1
            continue
        # Check right neighbor of 1st element
        if l == 0:
            if flowerbed[l] == 0 and flowerbed[r] == 0:
                count += 1
                flowerbed[l] = 1
        # Check left neighbor of last element
        elif l == m - 1:
            if flowerbed[l] == 0 and flowerbed[l - 1] == 0:
                count += 1
                flowerbed[l] = 1
        # Check left and right neighbor or an element
        else:
            if flowerbed[l - 1] == 0 and flowerbed[l] == 0 and flowerbed[r] == 0:
                count += 1
                flowerbed[l] = 1
        l += 1
    return count >= n

inputs = [
    [[1,0,0,0,1], 1],
    [[1,0,0,0,1], 2],
]

outputs = [True, False]

for i, o in zip(inputs, outputs):
    print(canPlaceFlowers(i[0], i[1]) == o)
