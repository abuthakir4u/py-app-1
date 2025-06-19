# Printing the character sequence in the string
for item in 'Python':
    print(item)

# Printing the list of string
for item in ['Mosh', 'John', 'Sar']:
    print (item)

# Printing the list of integer
for item in [1, 2, 3, 4]:
    print (item)

print ('.....................')

# range function - it will generate a list of object which we can iterate
for item in range(10):
    print (item)
print ('.....................')

for item in range(5, 10):
    print (item)
print ('.....................')

for item in range(5, 10, 2):
    print (item)
print ('.....................')

#########################
# Nested loop - example to print the coordinates
for x in range(4):
    for y in range(3):
        print (f'({x}, {y})')

# with nested loop printing the F character in terminal
numbers1 = [5, 2, 5, 2, 2]
for number in numbers1:
    print('x' * number)

print ('.....................')

numbers2 = [5, 2, 5, 2, 2]
for number in numbers2:
    output = ''
    for count in range(number):
        output += 'x'
    print(output)
