# Lambda function for square
square = lambda x: x**2
print("Square of 5:", square(5))

# Lambda with map
nums = [1, 2, 3, 4, 5]
squared_nums = list(map(lambda x: x**2, nums))
print("Squared Numbers:", squared_nums)

