f = open("names.txt")
# print(f.read())
# # print(f.readline())

# for line in f:
#     print(line)

# f.close()

try:
    f = open("names.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()

# append
f = open("names.txt", 'a')
f.write("Neil\n")
f.close()

# overwrite
f = open("names.txt", 'w')
f.write("The content was overwritten")
f.close()

f = open("names.txt")
print(f.read())
f.close()

import os
if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()

if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file dosenot exit to remove")

# with has built-in implicit exception handling
# close() will be automatically called
with open ("names.txt") as f:
    content = f.read()