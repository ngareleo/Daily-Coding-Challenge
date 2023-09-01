"""
This problem was asked by Google.

Given a set of points (x, y) on a 2D cartesian plane, find the two closest points. 
For example, given the points [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)], return [(-1, -1), (1, 1)]
"""

from .day_888 import find_distance
globals = {
    "a": {
        "1": [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)],
        "2": [(-1, -1), (1, 1)]
    }
}


def find_2_closest_points(arr: list) -> list:
    if len(arr) < 2:
        raise ValueError("Size of arr should be 2 or more")

    closest = [arr[0], arr[1]]
    d = find_distance(closest[0], closest[1])

    for i, point in enumerate(arr):
        for rest in arr[i+1:]:
            if find_distance(point, rest) < d:
                closest = [point, rest]

    return closest
