# Functions
# user definied module

# Creating a function
def fun():
    print("Inside function")
# calling a function
fun()

# Arguments & parameters
def even_odd(x):
    if(x%2 == 0) :
        print(f"{x} is a even number")
    else:
        print(f"{x} is a odd number")

even_odd(3)
even_odd(2)

# Types of Arguments

# 1. Default Arguments
def myfun(x, y=50):
    print(f"The value of x: {x} and y: {y}")

myfun(10)

# 2. Keyword Arguments
def myfun(q, z):
    print(f"The value of x: {q} and y: {z}")

myfun(q=10, z=20)

# 3. Arbitrary arguments
# *args
def myfun(*args):
    for arg in args:
        print(arg)

myfun("White", "Yellow", "Blue")

# **kwargs
def myfun(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

myfun("Hi", first="Vishnu", mid="Vishwas", last="Fushigoro")

def my_fun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
 
 
def my_fun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
 
 
# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Visnu", "for", "Vishwas")
my_fun(*args)
 
kwargs = {"arg1": "Visnu", "arg2": "for", "arg3": "Vishwas"}
my_fun(**kwargs)

# Function within function
def f1():
    print("f1 function")
    def f2():
        print("f2 function")
    f2()

f1()

# import user defined module
import models.user_defined_modules  as user_defined_modules
print(user_defined_modules.capital)
user_defined_modules.randomfunfact()

# prints the main function of code
print(__name__)
#prints the main function of kanasas module
print(user_defined_modules.__name__)