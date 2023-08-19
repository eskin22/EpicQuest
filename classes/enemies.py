import random
from colorama import init
import os
init()
from colorama import Fore, Back, Style
from _util import create_textbox
from _util import get_random_attribute
# from testing_dragon import print_enemy_anscii
class Enemy():
    def __init__(self):
        self.enemy_type = None
        self.hp_min = None
        self.hp_max = None
        self.enemy_hp = None
        self.enemy_phrases = None
        self.enemy_attack_types = {}
       
       
    # displaying enemy info
    def display_enemy_info(self):
        enemy_stats = [
            Back.LIGHTRED_EX + Fore.LIGHTWHITE_EX + Style.BRIGHT + f"\033[1m{self.get_enemy_type()} INFO:",
            Back.LIGHTRED_EX + Fore.LIGHTWHITE_EX + Style.BRIGHT + f"- Enemy HP: {self.enemy_hp}",
            Back.LIGHTRED_EX + Fore.LIGHTWHITE_EX + Style.BRIGHT + f"- Enemy Attack Power: {self.enemy_attack_strength}",
            Back.LIGHTRED_EX + Fore.LIGHTWHITE_EX + Style.BRIGHT + f"{self.print_enemy_anscii()}"
        ]

        create_textbox(enemy_stats, background_color= Back.LIGHTRED_EX)


    # setting the random attack
    def set_random_attack(self, random_attack):
        self.random_attack = random_attack

    # Setting random phrase for enemy to say
    def get_random_phrase(self):
        return random.choice(self.enemy_phrases)


    def enemy_attack(self):
        print("\n-------------------------------------------")
        print(Fore.LIGHTRED_EX + f"'{self.get_random_phrase()}'")
        print("-------------------------------------------\n")
        print(Fore.LIGHTRED_EX + f"\033[1mYou have been struck with {self.random_attack}!")
        print(Fore.LIGHTRED_EX + f"\033[1mEnemy has done {self.enemy_attack_strength} damage!\n")
        
        


    # Get a random enemy phrase from a list of enemy phrases
    def get_random_phrase(self):
        return random.choice(self.enemy_phrases)

    # setter methods
    def set_enemy_type(self, enemy_type):
        self.enemy_type = enemy_type

    def set_enemy_attack_power(self, enemy_attack_power):
        self.enemy_attack_power = enemy_attack_power
    
    def set_enemy_hp(self, enemy_hp):
        self.enemy_hp = enemy_hp
        
    def set_enemy_phrase(self, enemy_phrase):
        self.enemy_phrase = enemy_phrase

    def set_random_attack(self, random_attack):
        self.random_attack = random_attack

    def set_enemy_attack_strength(self, enemy_attack_strength):
        self.enemy_attack_strength = enemy_attack_strength

    # Getter methods 
    def get_enemy_type(self):
        return self.enemy_type
    
    def get_enemy_attack_power(self):
        return self.enemy_attack_power
    
    def get_enemy_hp(self):
        return self.enemy_hp
    
    def get_enemy_attack_strength(self):
        random_attack = random.choice(list(self.enemy_attack_types.keys()))
        attack_strength = self.enemy_attack_types[random_attack]
        self.enemy_attack_strength = attack_strength
        return random_attack, attack_strength, self.enemy_attack_strength
    
    def print_enemy_anscii(self):
        source = os.getcwd()
        os.chdir(r'C:\Users\cdale\OneDrive\Documents\GitHub\EpicQuest')
        with open(f"classes/assets/enemy_images/{self.get_enemy_type().lower()}_anscii.txt", 'r') as art_file:
            enemy_picture = art_file.read()
            art_file.close()

        print(enemy_picture)
        os.chdir(source)
    
    



# Create a level one dragon
class Level_One_Dragon(Enemy):
    def __init__(self):
        super().__init__()
        self.enemy_type = "DRAGON"
        self.hp_min = 8
        self.hp_max = 50
        self.enemy_hp = get_random_attribute(self.hp_min, self.hp_max)
        self.enemy_prize = {"Gold": 5}
        self.enemy_phrases = ["You will parish weakling!", "Feel my fire", "You will die"]
        self.enemy_attack_types = {"Claw and bite attack": 5, 
                                   "Tail Swipe": 6, 
                                   "Wing Buffet": 7, 
                                   "Dragon Roar": 6, 
                                   "Fire Strike": 9}
        self.get_enemy_attack_strength()
        self.set_random_attack(random.choice(list(self.enemy_attack_types.keys())))
        


# Create a level one witch
class Level_One_Witch(Enemy):
    def __init__(self):
        super().__init__()
        self.enemy_type = "WITCH"
        self.hp_min = 11
        self.hp_max = 65
        self.enemy_hp = get_random_attribute(self.hp_min, self.hp_max)
        self.enemy_prize = {"Gold": 9}
        self.enemy_phrases = ["I call upon the ancient spirits to lend me their wisdom and guidance.", "Beware, for the powers that dance within me are both blessing and curse.", "Chaos and order dance in harmony, fueled by the incantations of my craft."]
        self.enemy_attack_types = {"Elemental Blast: The witch harnesses the power of the elements, launching a focused blast of elemental energy.": 7, 
                                   "Arcane Blast: The witch unleashes a concentrated burst of raw arcane energy, dealing pure magical damage.": 10, 
                                   "Curse of Weakness: The witch casts a debilitating curse upon you, draining your strength": 7, 
                                   "Transmutation Bolt: The witch cast you with a spell, tranforming you into a small, unrecognizable creature.": 5, 
                                   "Hexing Curse: The witch strikes you with a hexing curse. You notice your skin start to turn black, and a decrease in strength.": 15}
        self.get_enemy_attack_strength()
        self.set_random_attack(random.choice(list(self.enemy_attack_types.keys())))


