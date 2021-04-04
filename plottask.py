#Program to display plot functions
#Create a plot using Matplotlib containing 3 lines 
#X axis contains range of points from 0 - 4
#Y axis points for each line are calcuted using the different formulas below
#author: Susan Henry

import matplotlib.pyplot as plt
import numpy as np

#first plot line - f(x)=x. 
# y1 calculated using formula x=x 
x1 = np.array([0, 1, 2, 3, 4])
y1 = x1



#second plot line - g(x)=x2
#y2 calculated using formula x **2
x2 = np.array([0, 1, 2, 3, 4])
y2 =x2 **2



#third plot line - h(x)=x3
#y3 calculated using formula x * x * x
x3 = np.array ([0, 1, 2, 3, 4])
y3 = x3 * x3 * x3
 


font1 ={'family':'sans', 'color' : 'purple', 'size' :20} # setting font properties for title
font2 = {'family':'sans','color':'hotpink','size':15} # setting font properties for labels

plt.title ("Plot Task" , fontdict= font1) #adding a title and font properties
plt.xlabel("x axis", fontdict= font2) # adding x and y axis label and font properties
plt.ylabel("y axis", fontdict= font2)




plt.plot(x1, y1, label= "F") #plots x versus y as a line, label = label to identify line for legend
plt.plot ( x2, y2, label= "G")
plt.plot (x3, y3, label= "H")

#Places a legend box in plot
plt.legend(bbox_to_anchor=(0.2, 0.8), borderaxespad=0.)

plt.show()


#Refrence
# https://www.w3schools.com/python/matplotlib_line.asp
# https://matplotlib.org/stable/tutorials/intermediate/legend_guide.html

