try:
    num = int(input("Enter a number: "))
    print("Reciprocal is:", 1/num)
except ValueError:
    print("Invalid input, enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Program ended.")

