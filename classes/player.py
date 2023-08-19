# Import colorama
from colorama import init
init()
from colorama import Fore, Back, Style

# import tiles assets
from tiles import Empty_Tile
from tiles import Enemy_tile
from tiles import Random_Paper_Tile
from inventory import Inventory
from _util import create_textbox
from _util import look_at_paper_object
from items import PaperObject
from items import SteelSword
from tiles import WeaponTile
# from _util import options_menu


# Better Comments
#* Highlight important comments
#! Indicate deprecated or dangerous code
#? Brainstorm future implementaitons/optimizations
#TODO Add notes for things you want to add in the short term
# Regular comment

#* This file defines the player class
# The player class defines different character races that the player can choose in the beginning of the game. This is done in the util.py
# in the create_player function. It also controls the player movements. 



#* This is the parent class for the players.
class Player:
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.attack_power = None
        self.hp = None
        self.character = None
        self.attack_types = {}
        self.mana = None
        self.player_x = None
        self.player_y = None
        self.equipped_weapon = None
        self.weapon_power = None
        self.inventory = Inventory()


    
    #* This method displays player information
    def display_info(self):
        player_stats = [
            Back.WHITE + Fore.GREEN + Style.BRIGHT + f'{self.name.upper()} INFO:',
            Back.WHITE + Fore.BLACK + Style.BRIGHT + f'- Race: {self.race}',
            Back.WHITE + Fore.BLACK + Style.BRIGHT + f'- HP: {self.hp}',
            Back.WHITE + Fore.BLACK + Style.BRIGHT + f'- Attack Power: {self.attack_power}',
            Back.WHITE + Fore.BLACK + Style.BRIGHT + f'- Mana: {self.mana}',
        ]

        create_textbox(player_stats, background_color=Back.WHITE)
 
 
 
 
 
 
 
 
 #* This is a method used for attacking the enemy
    def attack(self):

        # The method uses a for loop and enumerate to iterate over the attack type keys and display them with corresponding numbers.
        print("\n")

        # Prompts the player for input on how they would like to attack.
        while True: 
            selected_attack_style = int(input(Fore.BLUE + "\033[1mHow would you like to attack?\n1. Weapon Attack\n2. Player Attack\n"))
            if selected_attack_style == 1:
                if self.equipped_weapon is not None:
                    print(f"{self.equipped_weapon.name}")
                    weapon_info = self.equipped_weapon.display_weapon()
                    print(Fore.LIGHTYELLOW_EX + f"Enemy has been struck with your {self.equipped_weapon.name}.")
                    attack_power = self.equipped_weapon.damage 
                    total_attack_power = attack_power + self.weapon_power
                    print(Fore.LIGHTYELLOW_EX + f"You have done {total_attack_power} damage!")
                    total_mana = self.mana - (attack_power / 1.2)
                    print(Fore.LIGHTYELLOW_EX + f"Player Mana: {total_mana}\n")

                    return total_attack_power
                else:
                    print("You do not have a weapon equipped. Choose another option.")

        # Loops through attack methods and prints them out
            elif selected_attack_style == 2:
                for i, key in enumerate(self.attack_types.keys()):
                    print(Fore.WHITE + f"\n{i+1}. {key}")

                selected_attack_display_index = int(input(Fore.BLUE + "\033[1m\nHow would you like to attack?"))
                selected_attack_real_index = selected_attack_display_index - 1
                attack_type_keys = list(self.attack_types.keys())
                selected_attack_string_key = attack_type_keys[selected_attack_real_index]
                print(Fore.LIGHTYELLOW_EX + f"\nEnemy has been struck with {selected_attack_string_key}")
                attack_power = self.attack_types.get(selected_attack_string_key)
                total_attack_power = self.attack_power + attack_power
                print(Fore.LIGHTYELLOW_EX + f"You have done {total_attack_power} damage!")
                total_mana = self.mana - (attack_power / 1.2)
                print(Fore.LIGHTYELLOW_EX + f"Player Mana: {total_mana}\n")
        

                return total_attack_power

                
            

            else:
                print("You have entered an invalid number. Try again.")

   
   
   
    #* Player_Menu 
        # This will be a menu that will ask the player if they want to move, view their stats, or view their inventory.
    def player_menu_bar(self, room):
        while True:
            player_options = input(
            Fore.LIGHTWHITE_EX
            + "\nWhat would you like to do? \n1. Move \n2. View your stats \n3. View your inventory \n4. View room\n"
        ).strip()
            

            if player_options == "1":
                self.player_movements(room)
            
            elif player_options == "2":
                self.display_info()
 
            elif player_options == "3":
                self.display_player_inventory()
            
            elif player_options == "4":
                room.print_room(self)

         
            else:
                print("Invalid option. Please choose a valid option.")
  
   
    
    #* Handles the player movements
    def player_movements(self, room):
         current_position = [self.player_x, self.player_y]

         # While the player is still in the room, this will keep running
         move = input(Fore.LIGHTCYAN_EX + "\033[1mHow would you like to move?\033[0m" + Fore.LIGHTCYAN_EX+ "\n1. Up" + Fore.LIGHTCYAN_EX + "\n2. Down" + Fore.LIGHTCYAN_EX + "\n3. Right" + Fore.LIGHTCYAN_EX + "\n4. Left: ")
           

         new_position_x = self.player_x
         new_position_y = self.player_y

    #         # If the player enters 1, the player will move forward
         if move == "1":
                new_position_x -= 1 
                print(new_position_x, new_position_y)

    #         # If the player enters 2, the player will move backward
         elif move == "2":
                new_position_x += 1
                print(new_position_x, new_position_y)

    #         # If the player enters 3, the player will move up
         elif move == "3":
                new_position_y += 1  # Right
                print(new_position_x, new_position_y)

    #         # If the player enters 4, the player will move down
         elif move == "4":
                new_position_y -= 1  # Left
                print(new_position_x, new_position_y)

    #         # If the player enters a number that is not 1, 2, 3, or 4, the move will be invalid.
         else:
                print("Invalid move! Please try again.")


            
    #         # Check if the new_position is valid and within the bounds of the room
         if (0 <= new_position_x < room.height) and (0 <= new_position_y < room.width):
    #         # Move the character to the new position
                room.tiles[self.player_x, self.player_y] = Empty_Tile()
                self.player_x = new_position_x  # Update the player's position in the Player class
                self.player_y = new_position_y

    #             #Find the new tile
                new_tile = room.tiles[self.player_x, self.player_y]
                print(f"Player moved to position: [{self.player_x, self.player_y}]")
                print(new_tile.print_description())

    #             #* Check to see if it is an enemy tile
    #                 # if it is an enemy tile, the player will engage in combat with the enemy that is called in the Enemy_Tile class
                if isinstance(new_tile, Enemy_tile):
                    new_tile.interact(self)

                if isinstance(new_tile, Random_Paper_Tile):
                    new_tile.interact()
                    new_tile.add_object_option(self.inventory)
                    self.display_player_inventory()

                if isinstance(new_tile, WeaponTile):
                    new_tile.interact(self, self.inventory)
                    self.display_player_inventory()
                    
              
            # The player is out of bounds, essentially, they have hit a "wall" in the room.
         else:
            print("You have hit a wall! Pick a different direction to move!")


    
    
    
    #* This method displays the Player Inventory
    def display_player_inventory(self):
        while True:
            category_selection = self.inventory.inventory_menu()
            self.inventory.display_inventory_new(category_selection)
            selection = input("\nWhat would you like to do? (type command $ins to inspect, type command $exit to exit menu.)")
            # # # selection = "$ins 1"
            if selection[:4] == '$ins':
                self.inspect_new(category_selection, int(selection[5:]))
            if selection[:5] == '$exit':
                break 
            else:
                print("You have entered an invalid response.")
                # maybe pass or break
                continue

    
    
   #* This method allows a user to inspect an item within the inventory 
    def inspect_new(self, category, item_selection):
        # start default actions dictionary which contains all actions that the player can perform on ANY item
        # key is a string of what the action is (this will be useful when we want to easily iterate through the keys of the actions dictionary to 
        # indicate to the player what actions can be performed; as an added benefit, this way we don't have to hard code a bunch of conditional logic
        # to indicate available player actions depending on item type--if we have a dictionary that maintains all the available actions, then we can,
        # for ANY item, just iterate through the list of available actions and define that list based on the type)
        actions = {
            f"Drop {category}" : self.inventory.drop_item_new
        }

        # using the category the player selected in the display_player_inventory method, we can access the list of items for the category they want to see and save it to
        # a variable for easy access and clarity
        item_list = self.inventory.inventory[category]

        # now we need to define player actions based on the item type or category they've selected. For example, if the player chooses to view weapons, we want them to be able to
        # equip those weapons, thus we add the equip method. Remember, we're creating an actions dictionary where the key is the string defining the action and the value of we 
        # access with that key will be the mapped function for performing that action in the backend; this is going to make things much more clear and easy to use later on as we add
        # many actions that the player can perform, it's also polymorphic
        if category == "Weapon":
            actions["Equip Weapon"] = self.equip_weapon

        elif category == "Paper Object":
            actions["Read Item"] = look_at_paper_object

        else:
            pass

        # now we get the selected item OBJECT based on the integer (index) that the user entered. Recall that each list of items is a list of Item objects, so we simply take the 
        # player selected index - 1 to access the Item object we're interested in to account for the fact that we add 1 when we're printing them out since it would be weird if the 
        # menu started with zero instead of 1 for someone who doesn't program
        selected_item = item_list[item_selection-1]

        # print out the inspect information that we want to show for every item regardlesss of its category (e.g. name, description, etc)
        print("----------------------------------------------------------------------------------------------------------------------")
        print(selected_item.description)

        # now, based on the category or item type, we want to indicate more or less information. For example, a weapon will have a damage attribute that we want to display to the user
        if category == "Weapon":
            print(f"\nItem Damage:{selected_item.damage}")
            print(f"Item Weight: {selected_item.weight}")
        elif category == "Paper Object":
            print(selected_item.item_description)
        else:
            pass
        print("----------------------------------------------------------------------------------------------------------------------")

        # now that the user has seen the inspection information for their selected item, we want to display the available actions that the player can perform based on the item type.
        # Remember that we've been defining this dictionary as the user has been looking at the items, so we can simply print out the keys (string descriptions of the actions) as a 
        # shorthand way of creating menu items!
        for i, action in enumerate(actions.keys()):
            print(f"{i+1}. {action}")

        # finally, we prompt the player asking what they want to do based on the actions available to them
        selection = int(input("What would you like to do now?"))

        # once the player has made a selection (an int as an index of the keys we showed them) we have to do some compressed logic to map that index to the actual key and function we need 
        # to perform. It would be kind of redundant and very difficult/messy to define a whole other dictionary mapping the string ints to the actions like we've done in the past because the list of actions 
        # changes based on the category of the item. So, instead, we use this compression logic to programmatically determine the function needed that is generic for any item category/list 
        # of available actions we may encounter

        # let's break it down into parts: we want to access our actions dictionary, and to do that we need a key. But we don't know what key to use because the selection was passed as an index.
        # so, we can use the 'actions.keys()' method to get a dictionary of the keys for the actions dictionary. Cool. Now, since we want to be able to use the index that the user passed, and can't 
        # use an index for a dictionary, we need to convert the returned dictionary object from 'actions.keys()' into a list. So, we just type-cast the actions.keys() as a list like so 
        # "list(actions.keys())". Great. Now we have a list of the keys in the same order that they were printed out to the player so we can finally use our index. So now we just index 
        # the "list (actions.keys())" using "[selection-1]". Remember, the former is actually just a list of the keys in the actions dictionary (i.e. our available actions) and the latter
        # is simply the selected index - 1 to account for the + 1 we added during the printout. Okay. Now we're accessing the actions dictionary with the key of the action that was selected by the player
        # so we end up with the function. If the player selected 1, we've mapped that one to "Drop Weapon" and have called "actions["Drop Weapon"]" which gives us the value "self.inventory.drop_weapon"
        # all we have to do now is add the necessary parameters for the method, which is the item we want to drop/equip. That's it!
        actions[list(actions.keys())[selection-1]](selected_item)




   
   
    #* This method is used so a player can equip a weapon
    def equip_weapon(self, weapon):
        if weapon.item_type == "Weapon":
            if self.equipped_weapon is not None:
                print(f"You have unequipped {self.equipped_weapon.name}.")
                self.inventory.add_item_new(self.equipped_weapon)
            
            self.equipped_weapon = weapon
            print(f"You have equipped {weapon.name}.")
            
        else:
            print("You can only equip weapons.")





