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

    
    # Adding an item to the player inventory
    # def add_item_new(self, item):
    #         self.inventory[item.item_type].append(item)
    

    # This function adds an item to an item type list
    def add_item_new(self, item):
         options = input(Fore.LIGHTWHITE_EX + "\nWould you like to add the item?\n1. Yes\n2. No\n")
         while True:
            if options == "1":
                self.inventory[item.item_type].append(item)
            else: 
                break
             

    def drop_item_new(self, item):
         self.inventory[item.item_type].remove(item)



   
    def inventory_menu(self):
        categories = {
            "1" : "Weapon",
            "2" : "Paper Object",
            "3" : "Potions"
        }
        print("\n")
        print("----------------------------------------------------")
        while True:
            for i, key in enumerate(self.inventory.keys()):
                print(f"{i+1}. {key}")
            print("----------------------------------------------------")
            category = input("\nPlease select a category: ")
            if category not in "1" "2" "3":
                print("Please enter a valid number.")
            else:
                category = categories.get(category)
                return category
        

    def display_inventory_new(self, category):
        for i, item in enumerate(self.inventory[category]):
            print(f"{i+1}. {item.name}")








            
            



    