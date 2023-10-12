# b.	Write a python program to calculate simple Interest and compound Interest.

def simpleInterest(p, r, t):
    return (p * r * t) / 100

def compoundInterest(p, r, t):
    return p * (1 + r/100) ** t

p = int(input("Enter principal amount: "))
r = int(input("Enter rate of interest: "))
t = int(input("Enter time: "))

print("Simple Interest: ", simpleInterest(p, r, t))
print("Compound Interest: ", compoundInterest(p, r, t))
