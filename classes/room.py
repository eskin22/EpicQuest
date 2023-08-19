# Parent class for rooms
import numpy as np
from tiles import Empty_Tile
from tiles import Enemy_tile
from tiles import Table_Tile
from tiles import Random_Paper_Tile
from enemies import Level_One_Dragon
from items import DwarvianBookPage
from tiles import WeaponTile
from items import WoodenSword
from items import SteelSword
from colorama import init
init()
from colorama import Fore, Back, Style
class Room:
    def __init__(self, width, height):
        self.name = None
        self.description = None
        self.height = height
        self.width = width
        self.tiles = np.empty((height, width), dtype=object)


class Foyer(Room):
    def __init__(self):
        super().__init__(width=8, height=8)
        self.name = "Foyer"
        self.description = Fore.LIGHTWHITE_EX + "\033[1mYou have entered the foyer.\nYou notice the room is in complete disarray. It is evident that a fight has taken place here...\033[0m\n"
        

        print(Fore.MAGENTA + f"\n{self.description}") # Set the text to a light Cyan

        # Initialize all tiles as Empty_Tile
        
        for i in range(self.height):
            for j in range(self.width):
                self.tiles[i, j] = Empty_Tile()
                
                self.tiles[6, 1] = Enemy_tile(Level_One_Dragon())
                self.tiles[2, 3] = Random_Paper_Tile(DwarvianBookPage())
                self.tiles[3,3] = WeaponTile(WoodenSword())
                # self.tile[1,3] = WeaponTile(SteelSword())

    def print_room(self, player):
        for i in range(self.height):
            for j in range(self.width):
                tile = self.tiles[i][j]
                if i == player.player_y and j == player.player_x:
                    print(Fore.GREEN + '★', end='      ')
                 
                
                elif isinstance(tile, Enemy_tile):
                    print(Fore.RED + '✖', end='      ')
               
            
                elif isinstance(tile, Random_Paper_Tile):
                    print(Fore.BLUE + '⁇', end='      ')
                  
               
                elif isinstance(tile, WeaponTile):
                    print(Fore.LIGHTYELLOW_EX + "⁇", end ='      ')
                    

                else:
                    print (Fore.WHITE + '▢', end='      ')

            print(Style.RESET_ALL)
          