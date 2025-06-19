# Dice roll gam
import random

class Dice:
    def roll(self):
        dice1 = random.randint(0, 6)
        dice2 = random.randint(0, 6)
        # return (dice1, dice2) # to return tuple we can ignore the bracket
        return dice1, dice2

dice = Dice()
print(dice.roll())

# Note: PEP - Python Enhancement Proposal
# PEP 8: is one version of that proposal, which include coding indentation and other standards