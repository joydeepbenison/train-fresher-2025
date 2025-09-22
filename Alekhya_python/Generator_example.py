def fibonacci(n):
    a, b = 0, 1 #initializing
    count = 0
    while count < n:
        yield a #pauses the function and sends the current value
        a, b = b, a + b
        count += 1

for num in fibonacci(7):
    print(num)

