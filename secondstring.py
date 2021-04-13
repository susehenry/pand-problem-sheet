#my solution to weekly task 03
# program that asks a user to input a string and outputs every second letter 
# in reverse order
#author: Susan Henry


secondString = input("Enter a string: ")


# [::-1] = reverses string
# [::2] = outputs every second element

print ('Output: {}' .format (secondString[::-1][::2])) 








