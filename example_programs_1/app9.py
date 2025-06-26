# Constructors get called when creating the object
# self is the first parameter of every class method

class Point:
    #Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print ("move")

    def dra(self):
        print("draw")


point1 = Point(10,20)
point1.dra()
point1.move()
print(point1.x)
point1.x = 100
print(point1.x)