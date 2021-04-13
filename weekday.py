# my solution to weekly task 05
# A program that outputs whether or not today is a weekday
# author: Susan Henry

# import Python's datetime module

import datetime

 


 # find out what day of the week it is today - datetime.date.today()
 # weekday () represents the days of the week in numbers
 # weekdays:  0 =Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday
 # weekend: 5 = Saturday, 6 = Sunday

todaysDate = datetime.date.today().weekday ()

if todaysDate < 5:
    print ("Yes, unfortunately today is a weekday.")
else: 
    print ("It is the weekend, Yay!")    



