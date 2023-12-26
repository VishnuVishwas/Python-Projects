# Dictionaries

family = {
    "tiger" : "cat",
    "fox" : "dog",
    "racoon" : "dog"
}

# using constructor
family2 = dict(tiger = "cat", fox = "dog")

print(family)
print(family2)
print(type(family2))
print(len(family))

# Access items
print(family["fox"])
print(family.get("tiger"))

# list all keys, values & items
print(family.keys())
print(family.values())
print(family.items())

# verify if key exists
print("tiger" in family)
print("cat" in family)

# Change values 
family["tiger"] = "dog"              # update key's value
family.update({"Lion": "Cat"})       # add new element
print(family)

# remove items
family.pop("tiger")
print(family)

# remove last added pair
family.popitem()
print(family)

# delete and clear
#clear
family2.clear()
print(family2)

#delete
del family2

# Creating a copy
newdictionary = family.copy()
newdictionary1 = dict(family)
print(newdictionary)
print(newdictionary1)

# Nested Dictionaries
type1 = {
    "name" : "plant",
    "instrument" : "vocals"
}

type2 = {
    "name" : "page",
    "instrument" : "guitar"
}

band = {
    "member1" : type1,
    "member2" : type2
}

print("")
print(band)
print(band["member1"])
print(band["member1"]["name"])
