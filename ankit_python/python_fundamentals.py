def numbers():
#     for i in range(1,6):
#         yield i
# for n in numbers():
#     print(n)

# num = int(input())
# for i in range(0,num):
#     print(i)

# for i in range(1,10):
#     print(i)

# Examples of generators
# def ankit(n):
#     for i in range(1,n+1):
#         yield(i ** 2)

# n=int(input())       
# square = ankit(n)

# for _ in range(n):
#     print(next(square))


# str1 = "Hello World"
# res=''
# for num in str1:
#     res += num.upper()
# print(res)

# List operations
# num = [1,2,3,4,5]
# print(sum(num))
# print(max(num))
# print([x**2 for x in num])

# Fibonacci Series
# def fib(n):
#     if n<=1:
#         return 1
#     res = [0,1]
#     for i in range(2,n):
#         res.append(res[i-1]+res[i-2])
#     return(res)
# n=int(input())
# print(fib(n))

# Simple number guessing game
# import random
# num = random.randint(1,50)
# while True:
#     guess = int(input())
#     if guess == num:
#         print("Correct")
#         break
#     elif guess<num:
#         print("Nearer")
#     else:
#         print("Further")

# Lambda function uses
# num = [1,2,3,4,5]
# squares = list(map(lambda x:x**2,num))
# evens = list(filter(lambda x:x%2==0, num))
# print(squares)
# print(evens)

# Generators
# def square_num(n):
#     for i in range(1,n+1):
#         yield i*i 
# for num in square_num(10):
#     print(num)
