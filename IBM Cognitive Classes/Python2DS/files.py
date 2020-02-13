import os
print (os.getcwd())
example = open("example1.txt", "r")
print (example.name)
print (example.mode)

Filecontent = example.read()
print (Filecontent)
type (Filecontent)
example.close()

with open("example1.txt", "r") as file1:
    print(file1.read(4))

# Read all lines and save as a list

#variable should be created first 
with open("example1.txt", "r") as file1:
    FileasList = file1.readlines()

# Print the first line
FileasList[0]

# Add write examples and exercises 
