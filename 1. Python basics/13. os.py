import os

print(os.getcwd())      # to get the currrent worrking dir
os.chdir('../')         # to change the dir
os.chdir(path)                          # changing dir
path = os.path.join(parent_dir,dir)   # concatening the string
os.mkdir(path)                          # craeting new dir
print(os.listdir(path))                 # list out all folders, files in dir
os.rename(fd,'New.txt')             # rename the file
result = os.path.exists("file_name") # output as False or True
size = os.path.getsize("filename")  # getting the size of file
--------------------------------------------------------------------------------
def current_path():
    print("Current working directory: ") 
    print(os.getcwd()) 
    print() 
current_path() 
os.chdir('../')         # to change the dir
current_path()

---------------------------------------------------------------------------------
parent_dir = "C:/Users/91983/Desktop/Python/Interview Python/Selenium_Python"
dir = "rushi"

path = os.path.join(parent_dir,dir)   # concatening the string

os.mkdir(path)                          # craeting new dir
print("directory is crated", dir)

os.chdir(path)                          # changing dir
print("Current working directory: ", os.getcwd())
---------------------------------------------------------------------------------------

path = "C:/Users/91983/Desktop/Python/Interview Python/Selenium_Python"
print(os.listdir(path))                 # list out all folders, files in dir
-------------------------------------------------------------------------------------------
os.chdir("C:/Users/91983/Desktop/Python/Interview Python/Selenium_Python/rushi")
path = os.getcwd()
file_name = "RUSHIKESH.py"

file_path = os.path.join(path,file)

with open(file_path,"w") as file:
    file.write("Jai shree ram")

print(f"File name '{file_name}' successfully created in '{file_path}' directory")
-------------------------------------------------------------------------------------
location = "C:/Users/91983/Desktop/Python/Interview Python/Selenium_Python"
dir = "rushi"
path = os.path.join(location, dir)
os.rmdir(path)

fd = "GFG.txt"
os.rename(fd,'New.txt')             # rename the file

result = os.path.exists("file_name") # output as False or True
print(result)

size = os.path.getsize("filename")
print("Size of the file is", size," bytes.")
-------------------------------------------------------------------------------------------

