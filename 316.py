"""
This problem was asked by Snapchat.

You are given an array of length N, where each element i represents the number of ways we can produce i units of change.
For example, [1, 0, 1, 1, 2] would indicate that there is only one way to make 0, 2, or 3 units, and two ways of making 4 units.

Given such an array, determine the denominations that must be in use.
In the case above, for example, there must be coins with value 2, 3, and 4.
"""


def units_of_denom(arr):
    single_units = [i for i in range(len(arr)) if arr[i] == 1 and i != 0]
    missing_units = [j for j in range(len(arr)) if arr[j] != 1 and arr[j] != 0 and j != 0]
    for unit in missing_units:
        # we look for ways to make the unit and compare
        pass
    return single_units


def least_coins(coins: list, n):
    temp = 0
    for coin in sorted(coins, reverse=True):
        temp += n // coin
        n %= coin
        if n == 0:
            break
    return temp


if __name__ == '__main__':
    print(units_of_denom([1, 0, 1, 1, 2]))
    print(least_coins([1, 5, 10], 89))