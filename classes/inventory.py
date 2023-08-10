from colorama import init
init()
from colorama import Fore, Back, Style
from items import WoodenSword
from items import IronSword
from items import PaperObject



#* This is an inventory class
    #Players can 

class Inventory:
    def __init__(self):
        self.inventory = {
            "Weapon": [],
            "Paper Object": [],
            "Potion": []
        }

    # This function adds an item to an item type list
    def add_item(self, item_type, item):
        if item.item_type == "Weapon" or item.item_type == "Paper Object" or item.item_type == "Potion":
            item_list = self.inventory.get(item_type, [])
            item_list.append(item)
            self.inventory[item_type] = item_list

    def add_item_new(self, item):
        self.inventory[item.item_type].append(item)

    def drop_item_new(self, item):
        self.inventory[item.item_type].remove(item)

    # # This function delets an item from a list
    # def delete_item(self, item_list, item_number):
    #      if 1 <= item_number <= len(item_list):
    #         removed_item = item_list.pop(item_number - 1)
    #         print(f"{removed_item.name} has been removed from your inventory.")
    #      else:
    #         print("Invalid item number.")
    
    # This function prompts a player to choose a category of item 
    # def display_inventory(self, player, paper_object):

    #     # define category keys
    #     categories = {
    #         "1" : "Weapon",
    #         "2" : "Paper Objects",
    #         "3" : "Potions"
    #     }

    #     while True:
    #         choose_category = input(Fore.LIGHTWHITE_EX + "\033[1mWhich category would you like to view?\033[0m\n 1. Weapon\n 2. Paper Objects\n 3. Potions\n")

    #         if choose_category == "1":
    #             self.display_category(categories.get(choose_category))
    #             inventory_options = input(Fore.LIGHTWHITE_EX + "\033[1m\nHow would you like to continue?\033[0m\n 1. Inspect an item\n 2. Choose a different category\n 3. Exit menu\n")
    #             if inventory_options == "1":
    #                  self.inspect_weapon(categories.get(choose_category), player)

    #         elif choose_category == "2":
    #             self.display_category(categories.get(choose_category))
    #             inventory_options = input(Fore.LIGHTWHITE_EX + "\033[1m\nHow would you like to continue?\033[0m\n 1. Inspect an item\n 2. Choose a different category\n 3. Exit menu\n")
    #             if inventory_options == "1":
    #                  self.inspect_paper_object(categories.get(choose_category), paper_object)

    #         elif choose_category == "3":
    #             pass
            
    #         else:
    #             print("Invalid choice. Please select a valid option.")

            # if choose_category in categories:
            #     self.display_category(categories.get(choose_category))
            # else:
            #     print("Invalid choice. Please select a valid option.")
            #     continue

            # inventory_options = input(Fore.LIGHTWHITE_EX + "\033[1m\nHow would you like to continue?\033[0m\n 1. Inspect an item\n 2. Choose a different category\n 3. Exit menu\n")

            # if inventory_options == "1":
            #     if choose_category == "Weapon":
            #         self.inspect_weapon(categories.get(choose_category), player)
                
            #     elif choose_category == "Paper Object":
            #         self.inspect_paper_object(categories.get(choose_category), paper_object)

            #     else:
            #         pass
            
            
            # elif inventory_options == "2":
            #     continue  # This will loop back to choosing a category
            # elif inventory_options == "3":
            #     break  # Exit the inventory menu
            # else:
            #     print("Invalid choice. Please select a valid option.")


    # This displays the Category item and it's list of items
    # def display_category(self, category):
    #     items = self.inventory.get(category)
    #     if not items:
    #         print(Back.LIGHTWHITE_EX + Fore.BLACK + f"No items found in the {category} category.")
    #     else:
    #         print(Fore.LIGHTWHITE_EX + f"\033[1m\n{category}:\033[0m")
    #         for index, item in enumerate(items, start=1):
    #             print(f" {index}. {item.name}")

    
    
    # # This function asks a player if they would like to inspect an item
    # def inspect_weapon(self, category, player):
    #     item_list = self.inventory.get(category)

    #     item_number = int(input(Fore.LIGHTWHITE_EX + "\033[1m\nChoose the number item you'd like to inspect:\033[0m\n"))
    #     if 1 <= item_number <= len(item_list):
    #         selected_item = item_list[item_number - 1]
    #         print(Fore.LIGHTWHITE_EX + f"\nInspecting {selected_item.name}:\n")
    #         print("----------------------------------------------------------------------------------------------------------------------")
    #         print(f"{selected_item.description}.\nItem Damage:{selected_item.damage}\nItem Weight:{selected_item.weight}")
    #         print("----------------------------------------------------------------------------------------------------------------------")
    #         item_usage = input(Fore.LIGHTWHITE_EX + "\033[1mWhat would you like to do with this item?\033[0m\n1. Use Item\n2. Drop Item\n3. Nothing\n ")
    #         if item_usage == "1":
    #             player.equip_weapon(selected_item)
    #         elif item_usage == "2":
    #             self.delete_item(item_list, item_number)
    #         else:
    #             pass
    #     else:
    #         print("Invalid item number.")


    # def inspect_paper_object(self, category, paper_object):
    #     item_list = self.inventory.get(category)

    #     item_number = int(input(Fore.LIGHTWHITE_EX + "\033[1m\nChoose the number item you'd like to inspect:\033[0m\n"))
    #     if 1 <= item_number <= len(item_list):
    #         selected_item = item_list[item_number - 1]
    #         print(Fore.LIGHTWHITE_EX + f"\nInspecting {selected_item.name}")
    #         paper_object.look_at_paper_object()

    def inventory_menu(self):
        categories = {
            "1" : "Weapon",
            "2" : "Paper Object",
            "3" : "Potions"
        }
        for i, key in enumerate(self.inventory.keys()):
            print(f"{i+1}. {key}")
        category = input("Please select a category: ")
        # do bounds checking logic here
        category = categories.get(category)
        return category

    def display_inventory_new(self, category):
        for i, item in enumerate(self.inventory[category]):
            print(f"{i+1}. {item.name}")
        # selection = input("What would you like to do? (type command $ins to inspect)")
        # selection = "$ins 1"
        # if selection[:4] == '$ins':
        #     self.inspect_new(category, int(selection[5:]))








            
            



    