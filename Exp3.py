# Creating a List
numbers = [40, 10, 30, 20]

print("Original List:", numbers)

numbers.append(50)
print("After Append:", numbers)

numbers.insert(1, 15)
print("After Insert:", numbers)

numbers.remove(30)
print("After Delete:", numbers)

numbers.sort()
print("After Sort:", numbers)

# Creating a Tuple
my_tuple = (10, 20, 30, 40, 50)

print("\nTuple:", my_tuple)
print("Tuple starting element:", my_tuple[0:2])
print("Tuple last element:", my_tuple[-1:])


# Creating a Set
my_set = {10, 20, 30, 40, 50}

print("\nSet:", my_set)
print("Minimum in Set:", min(my_set))
print("Maximum in Set:", max(my_set))