# A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.

# def outerFunction(num1):
#     def innerFunction(num2):
#         return num1 * num2
#     return innerFunction

# # first pass the value to outer function
# times3 = outerFunction(3)
# times5 = outerFunction(5)

# # passing the 
# print(times3(9))
# print(times5(times3(3)))

def parent(person) :
    coins = 3
    def child():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")

    return child

tommy = parent("Tommy")
jenny = parent("Jenny")

tommy()
tommy()
jenny()
tommy()