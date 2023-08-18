from inventory import Inventory
from player import Human
from items import WoodenSword
from items import DwarvianBookPage
from combat import Combat_Engine
from enemies import Level_One_Dragon
from room import Foyer

foyer = Foyer


player = Human(name= "Cai", race = "Human")

foyer.print_room(player)
# dragon = Level_One_Dragon()

# wooden_sword = WoodenSword()
# # paper = DwarvianBookPage()

# player.equip_weapon(wooden_sword)

# # # # inventory = Inventory()


# # # player.inventory.add_item("Weapon", wooden_sword)
# # # player.inventory.add_item("Paper Object", paper)
# # # player.display_player_inventory()


# # # inventory.display_inventory(player, paper)

# # # category_selection = inventory.inventory_menu()
# # # inventory.display_inventory_new(category_selection)



# # # print("Initial Inventory:")
# # # inventory.display_inventory()

# combat_engine = Combat_Engine()
# combat_engine.perform_combat(player, dragon)