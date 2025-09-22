file = open("example.txt","mode")

# "r" -> Read
# "w" -> Write
# "a" -> append
# "x" -> Create
# "b" -> Binary Mode 
# "t" -> Text mode

#Reading a File
f = open("example.txt", "r")

print(f.read()) #read entire file
print(f.read(10)) #Read first 10 characters
print(f.readline()) #Read first line
print(f.readlines()) #Readl all lines as list

f.close()

#writing to a file
f = open("example.txt","w")
f.write("Hello, Python!\n") #overwrites content
f.write("File handling is easy.")
f.close()

#Appending to a file
f = open("example.txt","a")
f.write("\nThis line is appended")
f.close()

#using with (Better Practice)
with open("example.txt","r") as f:
    content = f.read()
    print(content)

#Deleting a File

import os

if os.path.exists("example.txt"):
    os.remove("example.txt")
else:
    print("File does not exist")
    
# create -> write -> read -> append -> read again ->


