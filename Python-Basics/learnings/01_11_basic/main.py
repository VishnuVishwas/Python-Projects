# Data Types in Python
# Numeric, Sequencial

# Numeric Data Types
# int, float and Complex numbers

# int
a = 5
print(type(a))

# float 
b = 5.0
print(type(b))

# Complex Numbers
c = 2 + 4j
print(type(c))

# Sequence Data types in python
# string, List, Tuple

# string - Immutable
# create string - single line
string1 = 'Welcome'
print(string1)

# multiline string
string2 = '''
Welcome
Happy
learning  '''
print(string2)

# Accessing characters in string
string1 = "Vishnu Vishwas"
print(string1[0])
print(string1[-1])

# string slicing
print(len(string1))
print(string1[3: 9])   # last index not considered
print(string1[3: -2])

# Reversing a python string
# Method - 1
print(string1[::-1])
# Method - 2
string1 = "".join(reversed(string1))
print(string1)

# Deleting / Updating from a string

# 1. Convert string1-> List1 -> string2
string1 = "Hello, I'm Vishnu"
list1 = list(string1)
list1[2] = 'P'
string2 = "".join(list1)
print(string2)

# 2. Slicing
string3 = string1[0:2] + 'p' + string1[3:]
print(string3)

# deleting a char & string
string1 = "Vishnu Vishwas"
# del string1[2] 
# print(string1) 

# using slicing 
string2 = string1[0:2] + string1[3:]
print(string2)

del string1
# print(string1)

# Lists
# lists are mutable

# Create List
list = ['Naruto', 5, 'Saitama', 6, 'Gojo']
print(list)

# Acessing 
print(list[0:2])

# Nested List
list = [['Naruto', 5, 'Saitama', 6, 'Gojo'], ['Hokage', 'SuperHuman', 'Sensei']]
print(list[1][2])

# size of list
print(len(list))

# String to list
# Split the words where there is space

# Method 1 
# string = input("Enter a string : ")
# list = string.split()
# print(list)
# Enter a string : vishnu is a good boy
# ['vishnu', 'is', 'a', 'good', 'boy']


# Adding elements to list

# 1. append()
list = ['Naruto', 5, 'Saitama', 6, 'Gojo']
list.append(100)
print(list)

# adding elements using a loop 
for i in range(10, 40, 7):
    list.append(i)
print(list)

# adding elements using a Tuple
list.append((50, 232))
print(list)

# appending a list
list1 = ("Zenin", "Gojo", "Uzumaki")
list.append(list1)
print(list)

# 2. insert(position, value)
list = ['1', 5, '2', 6, '3']
list.insert(3, "Anya")
print(list)

# 3. extend() - To add multiple ele at the same time at the end of the list.
list = ['1', 5, '2', 6, '3']
list.extend(["krishna", "Radha"])
print(list)

# Reverse a list -> reverse()
list = ['1', 5, '2', 6, '3']
list.reverse()
print("After reversing : ", list)

# Removing elements from the list
# 1. remove()
list = [1, 2, 3, 4, 5, 6,7 , 8, 9, 10, 11, 12]
print(list)
list.remove(5)
list.remove(6)
print(list)

# using iterator -  remove multiple elements
for i in range(1, 5):
    list.remove(i)
print(list)

# 2. using pop()
print(list)
print(list.pop())
print(list)

# removing element from specific location pop(location)
list.pop(3)
print(list)

