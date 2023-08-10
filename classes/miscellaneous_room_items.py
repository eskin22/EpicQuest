# Create a class for random tables that are either empty or contain random artifacts
class Table:
    def __init__(self):
        self.artifacts = []
        self.description = None

    def show_table_description(self):
        print(f"\n{self.description}")
        
        if len(self.artifacts) == 0:
            print("There are no artifacts on the table.\n")

        else:
            for item in self.artifacts:
                print(f"\n{item}")
        



# Creating a subclass of table 
class Table_One(Table):
    def __init__(self):
        super().__init__()
        self.artifacts = ["Forged Chains: The Dwarven Uprising", "Bloody Knife", "Dwarvan Necklace"]
        self.description = "In front of you is a whithering wooden table. You investigate further and find: "



# Create a class for letters/notes/ripped out pages in books






