# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a test file.")

# Reading from file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:", content)

