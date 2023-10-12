# c.	Write a python program for Sum of squares of first n natural numbers.

def sumOfSquares(n):
    sum = 0
    for i in range(1, n+1):
        sum += i*i
    return sum

userInput = int(input("Enter number: "))
print(sumOfSquares(userInput))
