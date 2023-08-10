from enemies import Enemy
from enemies import Level_One_Dragon
from enemies import Level_One_Witch
from enemies import Level_One_Bear
from enemies import Level_One_CultLeader
from enemies import Level_One_Undead
from enemies import Level_One_Warlord
import random
from _util import create_player
from _util import run
from room import Foyer
from colorama import init
init()
from colorama import Fore, Back, Style
from _util import create_textbox

# Creates the main game function
class Game:
    def __init__(self):
        self.player = None

    def intro(self):
        print(Back.MAGENTA + Fore.BLACK +"\033[1m                              EPIC QUEST                              \033[0m") #Text background Magenta, text color is dark green, text is bold
        print(Style.RESET_ALL)
        player_name = input(Fore.GREEN + "\033[1mInput character name: \033[0m") # Bold text
        race_input = input(Fore.GREEN + "\033[1m\nChoose character class:\033[0m" + Fore.WHITE + "\n1. Human" + Fore.CYAN + "\n2. Elf" + Fore.BLUE + "\n3. Dwarf" + Fore.LIGHTMAGENTA_EX + "\n4. Orc" + Fore.YELLOW + "\n5. Gnome" + Fore.LIGHTGREEN_EX + "\n6. Halfling" + Fore.LIGHTBLUE_EX + "\n7. Tiefling" + Fore.RED + "\n8. Dragonborn" + Fore.LIGHTCYAN_EX + "\n9. Goblin\n")
        print(Style.RESET_ALL)
        race_options = {
            "1": "Human",
            "2": "Elf",
            "3": "Dwarf",
            "4": "Orc",
            "5": "Gnome",
            "6": "Halfling",
            "7": "Tiefling",
            "8": "Dragonborn",
            "9": "Goblin"
        }

        #*Finds if the user input matches a race in the race_options dictionary for players
        if race_input in race_options:
            player_race = race_options[race_input]
        else:
            print("Invalid race chosen.")
            return
        

        #* create an instance of the player
        self.player = create_player(player_name, player_race)
        self.player.display_info()

    #* This is a function to place the instance of player within the Foyer class
        #Text has a green background with blue text. It is also bolded to make it easier for the person to read. 
    def start_dungeon(self):
        print("\n")
        start_of_dungeon = [
            Back.LIGHTRED_EX + Fore.WHITE + Style.BRIGHT + "-------------------------------------------------------------------------------------------------------------------------------------------------------------------",
            Back.LIGHTRED_EX + Fore.WHITE + Style.BRIGHT + "\033[1mYou have now arrived an abandoned dungeon. You have been sent by a clan of bandits.",
            Back.LIGHTRED_EX + Fore.WHITE + Style.BRIGHT + "\033[1mTwo-hundred years ago, the Dwarvian uprising against the humans and mages after years of enslavement.",
            Back.LIGHTRED_EX + Fore.WHITE + Style.BRIGHT + "\033[1mThe war is that of legend. You have heard the stories and the songs about the bloodshed, but it's not clear what is myth and what is real.",
            Back.LIGHTRED_EX + Fore.WHITE + Style.BRIGHT + "\033[1mHowever, there is one story told time and time again about the murder of Malgrom Voidreaver the Malovent.",
            Back.LIGHTRED_EX + Fore.WHITE + Style.BRIGHT + "                         ",
            Back.LIGHTRED_EX + Fore.WHITE + Style.BRIGHT + "\033[1mAccording to legend, deep within the dungeon the Drarvian commander, Thrain Rockhammer, slaughtered Voidreaver with his own enchanted Bane.",
            Back.LIGHTRED_EX + Fore.WHITE + Style.BRIGHT + "\033[1mAs the tension between the Dwarves and the Mages increases, both sides are searching for the bane, as it is said to contain the soul of Voidreaver himself.",
            Back.LIGHTRED_EX + Fore.WHITE + Style.BRIGHT + "\033[1mYour mission is to find the bane and return it to the bandits who have offered you a generous award.",
            Back.LIGHTRED_EX + Fore.WHITE + Style.BRIGHT + "-------------------------------------------------------------------------------------------------------------------------------------------------------------------"
        ]
        create_textbox(start_of_dungeon, background_color=Back.LIGHTRED_EX)
        foyer = Foyer()
        self.player.player_movements(foyer)





            


# calls the game class and corresponding functions
game = Game()
game.intro()
game.start_dungeon()







