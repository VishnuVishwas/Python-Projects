# functions

def sum(num1=0, num2=5):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1+num2    

total_sum = sum(5, 32)
print("The total sum is : ", total_sum)

# *args - if we dont know the number of parameters - tuple
def sum(*args):
    print(args)
    print(type(args))
sum(4, 5, 2, 54)

# **kwrgs - defines a dictionary
def items(**kwargs):
    print(kwargs)
    print(type(kwargs))
items(first="vishnu", last="vishwas")