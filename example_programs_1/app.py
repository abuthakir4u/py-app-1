# Printing string
print ("Abuthakir")
print ('o----')
print (' ||||')
print('*' * 10) #It will print 10 times *

#############

# Variables
price = 10
print(price)
price = 20
print(price)

rating = 4.9
print(rating)

name = "Abuthakir"
print(name)

is_published = True
print(is_published)

Is_published = False  #Boolean value should start with Caps
print(Is_published) # Python is case sensitive, so is_published and Is_published are not same

#################

# Getting input from user

my_name = input("What is your name? ")
print ("hi " + my_name)  # + for concatenating
my_fav_color = input("What is your favorite color? ")
print("My fav color: " + my_fav_color)

#################

# Type conversion - int() for converting the string to integer, flot() for converting to floating number, bool() for boolean conversion

birth_year = input('Birth year') #input method will return the string which you input via console
age = 2025 - int(birth_year);
print(age)

print(type(birth_year)) #to print the type of the variable
print(type(age))

# script to convert the lbs to kg
weight_lbs = input('Enter weight (lbs): ')
weight_kgs = int(weight_lbs) * 0.45
print(weight_kgs)

########################
# Python String. Can be created with single and double quote

course = 'Python\'s course of beginners' #escaping character

course1 = "Python's course for beginners"

#Multiline string with three single or double quote

multiline_string = '''
how are you
Python's course for beginner
"My course"
'''
print(multiline_string)

# Getting character from string
test_string1 = 'This is the string for testing'
print(test_string1[1])
print(test_string1[-1]) # this index will start from last. This will start with 1 not from 0
print(test_string1[-2])

print(test_string1[0:3])  # return character from 0th index and return 3 characters
print(test_string1[0:]) # will return character from 0th index to all character in that string
print(test_string1[:5]) # will return string from 0th index to 5 characters
print(test_string1[:]) # return all character, used to copy/clone

test_string2 = test_string1[:] # copy the one string into another. This creates a slice of the entire string - essentially making a copy of the string.
print(test_string2)

test_string3 = test_string1 # This doesn't create a copy - it just makes both variables point to the same string object in memory.
# However, there's a subtlety here: because strings are immutable in Python, this difference rarely matters in practice. If you modify either string, Python will actually create a new string object anyway.

test_string4 = 'Another test string'
print(test_string4[1:-1]) # return string from 1st index to last character (excluding the last one)

# Formatted String
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
print(message)
msg = f'{first} [{last}]' #formatted string start with f and {} is the placeholder of the variable
print(msg)

# String methods

course01 = 'Python for Beginners'

print(len(course)) # finding the length of the string. This len function will find the list length as well
print(course01.upper()) # to get the string in upper character, and it won't modify the object value
print(course01.lower())

print(course01.find("P")) #find the index of the character in the given string, it is case-sensitive
print(course01.find('Beginners')) #to find the position of sequence of character/string

print(course01.replace('Beginners', 'Advanced')) #to replace the string
print(course01.replace('B', 'A')) #to replace a single character

#to find the character/string in a string
print('Beginner' in course01) #print the boolean based on string existed

#Note find() will return the index, in operator return boolean

# NOTE
# Methods are for object - upper() is a method
# len(), print() are general function and it is not tied with object

##################

# Arithmetic operations
print(10+3)
print(10*3)

# 2 kinds of division
print(10/3) # the result will be floating point number
print(10//3) # the result will be integer
print(10%3) # modulo
print(10**3) #power of

x = 10
x = x+3
x += 3 #augmented assignment same as the above statement
print(x)

# Operator precedence
x = 10 + 3 * 2

# order of precedence
# 1 Exponentation
# 2 multiplication or division
# 3 addition or subtraction
# parenthesis will change the order and it will have hight priority

y = 10 + 3 * 3 ** 2 # answer 22

####################

# Math function

val1 = 2.9
print (round(x))
print (abs(-2.9)) # return always positive number













