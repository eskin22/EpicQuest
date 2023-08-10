
# Create a parent class for Chest
class Chest:
    def __init__(self) :
        self.chest_items = {}
        self.chest_description = None

    # A method to print the description of the chest
    def show_chest_description(self):
        print(f"{self.chest_description}")
    
    # A method to open the Chest
    def open_chest(self):
        choose_to_open = input("\nWould you like to open the chest?\n1. Let's see what's inside!\n2. Let's keep searching the room.")
        if choose_to_open == "1":
            if self.chest_items == None:
                print("This chest is empty.")
        
            else: 
                for key, value in self.chest_items.items():
                    print(f"\n{key}: {value}")
        else:
            pass
        #This pass will eventually ask users to move to a new square
        

# Creating Chest Number One
class Chest_One(Chest):
    def __init__(self):
        super().__init__()
        self.chest_items = {"Coins": 5, "Small Dagger": 1, "Goddess Statue": 1, "Dragon Bones": 6}
        self.chest_description = "Before you is a small chest. It is lined with gold and appears to be unlocked."




    

    