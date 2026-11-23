def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

# Maximum of Three Numbers using Function
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Maximum Number:", maximum(a, b, c))


# Factorial using Function
num = int(input("\nEnter a number: "))
print("Factorial:", factorial(num))