# parent class
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal details")
        print("")
        print("Name : ", self.name)
        print("age : ", self.age)
        print("gender : ", self.gender)