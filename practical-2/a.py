# a.	Write a python program to demonstrate use of recursive function.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
