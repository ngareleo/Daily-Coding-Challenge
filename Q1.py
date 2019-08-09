#This problem was recently asked by Google.

#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

sample = [10, 15, 3, 7]

k = 17

def any_two(array,k):
    sp = 0 #Starting point
    answer = [] #To store findings
    while ( sp < len(array)):

        for i in array:

            if ( sp + i == k ):

                answer.append(True)

            else:

                answer.append(False)
        sp += 1
    #analyse answers

    if True in answer:
        return True
    else:
        return False
print(any_two(sample,k))
