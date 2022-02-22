"""
This problem was asked by Google.

Given an array of integers
Return a new array where each element in the new array is the number of smaller elements
To the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1
"""

arr = [3, 4, 9, 6, 1]
ret = []
for c, i in enumerate(arr):
    count = 0
    for j in arr[c + 1:]:
        if j < i:
            count += 1

    ret.append(count)
print(ret)

