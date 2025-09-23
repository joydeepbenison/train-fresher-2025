with open("sample.txt","w") as file:
    file.write("hello world\n")
    file.write("Welcome to benison technology\n")

with open("sample.txt","r") as file:
    content = file.read()
    print("File contents")
    print(content)

