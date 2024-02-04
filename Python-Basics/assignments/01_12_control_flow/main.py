# Text Based Adventure game

forest_name = "Mysterious Forest"
print(forest_name.center(50, '='))

print("You are lost in a \"Mysterious Forest\", \nyou found an elf😇 which agreed to help you through the journey")
print("Elf: you have to find the heart of the forest to get out to the human world")

# Choosing a route
print("You have 3 routes in front, choose the right one\n1. Sea\n2. Plains\n3. Mountain")
choice = int(input("Enter your choice: "))

while True:
    if choice == 1:
        print("You are food for sharks 🦈")
        choice = int(input("Enter your choice: "))
        continue
    elif choice == 2:
        print("You survived 🎊 Find the key 🔑")
        break
    elif choice == 3:
        print("Burnt by dragon breath 🐲")
        choice = int(input("Enter your choice: "))
        continue
    else:
        print("Choose a valid number: ")
        choice = int(input("Enter your choice: "))
        continue

# Choosing a box
print("🕺🏻 You are a step closer to your destination 💃🏻")
print("Choose the right box to open the heart of the forest,\n1. Box1\n2. Box2\n3. Box3")

box_choice = int(input("Choose your box🔮: "))
while True:
    if box_choice == 1:
        print("Help!!! Snakesss 🐍")
        box_choice = int(input("Enter your choice: "))
        continue
    elif box_choice == 3:
        print("Key obtained 🔑")
        break
    elif box_choice == 2:
        print("Ouch!!! Bee stings 🐝")
        box_choice = int(input("Enter your choice: "))
        continue
    else:
        print("Choose a valid number: ")
        box_choice = int(input("Enter your choice: "))
        continue

print("Elf: I appreciate your bravery, you are the first human to pass the forest")
print("The key gets inserted🔒\nPortal Opens🔓\nElf: Take care my friend👋🏻\nBack to home🏠\nYou win!!!! 🏆")
