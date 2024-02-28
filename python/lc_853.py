"""
853. Car Fleet

There are n cars going to the same destination along a one-lane road.
The destination is target miles away.

You are given two integer array position and speed, both of length n,
where position[i] is the position of the ith car and
speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it,
but it can catch up to it and drive bumper to bumper at the same speed.
The faster car will slow down to match the slower car's speed.
The distance between these two cars is ignored
(i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed.
Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point,
it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.
"""
def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    """
    Stack solution needed.
    """
    res = 0

    return res


ex_in = [
    {'target': 12, 'position': [10, 8, 9, 5, 3], 'speed': [2, 4, 1, 1, 3]},
    {'target': 10, 'position': [3], 'speed': [3]},
    {'target': 100, 'position': [0,2,4], 'speed': [4,2,1]}
]

ex_out = [3, 1, 1]

for i, o in zip(ex_in, ex_out):
    print(carFleet(i['target'], i['position'], i['speed']) == o)
