# Lists, Tuple, Dictionary

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
Tuple1 = ('Geeks')
n = 5
print("\nTuple with a loop")
for i in range(int(n)):
    Tuple1 = (Tuple1,)
    print(Tuple1)

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



# Dictionary
Dict = {}
print(Dict)

Dict = {1 : "Vishnu", 2 : "Vishwas"}
print(Dict)

Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 

Dict = dict([(1, "Vishnu"), (2, "Vishwas")])
print("\nDictionary with each item as a pair: ")
print(Dict)

Dict = dict([(1, "Vishnu"), (2, "Vishwas")])
print(Dict[1])
print(Dict.get(2))