#* This a the subclass Human, which is a race a player can choose
class Human(Player):
    def __init__(self, name, race):
        super().__init__(name, race)
        self.skills = "Humans are adaptable creatures. Although not the strongest, they can excel in a number of areas through learned behavior. Due to their lack of raw strength, humans are especially skilled in tools and in weapon combat."
        self.name = name
        self.race = race
        self.attack_power = 5
        self.hp = 90
        self.restore_hp = 90
        self.attack_types = {
            "Physical Attack": 6,
            "Tactical Attack": 12,
            "Combo Attack (Tactical Attack and Physical Attack)": 16,
            "Elemental Attack": 4}
        self.mana = 10
        self.player_x = 0
        self.player_y = 0
        self.equipped_weapon = None
        self.weapon_power = 15

#* This a the subclass Elf, which is a race a player can choose
class Elf(Player):
    def __init__(self, name, race):
        super().__init__(name, race)
        self.skills = "Blah, blah, blah"
        self.name = name
        self.race = race
        self.attack_power = 7
        self.hp = 85
        self.restore_hp = 85
        self.attack_types = {
            "Agility Attack": 6,
            "Illusion Attack": 11,
            "Stealth Attack": 10,
            "Elemental Attack": 12}
        self.mana = 15
        self.player_x = 0
        self.player_y = 0
        self.equipped_weaponweapon = None
        self.weapon_power = 7

