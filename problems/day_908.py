"""
This problem was asked by Google.

You are given an N by M 2D matrix of lowercase letters. 
Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically. 
That is, the letter at each column is lexicographically later as you go down each row. It does not matter whether each row itself is ordered lexicographically.

For example, given the following table:

cba
daf
ghi
This is not ordered because of the a in the center. We can remove the second column to make it ordered:

ca
df
gi
So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

abcdef
Your function should return 0, since the rows are already ordered (there's only one row).

As another example, given the following table:

zyx
wvu
tsr
Your function should return 3, since we would need to remove all the columns to order it.

"""

globals = {
    "a": [
        ['c', 'b', 'a'],
        ['d', 'a', 'f'],
        ['g', 'h', 'i'],
    ],
    "b": [['a', 'b', 'c', 'd', 'e', 'f']],
    "c": [
        ['z', 'y', 'x'],
        ['w', 'v', 'u'],
        ['t', 's', 'r']
    ]
}


def get_column(arr: list, i: int) -> list:
    if len(arr) == 0:
        raise ValueError("invalid_arr")
    elif i < 0:
        raise ValueError("i cannot be signed")
    elif i >= len(arr[0]):
        raise ValueError("i is larger than arr")
    return [row[i] for row in arr]


def count_disordered_cols(arr: list) -> int:
    if len(arr) == 0:
        return 0
    columns = [get_column(arr, i) for i, _ in enumerate(arr[0])]
    return len([col for col in columns if col != sorted(col)])
