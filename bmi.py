# my solution to weekly task 02
# calcuate a persons body mass index
# author: Susan Henry

#input persons weight in kilograms and height in cms
weight = int (input ('Enter weight in kg:'))
height = int (input ('Enter height in cms:'))

#calcution for bmi 
bmi = round (weight / (height/100 * height/100), 2)

# Display the result
print ('Your BMI is: {}'. format (bmi) )