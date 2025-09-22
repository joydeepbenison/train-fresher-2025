#Error handling
try:
    x = 10/0
except ZeroDivisionError:
    print("Error")

try:
    num = int("abc")
except ValueError:
    print("Error")

try:
    x = int("10")/0
except ValueError:
    print("Invalid conversion")
except ZeroDivisionError:
    print("Divison by zero is not allowed")

try:
    res = 10 + "five"
except Exception as e:
    print("Something went wrong: ",e)
