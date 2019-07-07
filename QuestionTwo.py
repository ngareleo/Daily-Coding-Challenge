#This problem was asked by Uber.

#Given an array of integers,

#return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]

#If our input was [3, 2, 1], the expected output would be [2, 3, 6].

from functools import reduce

the_list = [1,2,3,4,5]

expected_output = []



current_index = 0

while current_index < len(the_list):

    new_ls = [ element for element in the_list if element != the_list[current_index]]

    products = reduce(lambda a , b : a * b , new_ls)

    expected_output.append(products)

    current_index+=1

print(expected_output)

