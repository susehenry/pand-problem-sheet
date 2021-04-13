# my solotion to weekly task 06
# a program that takes a positive floating-point number as input 
# and outputs an approximation of its square root
#author: Susan Henry

#import math 

#define a function for calculating the square root
tolerance = 0.000001
def sqrt(x):
   estimate = 1.0
   while True:
        estimate = (estimate + x / estimate) / 2 #calcuation for square root
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break
   return estimate


# main programme
def main():
   while True:
       x = input("Enter a positive number or enter/return to quit: ")
       if x == "":
           break
       x = float(x)
       print("The approximation of the square root is", sqrt(x)) # function sqrt called here
      
if __name__ == "__main__":
    main()

  






