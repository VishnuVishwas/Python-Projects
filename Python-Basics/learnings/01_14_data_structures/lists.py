# Creating a list
users = ['Vishnu', 'Vishwas', 'Ankith', 'Dhanush']
data = ['Vishnu', 20, True]
emptylist = []

# print(users)
# print(data)
# print(emptylist)

# check element in list
# print("Vishnu" in users)
# print("Vishnu" in emptylist)

# Accessing element using index / Slicing
# print(users[0:3])               # excludes last element
# print(users[:])                 # Prints all elements
# print(users[-3:-1])             # Accessing from -ve index

# len 
# print("Length of data is : ", len(data))

# Appending element to list
print("Intitial List : ", users)

# # Adding to last 
# users.append('Anya')
# print(users)

# # updating using operators
# users += ['Forger', 'L']
# print(users)

# # extend()
# users.extend(['Robert', 'Albert'])
# print(users)

# # Adding list to list
# emptylist.extend(data)
# print(emptylist)

# # Insert method
# users.insert(0, 'Bob')
# print(users)

# # Adding element using slicing

# users[3:3] = ['Anath', 'Sid']         # the elements will be moved and space is made to new ones
# print(users)

# users[1:4] = ['Romeo', 'Juilet']   # 1, 2 index elements are replaced by new ones
# print(users)

# Remove
anime = ['Naruto', 'Boruto', 'Shinigami', 'Light', 'Zenitsu']
# anime.remove('Boruto')
# print(anime)

# # pop
# anime.pop()
# print(anime)

# # del
# del anime[0]
# print(anime)

# # Clear all elements in list
# anime.clear()         # list will be empty
# print(anime)

# Reversing a list
reverse_list = anime.reverse()
print(anime)

# sort
anime.sort()            # ascending order
print(anime)

#descending order
anime.sort(reverse=True) 
print(anime)

# copy list types
list2 = users.copy()
mylist = list(anime)
list1 = anime[:]

print(mylist)
print(list1)
print(list2)