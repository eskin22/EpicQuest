
#* this file defines the player class for the game

class Player():

    # init method requires player name and player class to create player object
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.attack_power = 5

    # method for attacking an enemy
    def attack(self, enemy):

        print(f"{self.name} is attacking {enemy.name}!\n")

        while enemy.hp > 0:
            enemy.hp -= self.attack_power
            print(f"{self.name} attacked {enemy.name} and did {self.attack_power} damage! {enemy.name} has {enemy.hp} HP remaining.\n")

            if enemy.hp <= 0:
                print(f"{enemy.name} has been defeated by {self.name}!\n")


