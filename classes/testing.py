from inventory import Inventory
from player import Human
from items import WoodenSword
from items import DwarvianBookPage


player = Human(name= "Cai", race = "Human", weapon=None) 

wooden_sword = WoodenSword()
paper = DwarvianBookPage()

# inventory = Inventory()


player.inventory.add_item("Weapon", wooden_sword)
player.inventory.add_item("Paper Object", paper)
player.display_player_inventory()


# inventory.display_inventory(player, paper)

# category_selection = inventory.inventory_menu()
# inventory.display_inventory_new(category_selection)



# print("Initial Inventory:")
# inventory.display_inventory()



