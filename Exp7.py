# Creating and Writing a File
file = open("sample.txt", "w")
file.write("Anubhav 26SCAT2020003")
file.close()

# Reading a File
file = open("sample.txt", "r")
content = file.read()
print("File Content:", content)
file.close()

# Appending to a File
file = open("sample.txt", "a")
file.write(" This is additional text!")
file.close()

# Display Updated Content
file = open("sample.txt", "r")
content = file.read()
print("\nUpdated Content:", content)
file.close()

# Display Unique Words
words = content.split()
unique_words = set(words)
print("\nUnique Words:", unique_words)

# Demonstrating File Modes
print("\nFile Modes: r = Read, w = Write, a = Append")

# Search and Replace
search = input("\nEnter word to search: ")
replace = input("Enter replacement word: ")

if search in content:
    content = content.replace(search, replace)

    file = open("sample.txt", "w")
    file.write(content)
    file.close()

    print("Word Replaced Successfully!")
else:
    print("Word Not Found")

# Display Final Content
file = open("sample.txt", "r")
print("\nFinal File Content:", file.read())
file.close()