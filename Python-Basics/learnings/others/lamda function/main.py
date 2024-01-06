# lamda function
str1 = "Vishnu"

# create lambda function
upper = lambda message: message.upper()
print(upper(str1))

# Example 2
format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"
print("Int formmating: ", format_numeric(1000000000))
print("Float formatting: ", format_numeric(999999.234234324324324234))

# Difference between lambda and def
def cube(y):
    return y*y*y
print(cube(2))

# the function could be written in 1line
cube = lambda y: y*y*y
print(cube(5))