"""
Reading data from files and writing data into files using python.
"""

########################################################################

# Opening, writing and closing files

# open file with purpose
file = open("file_path", "w")                    # open file and write
file.write("Python is best to learn coding")

########################################################################
file = open("file_path", "r")                    # open file and read

print(file.read())      # read entire content in file
print(file.read(20))    # read first 20 characters

lines = file.readlines()      # all lines store in a variable

for line in lines:              # iterate each line from lines
    print(line)

print(file.readline())          # print only first line
print(file.readline())          # print second line
########################################################################

file = open("file_path", "a")                    # open file and append data
file.write("\nPython is an easy programming language.")

file.close()            # close the file
########################################################################