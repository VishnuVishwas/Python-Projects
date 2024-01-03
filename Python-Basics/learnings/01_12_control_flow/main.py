# Conditional statments 
# if, elif, else, shor hand of if, short hand of else, and, or, not, nested if, pass

# Loops 
# while, do while, 

# Conditional Statments
a = 5
b = 324

# if statement
if b > a:
    print("B is greater than A")

# elif statement
if b > a:
    print("B is greater than A")
elif a == b:
    print("Both are equal")

# else statement
if b > a:
    print("B is greater than A")
elif a == b:
    print("Both are equal")
else:
    print("A is greater than B")

# Short hand if 
if a > b: print("a is greater than b")

# Short hand else 
print("A") if a > b else print("B")

# and
c = 2254
if b>a and c>a:
    print("Both conditions are true")

# or 
if a > b or a > c:
    print("prints if any one of the condition is true")

# Not 
    if not a>b:
        print("A is not greater than B")

# Nested if 
x = 5
if x > 2:
    print("if of 2")
    if x > 1:
        print("if of 1")
    else:
        print("1's else")
else:
    print("else of 2")

# Pass
a = 33
b = 200
if b > a:
    pass

# Loops 
# While 
count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")
else:
    print("In Else Block")

# for 
n = 4
for i in range(0, n):
    print(i)

# Iterating list
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

# Iterating nDictionary
d = dict()
d['xya'] = 123
d['xyb'] = 456
for i in d:
    print(i, d[i])

# break
value = 1
while value<=10:
    if(value == 5):
        break
    print(value)
    value+=1

# continue
while value<10:
    value+=1
    if(value == 5):
        continue
    print(value)
else:
    print("value is now equal to : ", value)

# working of loop internally
fruits = ["apple", "orange", "kiwi"]
i = iter(fruits)
while True:
    try:
        fruit = next(i)
        print(fruit)
    except StopIteration:
        print("Break")
        break