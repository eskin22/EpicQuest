# from enemies import Enemy
# from enemies import Level_One_Dragon
# from enemies import Level_One_Witch
# from enemies import Level_One_Bear
# from enemies import Level_One_CultLeader
# from enemies import Level_One_Undead
# from enemies import Level_One_Warlord
from chest import Chest_One
from chest import Chest
from miscellaneous_room_items import Table_One
from combat import Combat_Engine
# from items import Dwarvian_book_page
from colorama import init
init()
from colorama import Fore, Back, Style
from _util import create_textbox


class Tile:
    def __init__(self):
        self.description = None

    def print_description(self):
        return self.description
    
    def interact(self):
       pass

class Empty_Tile(Tile):
    def __init__(self):
        super().__init__()
        self.description = Fore.YELLOW + "\033[1m\nThis tile is empty! Keep searching!\n\033[0m"

    def print_description(self):
      return self.description
    
    def interact(self):
        return

        

# Create an enemy tile
class Enemy_tile(Tile):
    def __init__(self, enemy):
        super().__init__()
        self.enemy = enemy
        self.description = Fore.RED + "\033[1m\nOh no! An enemy!\n\033[0m"

    def print_description(self):
        return self.description

    def interact(self, player):
        print(f"A {self.enemy.enemy_type} IS IN FRONT OF YOU. YOU ARE NOW IN COMBAT.\n")
        combat = Combat_Engine()
        combat.perform_combat(player, self.enemy)


class Chest_Tile(Tile):
    def __init__(self, chest):
        super().__init__()
        self.chest = chest
    
    def chest_interact(self):
        self.chest.show_chest_description()
        self.chest.open_chest()


class Table_Tile(Tile):
    def __init__(self, table):
        super().__init__()
        self.table = table

    def table_interact(self):
        self.table.show_table_description()


class Random_Paper_Tile(Tile):
    def __init__(self, paper):
        super().__init__()
        self.paper = paper

    def interact(self):
        self.paper.look_at_paper_object()


# random_table = Table_One()
# table_tile = Table_Tile(random_table)
# table_tile.table_interact()




    
       


