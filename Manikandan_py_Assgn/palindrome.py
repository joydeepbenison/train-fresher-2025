# Take user input as an integer and check palindrome

try:
    num = int(input("Enter the integer number: "))
except ValueError:
    print("Enter a proper integer")
    exit()  # Stop the program if input is invalid

s = str(num)
low, high = 0, len(s) - 1

while low < high:
    if s[low] != s[high]:
        print("Not a palindrome")
        break
    low += 1
    high -= 1
else:
    print("Palindrome")