#* This a the subclass Dwarf, which is a race a player can choose
class Dwarf(Player):
    def __init__(self, name, race):
        super().__init__(name, race)
        self.skills = "Blah, blah, blah"
        self.name = name
        self.race = race
        self.attack_power = 5
        self.hp = 105
        self.restore_hp = 105
        self.attack_types = {
            "Rage Attack": 9,
            "Axe Attack": 10,
            "Smithing Magic (Conjure a powerful weapon in battle)": 17,
            "Artillary Attack": 8
        }
        self.mana = 12
        self.player_x = 0
        self.player_y = 0
        self.weapon = None
        self.weapon_power = 17

#* This a the subclass Orc, which is a race a player can choose
class Orc(Player):
    def __init__(self, name, race):
        super().__init__(name, race)
        self.skills = "Blah, blah, blah"
        self.name = name
        self.race = race
        self.attack_power = 8
        self.hp = 95
        self.restore_hp = 95
        self.attack_types = {
            "Savage Strike": 10,
            "Charge Strike": 6,
            "Tribal Magic": 12,
            "War Cry": 8 

        }
        self.mana = 20
        self.player_x = 0
        self.player_y = 0
        self.equipped_weapon = None
        self.weapon_power = 15
        self.weapon_power = 12

#* This a the subclass Gnome, which is a race a player can choose
class Gnome(Player):
    def __init__(self, name, race):
        super().__init__(name, race)
        self.skills = "Blah, blah, blah"
        self.name = name
        self.race = race
        self.attack_power = 8
        self.hp = 85
        self.restore_hp = 85
        self.attack_types = {
            "Illusion and Deception strike": 12,
            "Gnome's Luck Attack": 6,
            "Stealth Attack": 9,
            "Agility Strike": 10
        }
        self.mana = 15
        self.player_x = 0
        self.player_y = 0
        self.equipped_weapon = None
        self.weapon_power = 6


