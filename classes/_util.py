# importing the subclasses
from combat import Combat_Engine
from colorama import init
init()
from colorama import Fore, Back, Style
import re
import random

# Method to create a player
def create_player(name, race):
    from player import Human, Elf, Dwarf, Orc, Gnome, Tiefling, Dragonborn, Goblin
    race_classes = {
        "Human": Human,
        "Elf": Elf,
        "Dwarf": Dwarf,
        "Orc": Orc,
        "Gnome": Gnome,
        "Tiefling": Tiefling,
        "Dragonborn": Dragonborn,
        "Goblin": Goblin      

    }

    player = race_classes.get(race)(name, race)

    return player


#method to run avoid combat
def run():
    print("You have decided to run.")
    return


 # Function for the player and an enemy to engage in combat    
# def engage_in_combat(self):
#     if self.player is None:
#         print("Player not created.")
#         return
    
#     enemy = Level_One_Witch()
#     print(f"You are now in combat with dangerous {enemy.get_enemy_type()}!")
#     combat_options = input("Would you like to...\n1. Run Away!\n2. Attack!\n")
#     if combat_options == "1":
#         run()
#         return
            
#     else:
#         combat_engine = Combat_Engine()
#         combat_engine.perform_combat(self.player, enemy)


#* This is a method to take a list of sentences to form a text box around them 

def visible_length(text):
    # Use a regular expression to remove ANSI escape sequences from the text
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    visible_text = ansi_escape.sub('', text)
    return len(visible_text)

import re

def visible_length(text):
    # Use a regular expression to remove ANSI escape sequences from the text
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    visible_text = ansi_escape.sub('', text)
    return len(visible_text)

def create_textbox(random_list, background_color=Back.WHITE):
    # Calculate the maximum visible width of the box based on the longest line in the entire list.
    visible_box_width = max(visible_length(line) for line in random_list)

    # Print the lines centered with the specified background color
    for line in random_list:
        padding = " " * (visible_box_width - visible_length(line))
        print(background_color + " " * 5 + line + padding + " " * 5 + Back.RESET)








def get_random_attribute(min, max):
        attribute = random.randint(min, max)
        return attribute




#* Read Paper Objects
# This method takes a user's input if they want to read an object or not
def look_at_paper_object(paper_object):
    read = input(f"Would you like to read the {paper_object.name}\n1. Yes\n2. No")

    if read == "1":
        print("---------------------------------------------------------")
        print(f"{paper_object.content}")
        print("---------------------------------------------------------")
        
    else: 
        pass


4

  









    



