## Tuples - kine of a list, but it immutable - it will be created with ()
# it will have count and index methods

numbers = [1, 2, 3]
number_tuples = (1, 2, 3, 2, 3)
print(number_tuples.count(3)) #show the number occurrence of the nuber 3
print(number_tuples[1])

# number_tuples[0] = 10 # we cannot do this in tuples

#Unpacking with Tuples

coordinates = (1, 2, 3)
x, y, z = coordinates
print(x, y, z)

#Unpacking with List

coordinates_lists = [1,2,3,4]
a,b,c,d = coordinates_lists
print(a,b,c,d)

# Dictionaries - key value pair, define with {}. Key should be unique. Key can be number as well. Value can be anything. Key is case-sensitive
customer = {
    "name": "Abu",
    "age" : 30,
    "is_verified": True
}
print(customer)
print(customer["name"]) #accessing the element in dictionary
print(customer.get("name"))

print(customer.get("namex")) # return None, None - absense of value
print(customer.get("namex", "default name")) # return default value when it not exists

customer["name"] = "updated name"
print(customer)

customer["country"] = "US" #adding a new element in the dictionary

# Sample program to print the numbers is words
number_dictionary = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four"
}

input_num = "1233328"
for num_char in input_num:
    #print (number_dictionary[num_char])
    print(number_dictionary.get(num_char, "no word available"))

# program to convert emoji in sentences
message_input = input("> ")
words = message_input.split(" ")
emojis = {
    ":)" : "😊",
    ":(" : "😒"
}
output_txt = ""
for word in words:
    output_txt += emojis.get(word, word) + " "

print(output_txt)



