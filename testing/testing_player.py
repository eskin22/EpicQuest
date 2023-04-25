
# append sys path to access the class files
import random
import sys, os
sys.path.append('../EpicQuest')

# import player class
from classes.enemies import Dragon

# define basic enemy class
class Player():
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# create dragon object with attributes
dragon = Dragon()

# create player object
chad = Player("Chad", 45)

# call combat method on dragon object, passing in player object
dragon.combat(chad)

# print(dragon.get_random_phrase())
# print(dragon.test())

