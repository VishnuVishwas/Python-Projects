# Sets

# creating a set
nums = {1, 2, 3, 4}
nums2 = set((1, 3, 4, 5, 2 , 1))
print(nums)
print(nums2)

# True is 1 and Flase is 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

#check if value is in set
print(2 in nums)

# Add elements from one set to another
nums3 = {5, 6 ,7}
nums.update(nums3)
print(nums)

# merge two sets
one = {1, 2, 3}
two = {4, 5, 6}

newSet = one.union(two)
print(newSet)

# Intersection
one = {1, 2, 3}
two = {4, 2, 1}
newSet = one.intersection(two)
print(newSet)

# or 
one = {1, 2, 3}
two = {4, 2, 1}
one.intersection_update(two)
print(one)

# difference  - keep everything except the duplicates
one = {1, 2, 3}
two = {4, 2, 1}

one.symmetric_difference_update(two)
print(one)