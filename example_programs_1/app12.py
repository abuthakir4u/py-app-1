class Mammal:
    def walk(self):
        print ("walk")

class Dog(Mammal):
    def bark(self):
        print("Barking")

class Cat(Mammal):
    def sound_make(self):
        print('cat sound')

dogObj = Dog()
dogObj.walk()
dogObj.bark()

catObj = Cat()
catObj.walk()
catObj.sound_make()