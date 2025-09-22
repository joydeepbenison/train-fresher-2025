def square_numbers():
    for n in range(1, 101):  # Numbers from 1 to 100
        yield n ** 2

for i in square_numbers():
    print(i)

