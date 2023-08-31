"""
This problem was asked by Yahoo.
Write a function that returns the bitwise AND of all integers between M and N, inclusive.
"""


def bitwise(m, n):
    # numbers between m and n
    nums = [i for i in range(m + 1, n)]
    res = nums[0]
    for i in range(1, len(nums)):
        res = res & nums[i]
    return res


if __name__ == '__main__':
    bitwise(10, 20)
