class custom(Exception):
    pass

x = 6

try:
    # print(z)
    # print(x/0)
    # if not type(x) is str:
    #     raise TypeError("only strings are allowed")
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

