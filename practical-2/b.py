# b.	Write a python program to check Armstrong Number using function.

def isArmstrong(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if n == sum:
        return True
    else:
        return False
    
print(isArmstrong(153))
print(isArmstrong(123))
