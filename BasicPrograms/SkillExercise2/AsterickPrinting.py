# Program for printing "*" according to the given input

n = int(input("Enter number of astriks you need:"))
x = n
for i in range(n):
    print("*" * x)
    x = x - 1
x = 1
for i in range(n):
    print("*" * x)
    x = x + 1
