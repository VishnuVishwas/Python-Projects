# Data Types in Python
# Numeric, Sequencial, Boolean, Set & Dictionary
# Variables

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

# Tuple - Immutable 
tuple1 = ("lenskart", "Amazon")
print(tuple1)

list1 = [1, 2, 3, 4, 5]
print("\n",tuple(list1))

print(tuple("Flipkart"))

# for loop
tuple1 = ('Geeks')
n = 5
print("\nTuple with a loop")
for i in range(int(n)):
    tuple1 = (tuple1,)
    print(tuple1)

# Unpacking
tuple1 = ("lenskart", "Amazon", "Flipkart")
a, b, c = tuple1
print(a)
print(b)
print(c)

# Concatenation of Tuples
tuple1 = ("lenskart", "Amazon", "Flipkart")
tuple2 = (0, 1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Delete a tuple
del tuple3
# print(tuple3)

# Boolean
print(type(True))
print(type(False))


# Set - mutable & unordered
set1 = {"Vishnu", "Vishwas", 20}
print(type(set1))

string1 = "Vishnu"
set1 = set(string1)
print(set1)

# set of list
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(set1)

# adding element to set

# add element using add()
set1 = set()
set1.add(23)
set1.add(33)
set1.add(44)
print(set1)

# add element using update()
set1 = {1, 2, (4, 5)}
set1.update([6, 7])
print(set1)

# Removing ele from set
set1 = {1, 2, (4, 5), 9, 10}

# using remove()
set1.remove(1)

# using discard()
set1.discard((4,5))
print(set1)

# using pop()     - First element will be deleted
set1.pop()
print(set1)

# frozen set - immutable
set1 = {1, 2 ,3 , 4, 5} 
set2 = frozenset(set1)
print(set2)

# Empty Frozenset
print(frozenset())

# clear()
set1.clear()
print(set1)

# Union
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.union(set2))

# super set
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4}
superset = set1.issuperset(set2)
print(superset)

# Dictionary
dict = {}
print(dict)

dict = {1 : "Vishnu", 2 : "Vishwas"}
print(dict)

dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'}) 
print("\ndictionary with the use of dict(): ") 
print(dict) 

dict = dict([(1, "Vishnu"), (2, "Vishwas")])
print("\ndictionary with each item as a pair: ")
print(dict)

dict = dict([(1, "Vishnu"), (2, "Vishwas")])
print(dict[1])
print(dict.get(2))



# variables are used to store data 

# type()
number = 435
print(number)
print(type(number))  # type() - data type of variable

name = "Vishwas"
print(name)
print(type(name))    # the data type will be string

# concatenation of variable 
print("Vishnu " + name)

# multiple assignment
a = b = c = 45
print(str(a) + " " + str(b) + " " + str(c))

# multiple assignment  for different var in 1line
a, b, c = 34, 44, 55
print(str(a) + " " + str(b) + " " + str(c))

# concatenation of 2 variables
fist_name = "Itachi"
last_name = "Uciha"

print("Full name : " + fist_name + " " + last_name)

# Global Variable - Global keyword is used inside a function only when we want to do assignments or when we want to change a variable

x = 15
def change():
    # using a global keyword
    global x

    # increment value of a by 5
    x = x + 6
    print("Value of x inside a function :", x)
 
change()
print("Value of x outside a function :", x)