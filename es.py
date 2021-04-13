# my solution to weekly task 07
# A program that reads in a text file and outputs the number of e's it contains.
# moby-dick.txt file created

#author: Susan Henry



#The with statement is frequently used with files, 
#as it can help code to be more readable 
#in addition it will automatically close the file.

with open ("moby-dick.txt", "rt") as file: #opens file in read mode
    data = file.read() # reads content of file
    es = data.count ("e") # counts the number of letter E's in text
    print ( "Occurences of the letter E: {}" .format(es))

