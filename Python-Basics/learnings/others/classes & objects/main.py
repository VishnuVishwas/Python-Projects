class Dog:

    # # Attributes
    # attr1 = "mammal"
    # attr2 = "dog"

    # this class will be automatically called
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

    def __str__(self) -> str:
        print("This will print the content when a print is called.")

    def fun(self ,name):
        print("I'm a" , self.age)
        print("I'm ", self.age)
        print("My name is : ", name)

Rodger = Dog("Rodger", 8)
Pug = Dog("Pug", 5)
Rodger.fun("Tommy")
Pug.fun("Blacky")
