# Exception handling in python 
# File operations 

import os

class custom(Exception):
    pass

x = 6

try:
    print(z)
    print(x/0)
    if not type(x) is str:
        raise TypeError("only strings are allowed")
    raise custom("This a custom error")
except NameError:
    print("We have a name error")
except ZeroDivisionError:
    print("You cannot divide with zero")
# if exception occurs in try block, this will be executed
except Exception as error:
    print(error)
finally:
    print("This block will be printed even if there are no erros")

# File operations
# read files

# 1. read content using 'for loop'
file = open('sample.txt', 'r')
for each in file:
    print(each)

# 2. to extract all characters
file = open('sample.txt')
print(file.read())

# 3. using 'with'
with open('sample.txt') as file:
    data = file.read()
print(data)

# 4. desired number of characters
file = open("sample.txt", "r")
print(file.read(7))

# 5. using 'split'  -> split when we encounter space
with open("sample.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

# write files 
# Method 1 - 'w' mode and write()
file = open('sample2.txt', 'w')
file.write("This is line1 in write mode. ")
file.write("This continuation of line1 in write mode")
file.close()

# Method 2 - with()
with open('sample2.txt', "w") as f:
    f.write("Method 2")

# append mode
file = open('sample2.txt', 'a')
file.write("This will add this line")
file.close()

# remove files
os.remove('sample.txt')
print("Sample.txt was removed")
os.remove('sample2.txt')
print("Sample2.txt was removed")


# All file handling functions
import File_handling_fuctions.main as fun

filename = "sample3.txt"
new_filename = "new_sample.txt"

fun.create_file(filename)
fun.read_file(filename)
fun.append_file(filename, "This is appended text\n")
fun.read_file(filename)
fun.rename_file(filename, new_filename)
fun.read_file(new_filename)
fun.delete_file(new_filename)
print("The file was deleted")