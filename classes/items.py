#* Parent class for Weapons
from _util import get_random_attribute

class Item():
    def __init__(self):
        self.item_type = None
        self.name = None
        self.description = None
        self.weight = None

class Weapon(Item):
    def __init__(self):
        self.item_type = 'Weapon'
        self.weapon_type = None
        self.damage_min = None
        self.damage_max = None
        self.damage = None
        self.forge_type = None

#Child class of Weapons for different types of swords.
class Sword(Weapon):
    def __init__(self):
        super().__init__()
        self.weapon_type = 'Sword'


# Subclass for a Wooden SWord
class WoodenSword(Sword):
    def __init__(self):
        super().__init__()
        self.name = "Wooden Sword"
        self.description = "A wooden Sword. Most likely used for combat training, since it will deal little harm to opponent."
        self.damage_min = 2
        self.damage_max = 7
        self.damage = get_random_attribute(self.damage_min, self.damage_max)
        self.weight = 3
        self.forge_type = "Wood"


# Subclass for an Iron Sword
class IronSword(Sword):
    def __init__(self, type, name, description, damage_min, damage_max, damage, weight, forge_type):
        super().__init__(type, name, description, damage_min, damage_max, damage, weight, forge_type)
        self.name = "Iron Sword"
        self.description = "An Iron Sword. Still not great for combat, but could be useful for weaker enemies."
        self.damage_min = 5
        self.damage_max = 10
        self.damage = get_random_attribute(damage_min, damage_max)
        self.weight = 4
        self.forge_type = "Iron"

# Subclass for an Steel Sword
class SteelSword(Sword):
    def __init__(self, type, name, description, damage_min, damage_max, damage, weight, forge_type):
        super().__init__(type, name, description, damage_min, damage_max, damage, weight, forge_type)
        self.name = "Steel"
        self.description = "A Steel Sword. This is a strong weapon, likely to do heavy damage to opponents."
        self.damage_min = 9
        self.damage_max = 14
        self.damage = get_random_attribute(damage_min, damage_max)
        self.weight = 8
        self.forge_type = "Steel"



# class Paper_objects:
class PaperObject(Item):
    def __init__(self):
        self.item_type = "Paper Object"
        self.content = None

    # def look_at_paper_object(self):
    #     read = input(f"Would you like to read the {self.name}\n1. yes\n2. no")

    #     if read == "1":
    #         print("---------------------------------------------------------")
    #         print(f"{self.content}")
    #         print("---------------------------------------------------------")
    #     else: 
    #         pass




class DwarvianBookPage(PaperObject):
    def __init__(self):
        super().__init__()
        self.name = "Parchment"
        self.description = "You see a piece of parchment on the ground...\n"
        self.item_description = "It appears to be ripped in half, but the other half doesn't seem to be in the room. The page is filled from top to bottom, so it looks like it may be out of a book.\n"
        self.content = '''\nThe Dwarvian race are exceptionally vulnerable to magic.\n 
        To entrap larger Dwarves, it is common practice to use Illusionary Lodes lure Dwarves into traps with fake gems.\n
        To create committed slaves amongst the Dwarvian race, it has long been known to use a Forced Oath enchantment to secure a Dwarves loyalty.\n
        This causes an absolute breakdown of any autonomy, forcing them to be completely subserviant to their masters. 
        '''











    

