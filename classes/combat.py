# from enemies import Level_One_Dragon
# from enemies import Level_One_Witch
# from enemies import Level_One_Bear
# from enemies import Level_One_CultLeader
# from enemies import Level_One_Undead
# from enemies import Level_One_Warlord
# from player import Human
from colorama import init
init()
from colorama import Fore, Back, Style

class Combat_Engine:
    def __init__(self): 
        pass

    def perform_combat(self, player, enemy):
        player.display_info()
        enemy.display_enemy_info()

        while enemy.enemy_hp > 0 and player.hp > 0:
            if player.mana <= 0:
                print(Back.LIGHTYELLOW_EX  + Fore.WHITE + "\033[1mYou do not have the energy to attack the enemy.\033[0m")
                print("\n")
                player.mana += player.attack_power / 2  # Refresh player's mana
            else:
                total_attack_power = player.attack()
                new_hp = enemy.get_enemy_hp() - total_attack_power
                print(Fore.LIGHTRED_EX + f"\033[1mEnemy HP is now {new_hp}\033[0m")
                enemy.set_enemy_hp(new_hp)
                player.mana -= player.attack_power / 2

            if enemy.get_enemy_hp() <= 0:
                print(Fore.GREEN + "\033[1mENEMY DEFEATED!\033[0m")
                print("----------------------------------------------")
                print(Back.GREEN + Fore.WHITE + Style.BRIGHT + f"\033[1mCongrats!! Your HP is now {player.restore_hp + 1}\033[0m\n")
                break

            # Perform enemy's attack
            enemy.enemy_attack()
            player.hp -= enemy.enemy_attack_strength
            print(Fore.LIGHTYELLOW_EX + f"\033[1m{player.name} HP reduced to {player.hp}. Mana is {player.mana}\033[0m")

            if player.hp <= 0:
                print(Fore.RED + f"\033[1mYOU HAVE BEEN DEFEATED\033[0m")
                return
        else:
            print(Back.RED + Fore.WHITE + Style.BRIGHT +  "\033[1mEnemy wins!\033[0m")



    # def perform_combat(self, player, enemy):
    #     player.display_info()
    #     enemy.display_enemy_info()

    #     while enemy.enemy_hp > 0 and player.hp > 0:

    #         if player.mana <= 0:
    #               print("You have no energy to perform this attack.")
    #               player.mana += player.attack_power / 2  # Refresh player's mana

    #         total_attack_power = player.attack()
    #         new_hp = enemy.get_enemy_hp() - total_attack_power
    #         print(f"Enemy HP is now {new_hp}")
    #         enemy.set_enemy_hp(new_hp)
    #         player.mana -= player.attack_power / 2

    #         if enemy.get_enemy_hp() <= 0:
    #                     print("Enemy defeated!")
    #                     print("----------------------------------------------")
    #                     print(f"Congrats!! Your HP is now {player.restore_hp + 1}")
    #                     break
                
    #         else:
    #         # Perform enemy's attack
    #                     enemy.enemy_attack()
    #                     player.hp -= enemy.enemy_attack_strength

    #                     print(f"{player.name} HP reduced to {player.hp}. Mana is {player.mana}")

    #                     if player.hp<= 0:
    #                         print(f"{player.name} was defeated.")
    #                         return
    #     else: 
    #           print("Enemy wins!")


