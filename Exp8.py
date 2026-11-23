# Creating a Student Class
class Student:
    # Constructor
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    # Method to Display Student Details
    def display(self):
        print("Name:", self.name, "| Age:", self.age, "| Marks:", self.marks)


# Creating Multiple Objects
s1 = Student("Anubhav", 21, 90)
s2 = Student("Rahul", 20, 85)
s3 = Student("Aman", 22, 95)

# Displaying Student Data
print("Student 1:")
s1.display()

print("\nStudent 2:")
s2.display()

print("\nStudent 3:")
s3.display()