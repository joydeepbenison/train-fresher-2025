from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

# Filter even numbers
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print("Even Numbers:", even_nums)

# Sum using reduce
sum_nums = reduce(lambda x, y: x + y, nums)
print("Sum of Numbers:", sum_nums)

