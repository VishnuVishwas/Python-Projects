# data types in python 

# int 
number = 45
print("Type of :", number, "is : ", type(number))

# float
number = 45.6
print("Type of :", number, "is : ", type(number))

# string 
name = "Itachi"
print("Type of :", name, "is : ", type(name))

# list    
fruits = ['Mango', 'Apple']
print("Type of :", fruits, "is : ", type(fruits))

# Boolean
flag = True
print(flag == False)    #checks if flag is eq to false

# Tuple 
constants = (3.14, 9.8)
print("Type of :", constants[0], "is : ", type(constants))

# set
set = {'vishnu', 20, 'Male'}
print("Type of :", set, "is : ", type(set))

phone_book = {
    1 : "Nagato",
    2 : "Saske",
    3 : "Madara"
}
print(type(phone_book))

# variables are used to store data 

number = 435
print(number)
print(type(number))  # type() - data type of varible

name = "Vishwas"
print(name)
print(type(name))    # the data type will be string

# concatenation of variable 
print("Vishnu " + name)

# multiple assignment
a = b = c = 45
print(str(a) + " " + str(b) + " " + str(c))

# multiple assgnment for different var in 1line
a, b, c = 34, 44, 55
print(str(a) + " " + str(b) + " " + str(c))

#concatenation of 2 variables
fist_name = "Itachi"
last_name = "Uciha"

print("Full name : " + fist_name + " " + last_name)


