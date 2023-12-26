# # Loops 

# # while 
# value = 1
# while value<=10:
#     print(value)
#     value+=1

# # break
# while value<=10:
#     if(value == 5):
#         break
#     print(value)
#     value+=1

# # continue
# while value<10:
#     value+=1
#     if(value == 5):
#         continue
#     print(value)
# else:
#     print("value is now equal to : ", value)

# for loop
heros = ["pateric", "batman", "aquaman"]
for x in heros:
    print(x)

# break
for x in heros:
    if x == 'batman':
        break
    print(x)

#continue
for x in heros:
    if x == 'batman':
        continue
    print(x)    

for i in range (4):
    print(i)

for i in range (1, 4):
    print(i)

for x in range(5, 101, 5):
    print(x)
else:
    print("the stopping number : ", x)

# nested for loop
names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

for x in names:
    for y in actions:
        print(x + " " + " " + y)