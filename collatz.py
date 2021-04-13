#my solution to weekly task 04
#program that asks the user to input any positive interger 
#and outputs the succesive values following calculation
#At each step calculate the next value by taking the current value and, if it is even, 
#divide it by two, but if it is odd, multiply it by three and add one.

#author: Susan Henry

import math 


number = int(input ('enter a positive integer:'))
     

while number != 1: # creates a loop to keep returning a number until 1 is reached
  if (number % 2) == 0: # checks if number is even (True)
    number = number/2  # if True the number will be divided by 2
  else: # if number is not even (False)
   number  = (number* 3) + 1 # if False the number will be multiplied by 3 and add one
 
 

  print (number) 
   
 



    
     
