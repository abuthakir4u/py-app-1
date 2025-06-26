# list of names
import numbers

names = ['abu', 'test', 'test2', 'test3']
print (names)
print (names[0])
print (names[1])
print (names[-1])

print('..............')
print (names[0:2])
print('..............')
print (names[2:])
print('..............')

# Modify the element
names[2] = 'updated value'
print(names)

# find the biggest value in the list
input_numbers = [1, 34, 2, 455, 43, 4565, 23,4,5,6];
big_number = input_numbers[0]
for number in input_numbers:
    if number > big_number:
        big_number = number
print(big_number)
print('..............')
# 2D Lists
# for example 3 x 3 matrix => list of list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
print(matrix[0][1])
#updating the 2d list
matrix[0][1] = 100
print(matrix)
print('..............')
for row in matrix:
    for item in row:
        print(item)

## List methods
list_of_number = [5, 2, 1, 5, 6, 7]
list_of_number.append(20) #adding item at last
print(list_of_number)
print('..............')
list_of_number.insert(0, 100) #inserting item at the specified index
print(list_of_number)
print('..............')
list_of_number.remove(5) #remove the item from a list
print(list_of_number)
print('..............')
list_of_number.pop() #remove the last item in the list
print(list_of_number)
print('..............')
#list_of_number.clear() # empty the list
print(list_of_number)
print('..............')
list_of_number.index(6) #The index of the first occurance of the item. If the element does not exist, it will throw error
print(list_of_number)
print('..............')
print (50 in list_of_number) # used to find the element existence in the list
print('..............')
print(list_of_number.count(5)) # return the count of the item in the list
print('..............')
print(list_of_number.sort()) #to sort the list. It will return None, and it will sort the original list itself
print(list_of_number)
print(list_of_number.reverse()) # for sorting descending
print('..............')
list_of_number1 = list_of_number.copy() #take a copy of the list

#Note: "None" is the object that is nothing/void

#####################
# Removing the duplicates from the list
input_num_list = [2, 2, 3, 6, 3, 4, 1]
unique_num_list = []
for number in input_num_list:
    if number not in unique_num_list:
        unique_num_list.append(number)
print(unique_num_list)


