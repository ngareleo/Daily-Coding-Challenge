#This problem was asked by Uber.

#Given an array of integers
# return a new array such that each element at index i of the new array is the product of all the numbers in the original array
# except the one at i.

#For example, if our input was [1, 2, 3, 4, 5],
#the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].


Sample_one = [ 1, 2, 3, 4, 5]
Sample_two = [3,2,1]

def reduce(array):
    sp = 0 #Starting point
    r = len(array)
    result = 1
    while ( sp <= r - 1):
        result *= array[sp]
        sp += 1
    return result

def exclude(array):
    sp = 0 #Starting point
    answer = []
    while (sp <= len(array)- 1):
        new_array = [ number for number in array if number != array[sp]] #Remove the number at i
        answer.append(reduce(new_array))
        sp += 1
    return answer


"""
I know I could use the functools.reduce() function but its fun to make mine
"""
print(exclude(Sample_one))
