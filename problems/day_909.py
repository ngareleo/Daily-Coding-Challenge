import unittest

"""
This problem was asked by Google.

Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. 
If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals is {3, 6}.
"""

a = [[3, 7], [6, 10], [4, 9], [11, 34]]
b = [[0, 3], [2, 6], [3, 4], [6, 9]]  # {3, 6}
c = [[0, 10]]  # {0, 1}
d = [[0, 3], [2, 5], [3, 4], [6, 9], [11, 20]]  # {3, 6}


def find_smallest_interval(arr: list) -> list:
    size = len(arr)
    if size == 1:
        return arr
    f, g = arr[0], arr[1]
    return find_smallest_interval(find_smallest_overlap(f, g) + arr[2:])


def find_smallest_overlap(a: [int, int], b: [int, int]) -> [int, int]:

    # [0, 3], [2, 5]
    seq = sorted([sorted(a), sorted(b)])
    low = seq[0][1]
    high = low + 1
    high = seq[1][1] if seq[1][0] <= low else seq[1][0]
    return [low, high]
