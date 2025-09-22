def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("Number must be positive")
            return value
        except ValueError as e:
            print("Invalid input:", e)

age = get_int("Enter your age: ")
print("Your age is:", age)

