# Check if a number is an Armstrong number

num = int(input("Enter an integer number: "))

s = str(num)
n = len(s)
sum_digits = 0

for digit in s:
    sum_digits = sum_digits + int(digit) ** n

if sum_digits == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

