# Generator function to yield squares up to 100
def squares_up_to_100():
    n = 1
    while n * n <= 100:
        yield n * n
        n = n +1

# Using the generator
for square in squares_up_to_100():
    print(square)

