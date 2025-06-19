# Functions - as like print(), input() - re usable chunk of code
# Function name naming convention: all small char, separate word with _

 # greet_user() # we cannot call the function before defining


def greet_user():
    print ("Hi how are u")
    print("Thanks")


print ("start")

greet_user()

print("end")

# function with parameter

def greet_user_with_name(name):
    print ("Hi how are u" + name)
    print("Thanks")


greet_user_with_name("Abu")

# key word argument (position less argument). So when calling the function, we will specify param name and value
# with this by seeing the calling place we can easily understand the parameter detail + we can ignore the param order
# NOTE: keyword argument will come always after positional argument

def greet_user_with_full_name(first_name, last_name):
    print ("Hi how are u " + first_name + " " + last_name)
    print("Thanks")


greet_user_with_full_name(last_name = "G", first_name = "Abu")

# return statement from function to return value

def square(number):
    return number * number

print(square(3))