#1. Write a function called calculate_factorial that takes a positive integer as a parameter and returns its factorial (use recursion)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = int(input())
print(factorial(5))

#2. Write a recursive function fibonacci that returns the nth Fibonacci number.
#q = input()
def fibonacci(n):
    a = 1
    b = 2
    if n<0:
        print("Error")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
            #q += 1
        return c
n = int(input())
print(fibonacci(n))