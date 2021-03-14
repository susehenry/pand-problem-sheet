# my solution to weekly task 07
# write a program that reads in a text file 
# and outputs the number of e's it contains.
# moby-dick.txt file created

#author: Susan Henry



l=input("Enter letter to be searched:")
x = 0
 
with open("moby-dick.txt", 'r') as f: # 'r' = read, opens a file for reading
    for line in f:
        words = line.split() #splits the line to form a list of words
        for i in words:      # creates for loop to move through each word 
            for letter in i: # creates another for loop moves through the letters in each word
                if(letter==l): #if letter in text = letter in search it is added to count
                    x=x+1
print("Occurrences of the letter: {}" .format(x))



#ref https://www.sanfoundry.com/python-program-read-file-counts-number/