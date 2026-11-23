# Creating a Dictionary
student = {"Name": "Anubhav", "Age": 21, "Marks": 85}

print("Original Dictionary:", student)

student["Course"] = "BCA"  # Add
student["Marks"] = 90      # Update
del student["Age"]         # Delete

print("After Changes:", student)

# Searching a Value in Dictionary
search = input("\nEnter a name to search : ")

if search in student.values():
    print("Value Found:", search)
else:
    print("Value Not Found")

# Traversing Dictionary using For Loop
for key, value in student.items():
    print(key, ":", value)

# Factorial using Loop
num = int(input("\nEnter a number to find it's factorial : "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("\nFactorial:", fact)

# Even Numbers using Loop
print("Even Numbers:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i, end=" ")