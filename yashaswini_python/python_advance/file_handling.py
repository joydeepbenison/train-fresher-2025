# Text file
with open("example.txt", "w") as f:
    f.write("Hello World\nPython File Handling")

with open("example.txt", "r") as f:
    print(f.read())

# Binary file
data = b"Binary data example"
with open("example.bin", "wb") as f:
    f.write(data)

with open("example.bin", "rb") as f:
    print(f.read())

