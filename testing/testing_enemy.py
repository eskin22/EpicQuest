# append sys path to access the class files
import sys, os
sys.path.append('../EpicQuest')

# import player class
from classes.player import Player

# create player object
player = Player("Chad", "Fuck")

# define basic enemy class
class Enemy():
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# create enemy object 
goblin = Enemy("Goblin", 25)

player.attack(goblin)