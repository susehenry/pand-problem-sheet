# my solution to weekly task 07
# write a program that reads in a text file 
# and outputs the number of e's it contains.
# moby-dick.txt file created

#author: Susan Henry




with open ("moby-dick.txt", "rt") as file: #opens file in read mode
    data = file.read() # reads content of file
    es = data.count ("e") # counts the number of letter E's in text
    print ( "Occurences of the letter E: {}" .format(es))


#ref https://www.sanfoundry.com/python-program-read-file-counts-number/
#ref https://pythonexamples.org/python-count-number-of-characters-in-text-file/ 