#This problem was recently asked by Google.

#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
my_list = [10,15,3,7]

k = 17

from itertools import combinations 
from functools import reduce


two_number_lists = [lists for lists in combinations(my_list,2)] #This is a two number long list of all possible lists of combinations using the combinations function returns all possible

for i in enumerate(two_number_lists): #enumarate gives ability to keep count of th number of iterations the forloop makes 


    reduced_number = reduce(lambda a,b: a+b,i[1])  #the reduce function takes an anonymous function which literally reduced the list to one by adding all the objects in the list


    if reduced_number == k:#checks if any nested list adds up to k
        print(True)
        break

    elif i[0] == len(two_number_lists)-1 and reduced_number != k: # checks if the loop is done and no nested list has added up to the number k
        print(False)
        
        


