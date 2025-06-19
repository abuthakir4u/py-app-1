# Module is a separate file with reusable code
# We can use module to organize a project into different files
import math

print(math.pow(10, 2))
print(math.ceil(10.2))
print(math.ceil(10.8))
print(math.floor(10.8))

is_hot = False
is_cold = True

#########################

#if else block

if is_hot:
    print('it is hot')
elif is_cold:
    print('it is cold')
else:
    print('in it no hot or cold')

print('Enjoy your day block')

########################
# Logical operator

# AND: both
# OR: at least one
# NOT: Inverse the boolean value

has_high_income = True
has_good_credit = True

if has_good_credit and has_good_credit:
    print("Eligible for loan")
else:
    print ("Not eligible")

if not has_high_income:
    print("not high income")

age = 10
if age == 10:
    print('age is 10')

######################
# while loop

i =1
while i<=5:
    print (i)
    i +=1
else:
    print('loop ended')
print('done')

#######################