#* This a the subclass Tiefling, which is a race a player can choose
class Tiefling(Player):
    def __init__(self, name, race, weapon):
        super().__init__(name, race)
        self.skills = "Blah, blah, blah"
        self.name = name
        self.race = race
        self.attack_power = 8
        self.hp = 98
        self.restore_hp = 98
        self.attack_types = {
            "Infernal Blast": 9,
            "Soul Harvest (Conjure souls to help you attack)": 14,
            "Fiery Aura Strike": 6, 
            "Demon's Rage (Transform into a demon for this turn, combining fire magic and energy from the underword)": 16
        }
        self.mana = 30
        self.player_x = 0
        self.player_y = 0
        self.equipped_weapon = None
        self.weapon_power = 5

#* This a the subclass Dragon, which is a race a player can choose
class Dragonborn(Player):
    def __init__(self, name, race):
        super().__init__(name, race)
        self.skills = "Blah, blah, blah"
        self.name = name
        self.race = race
        self.attack_power = 10
        self.hp = 90
        self.restore_hp = 90
        self.attack_types = {
            "Draconic Breath": 12, 
            "Draconic Roar": 8,
            "Dragonborn Magic Attack": 7, 
            "Draconic Heritage (Summon powers from your dragon ancestors)" : 16
        }
        self.mana = 15
        self.player_x = 0
        self.player_y = 0
        self.equipped_weapon = None
        self.weapon = 9
        
#* This a the subclass Tiefling, which is a race a player can choose       
class Goblin(Player):
    def __init__(self, name, race, weapon):
        super().__init__(name, race)
        self.skills = "Blah, blah, blah"
        self.name = name
        self.race = race
        self.attack_power = 6
        self.hp = 97
        self.restore_hp = 97
        self.attack_types = {
            "Sneak Attack": 7,
            "Goblin Shenanigans (Confuse your component and then strike)": 9,
            "Dirty Tricks Attacks (Use your surrounding resources to trick your opponent and then attack)": 8,
            "Goblin Rage Attack": 14
                                          }
        self.mana = 25
        self.player_x = 0
        self.player_y = 0
        self.equipped_weapon = None
        self.weapon_power = 6