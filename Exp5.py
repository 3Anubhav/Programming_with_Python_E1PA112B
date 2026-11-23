# String Programming
text = input("Enter a string: ")

# Calculate Length
print("\nLength:", len(text))

# Positive and Negative Indexing
print("First Character:", text[0])
print("Last Character:", text[-1])

# Slicing
print("Sliced String:", text[0:4])

# Split and Join
words = text.split()
print("Split String:", words)
print("Joined String:", "-".join(words))

# Case Conversion
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())

# Find and Replace
search = input("\nEnter a word to find: ")
print("Position:", text.find(search))

replace = input("Enter replacement word: ")
print("After Replace:", text.replace(search, replace))

# Simple Validation using String Methods
if text.isalpha():
    print("Valid Alphabetic String")
elif text.isdigit():
    print("Valid Numeric String")
elif text.isalnum():
    print("Valid Alphanumeric String")
else:
    print("String contains Special Characters or Spaces")