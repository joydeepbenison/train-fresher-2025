#Fibonaci series

num = int(input("Enter the limit: "))
first,second = 0,1
"""
for i in range(num): #Number of iteration
    print(first)
    first, second = second, first +second
"""

#Upto limit

while first <= num:
    print(first)
    first,second = second,first + second

