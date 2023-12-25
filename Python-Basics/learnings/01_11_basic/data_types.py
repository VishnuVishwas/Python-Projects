import math

#int
a = 5
print('Integer: '+str(a))

#float
b = 25.7
print('Float: '+str(b))

#divide
c = int(b//a)
print('Divide Operation: '+str(c))

# integer pow
d = c**a
print(f'Power: {c}^{a}={d}')

# List
names = ['cat','dog','marvel']
print(names)

# Dictionary
contact_info = {'name':"Dojo",
                "email":"dojo@gmail.com",
                "contact":"+1838523842"}

print(contact_info)

#List operations
names.append('Montony')
print(f'After Adding to List: {names}')

other_names = ['Naruto','Sakuna','Itadori','Gojo']
names.extend(other_names)
print(f'After extending with other names: {names}')

# Reverse the list
names.reverse()
print(f'Reverse the list: {names}')



# Execute these file only when these file is run
if __name__ == "__main__":
    pass
