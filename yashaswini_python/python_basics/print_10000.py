def square_numbers(n):
    for i in range(1, n + 1):
        yield i * i

# Use the generator
squares = square_numbers(10000)

for sq in squares:
    print(sq)

