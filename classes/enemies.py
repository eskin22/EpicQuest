import random
class Enemy():
    def __init__(self):
        self.enemy_type = None
        self.attack_power_min = None
        self.attack_power_max = None
        self.enemy_attack_power = None
        self.hp_min = None
        self.hp_max = None
        self.enemy_hp = None
        self.enemy_phrases = None

    def get_random_attribute(self, min, max):
        attribute = random.randint(min, max)
        return attribute

    # get a random hp for each enemy class
    def get_random_hp(self):
        self.enemy_hp = random.randint(self.hp_min, self.hp_max)
        return self.enemy_hp
    
    # get a random attack power for each enemy class
    def get_random_attack_power(self):
        self.enemy_attack_power = random.randint(self.attack_power_min, self.attack_power_max)
        return self.enemy_attack_power

    # Get a random enemy phrase from a list of enemy phrases
    def get_random_phrase(self):
        return random.choice(self.enemy_phrases)

    def combat(self, player):
        print(f"{self.enemy_type} is attacking {player.name}.")
        print(f"{self.enemy_type}\nHP : {self.enemy_hp}\nAttack Power : {self.enemy_attack_power}")
        while player.hp > 0:
            player.hp -= self.enemy_attack_power
            print(f"{self.get_random_phrase()}")
            print(f"Oh no! Watch your back. The {self.enemy_type} has done {self.enemy_attack_power} damage.")

        if player.hp <= 0:
            print(f"Sorry! {player.name} you have been defeated by the {self.enemy_type}.")

    # setter methods
    def set_enemy_type(self, enemy_type):
        self.enemy_type = enemy_type

    def set_enemy_attack_power(self, enemy_attack_power):
        self.enemy_attack_power = enemy_attack_power
    
    def set_enemy_hp(self, enemy_hp):
        self.enemy_hp = enemy_hp
        
    def set_enemy_phrase(self, enemy_phrase):
        self.enemy_phrase = enemy_phrase

    # Getter methods 
    def get_enemy_type(self):
        return self.enemy_type
    
    def get_enemy_attack_power(self):
        return self.enemy_attack_power
    
    def get_enemy_hp(self):
        return self.enemy_hp
    
    def get_enemy_phrase(self):
        return self.enemy_phrase    

class Dragon(Enemy):
    def __init__(self):
        super().__init__()
        self.enemy_type = "Dragon"
        self.attack_power_min = 1
        self.attack_power_max = 11
        self.enemy_attack_power = self.get_random_attribute(self.attack_power_min, self.attack_power_max)
        self.hp_min = 5
        self.hp_max = 50
        self.enemy_hp = self.get_random_attribute(self.hp_min, self.hp_max)
        self.enemy_prize = {"Gold": 5}
        self.enemy_phrases = ["I am Smaug", "Feel my fire", "You will die"]
        
    def death_prize(self, player):
        if self.enemy_hp <= 0:
            player.inventory += self.enemy_prize
            print(f"Congrats! {player.name} you have gained {self.enemy_prize}")
        else:
            print(f"Sorry, {player.name}. Your journey is over.")
