# Classes in Python
from xmlrpc.client import Boolean

# Basic types
# Numbers
# Strings
# Boolean
#
# Complex types
# Lists
# Dictionaries
#
# Custom Types
# Class

# Class for points
# Class Naming convention is camelcase
# Variable naming convention is all small char and _ for word separate

class Point:
    def move(selfs):
        print ("move")

    def draw(self):
        print("draw")

# Creating an object
point1 = Point()
point1.draw()
point1.move()

#Attribute of an object
point1.x = 10
point1.y = 20
print(point1.x)

#Creating another object, point1 attribute won't be available in point2
point2 = Point()
point2.move()
#print(point2.x) # won't be available


