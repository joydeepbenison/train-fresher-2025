# Writing data to file
with open("students.txt", "w") as f:
    f.write("ID: 1, Name: Mani, Marks: 90\n")
    f.write("ID: 2, Name: Ankit, Marks: 95\n")
    f.write("ID: 3, Name: yashaswini, Marks : 97\n")
    f.write("Id: 4, name: Alekya, Marks : 98\n")

#Read data from file
with open("students.txt", "r") as f:
    print("File content:")
    print(f.read())

