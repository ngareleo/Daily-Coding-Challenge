#This problem was asked by Stripe.

#Given an array of integers, find the first missing positive integer in linear time and constant space

#In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

def find_missing_number(array):

    sorted_array = sorted([ number for number in array if number > 0]) #Removes all negative numbers

    perfect_array = list(range(1,sorted_array[-1]+1))  # forms a list of all the numbers in to the largest integer so that we compare the two lists

    missing_numbers = []  #A list of all the missing postive numbers in the array
    """ The for loop below compares the two lists : The perfect one 
    and the one with missing numbers 
    """
    for i in perfect_array:
        if i not in sorted_array:
            missing_numbers.append(i)

    if len(missing_numbers) == 0: #This will happen if the array consists of all the numbers from 0 and i then the least integer will be i+1
        return perfect_array[-1]+1
    else:
        return missing_numbers[0]  #Returns all the least number in the missing numbers array

print(find_missing_number([3,4,5,2]))