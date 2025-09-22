# Write to file
with open("example.txt", "w") as f:#w means overwrite it
    f.write("Hello!\n")

# Read file
with open("example.txt", "r") as f:
    print(f.read())

# Append to file
with open("example.txt", "a") as f:# a it will add
    f.write("This is an added line.\n")

# Read again
with open("example.txt", "r") as f:
    print(f.read())

