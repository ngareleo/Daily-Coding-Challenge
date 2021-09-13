#This problem was asked by Uber.
#Given an array of integers
# return a new array such that each element at index i of the new array is the product of all the numbers in the original array
# except the one at i.
#For example, if our input was [1, 2, 3, 4, 5],
#the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Sample_one = [ 1, 2, 3, 4, 5]
Sample_two = [3,2,1]

def reduce_array(array):
    
    temp = 1
    answer_array = []
    for i in range(len(array)):
        for j in range(len(array)):
            if i == j:
                pass
            else:
                temp *= array[j]
        answer_array.append(temp)
        temp = 1
    return answer_array
            
"""
I know I could use the functools.reduce() function but its fun to make mine
"""
print(reduce_array(Sample_one))
