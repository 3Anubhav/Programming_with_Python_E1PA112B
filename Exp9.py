class A:
    def __init__(self):
        print("Constructor Inside Class A")

    def show(self):
        print("This is Class A")


# Single Inheritance
class B(A):
    def __init__(self):
        super().__init__()
        print("Constructor Inside Class B")

    def show(self):
        print("This is Class B")


# Multilevel Inheritance
class C(B):
    def __init__(self):
        super().__init__()
        print("Constructor Inside Class C")

    def show(self):
        print("This is Class C")


print("\nSingle Inheritance:")
obj = B()
obj.show()

print("\nMultilevel Inheritance:")
obj1 = C()
obj1.show()