tuple1 = (1, 23, 432, 'Vishnu')
tuple2 = tuple((1, 2, 2, 2, 3 , 54))

print(tuple1)
print(tuple2)
print(type(tuple2))

# creating a new tuple from a list
newlist = tuple(tuple1)
newtuple = tuple(newlist)
print(newtuple)

# Unpacking of tuple
(one, *two, three) = newtuple      # here * means remaining elements
print(one)
print(two)
print(three)

# find freq of ele
print(tuple2.count(2))