# my solution to weekly task 02
# calcuate a persons body mass index
# author: Susan Henry

#Input persons weight in kilograms and height in cms
#Using int will convert the number inputted into an interger which is need for the calculation
weight = int (input ('Enter weight in kg:'))
height = int (input ('Enter height in cms:'))

# calcution for bmi 
# round function returns a floating point number 
# that is rounded to a specified number of decimals in this program 2
bmi = round(weight / (height/100 * height/100), 2)

# Display the result
print ('Your BMI is: {}'. format (bmi) ) 