"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10,
since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


n = [2, 4, 6, 2, 5]
n_2 = [2, 3, 5, -5, 8, 9]
n_3 = [2, 5, 7, 8, -10, 3, 9, 9, 10]
# with 0(n ^ 2)


def non_adjacent_sums(arr, temp=[]):
    clean_arr = [arr[i] for i in range(len(arr)) if i not in temp]
    if len(clean_arr) == 0:
        return 0
    large = sorted(clean_arr)[-1]
    in_large = arr.index(large)
    temp.append(in_large)
    temp.append(in_large + 1)
    temp.append(in_large - 1)
    return large + non_adjacent_sums(arr, temp)


if __name__ == '__main__':
    print(non_adjacent_sums(n_3))