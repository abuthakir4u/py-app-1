# Python builtin modules

# Generating random number modules

import random


for i in range(3):
    print(random.random()) # random number between 0 and 1
    print(random.randint(10, 20)) # random number between 10 and 20

#picking the random list item
members = ['abu1', 'abu2', 'abu3']

leader = random.choice(members) #selecting random list item
print (leader)