# Inheritance

class Mammal:
    def walk(self):
        print ("walk")

class Dog(Mammal):
    pass #to inform Python don't validate for empty class

class Cat(Mammal):
    pass #to inform Python don't validate for empty class

dogObj = Dog()
dogObj.walk()

catObj = Cat()
catObj.walk()