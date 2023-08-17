

def print_dragon():
    with open('dragon.txt', 'r') as file:
        dragon = file.read()
        file.close()

    print(dragon)


def print_enemy_anscii(enemy):
    with open(f"{enemy.name.lower()}_anscii.txt", 'r') as art_file:
        enemy_picture = art_file.read()
        art_file.close()

    return enemy_picture


class Dragon():
    def __init__(self):
        self.name = "Dragon"

dragon = Dragon()
enemy_art = print_enemy_anscii(dragon)
print(enemy_art)