# create a level one undead
class Level_One_Undead(Enemy):
    def __init__(self):
        super().__init__()
        self.enemy_type = "UNDEAD"
        self.hp_min = 11
        self.hp_max = 70
        self.enemy_hp = get_random_attribute(self.hp_min, self.hp_max)
        self.enemy_prize = {"Gold": 12}
        self.enemy_phrases = ["Feel the icy embrace of eternal death.", "Your life force shall fuel my undying power.", "The grave calls to you, beckoning your eternal slumber."]
        self.enemy_attack_types = {"Haunting Wail: The undead creaure has released an ear-shattering shreak, damaging your sanity.": 6, 
                                   "Life Drain: To fuel their own life force, the undead creature has drained your life force.": 15, 
                                   "Unholy Ressurection: The undead creature calls an undead spirits from the after life. You are struck by the spirit!": 7, 
                                   "Cursed Strike: The undead curses their weapon with a dark force, causing you even more damage.": 8, 
                                   "Shadow Bolt: A shadow-like spirit strikes your soul draining your health!": 12}
        self.get_enemy_attack_strength()
        self.set_random_attack(random.choice(list(self.enemy_attack_types.keys())))




# Create a level one warlord
class Level_One_Warlord(Enemy):
    def __init__(self):
        super().__init__()
        self.enemy_type = "Warlord"
        self.hp_min = 7
        self.hp_max = 55
        self.enemy_hp = get_random_attribute(self.hp_min, self.hp_max)
        self.enemy_prize = {"Gold": 11}
        self.enemy_phrases = ["Kneel before your conqueror!", "Bow to me, for I am your ultimate ruler", "Resistance is futile; you will fall before my might!"]
        self.enemy_attack_types = {"War Cry: A mighty battlecry is unleashes! A samll group of followers assemble with blood thirsty eyes. A small attack is performed by each member.": 5, 
                                   "Frenzied Assault: Opponent's weapon is drawn. He approaches with a relentless speed. A flurry of powerful strikes comes your way.": 7, 
                                   "Commanding Aura: A strong sense of intimidation comes over you. Stuck in your place, the warlord attacks you with a series of strikes.": 7, 
                                   "Tactical Strike: Watch out! The warlord has found a weak point in your armor and forcefully strikes you with his weapon.": 8, 
                                   "Battlefield Control: YOu have entered the warlords trap!": 9}
        self.get_enemy_attack_strength()
        self.set_random_attack(random.choice(list(self.enemy_attack_types.keys())))

        

# create a level one cult leader
class Level_One_CultLeader(Enemy):
    def __init__(self):
        super().__init__()
        self.enemy_type = "Cult Leader"
        self.hp_min = 6
        self.hp_max = 40
        self.enemy_hp = get_random_attribute(self.hp_min, self.hp_max)
        self.enemy_prize = {"Gold": 20}
        self.enemy_phrases = ["Those who oppose us are blind to the greater purpose", "Open your mind and embrace the truth I offer.", "Sacrifice is necessary for our journey towards transcendence."]
        self.enemy_attack_types = {"Semon Attack: The cult leader summons a demon, which attacks you for 1 minute": 7, 
                                   "Curse of Despair: The cult leader has hit you with a powerful curse! You are now fully aware of all the darkness that exists in the world and filled with despair.": 6, 
                                   "Mind Control: The cult leader now has control of your mind! You begin attacking yourself for 10 seconds!": 9, 
                                   "Eldritch Blast: The cult leader has struck you with a bolt of dark energy! It was a direct attack!": 9, 
                                   "Divine Punishment: The cult leader has summoned the wrath of a cosmic force. You have been hit with divine energy, resulting in burns!": 10}
        self.get_enemy_attack_strength()
        self.set_random_attack(random.choice(list(self.enemy_attack_types.keys())))


# create a level one beat
class Level_One_Bear:
    def __init__(self):
        super().__init__()
        self.enemy_type = "BEAR"
        self.hp_min = 3
        self.hp_max = 40
        self.enemy_hp = get_random_attribute(self.hp_min, self.hp_max)
        self.enemy_prize = {"Gold": 0}
        self.enemy_phrases = ["ROAR", "GRRRRRRRR", "Rrrrrrrraaaaaaa"]
        self.enemy_attack_types = {"Claw and bite attack: The bear has struck you with his teeth and claws!": 7, 
                                   "Mauling swipe: The bear swipes you with his paws!": 6,
                                   "Savage maul: The bear commits a series of claw and bite attacks!": 10, 
                                   "Crushing slam: The bear rears up on its hind legs before forcefully slamming its massive body onto the ground, causing a shockwave that damage": 8, 
                                   "Territorial roar: The bear lets out a powerful roar, making you stumble back": 3}
        self.get_enemy_attack_strength()
        self.set_random_attack(random.choice(list(self.enemy_attack_types.keys())))




        
        
    # def death_prize(self, player):
    #     if self.enemy_hp <= 0:
    #         player.inventory += self.enemy_prize
    #         print(f"Congrats! {player.name} you have gained {self.enemy_prize}")
    #     else:
    #         print(f"Sorry, {player.name}. Your journey is over.")

# dragon = Dragon()
# dragon.get_enemy_attack_strength()
