# Text Based Adventure game

var = "Mysterious Forest"
print(var.center(50, '='))

print("You are lost in a \"Mysterious Forest\", \nyou found an elf😇 which agreed to help you through journey")
print("Elf: you have to find heart of forest to get out to human world")

print("You have 3 routes infront, choose right one\n1. Sea\n2. Planes\n3. Mountain")
choice = int(input("Enter your choice : "))

while True:
    if choice == 1:
        print("You are food to sharks 🦈")
        choice = int(input("Enter your choice : "))
        continue
    elif choice == 2:
        print("You survived 🎊 Find the key 🔑")
        break
    elif choice == 3:
        print("Burnt by dragon breath 🐲")
        choice = int(input("Enter your choice : "))
        continue
    else:
        print("Choose a valid number : ")
        choice = int(input("Enter your choice : "))
        continue

print("🕺🏻 You are a step closer to your destination 💃🏻")
print("Choose the right box to open heart of forest,\n1. Box1\n1. Box2\n1. Box3")

boxChoice = int(input("Choose your box🔮 : "))
while True:
    if boxChoice == 1:
        print("Help!!! Snakesss 🐍")
        boxChoice = int(input("Enter your choice : "))
        continue
    elif boxChoice == 3:
        print("Key obtained 🔑")
        break
    elif boxChoice == 2:
        print("ochh!!! Bee stings 🐝")
        boxChoice = int(input("Enter your choice : "))
        continue
    else:
        print("Choose a valid number : ")
        boxChoice = int(input("Enter your choice : "))
        continue

print("Elf : I appriciate your bravery, you are the first human to pass the forset")
print("The key gets inserted🔒\nportal Opens🔓\nElf : Take care my friend👋🏻\nBack to home🏠\nYou win!!!! 🏆")