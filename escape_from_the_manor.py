import os
import random
import subprocess
import time


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def game():
    clear()
    print("You are driving out of town on a stormy night, it's getting late.\n"
          "You're driving down country roads, the darkness is illuminated by\n"
          "the headlights on your car and cracks of lightning.\n"
          "You find yourself getting tired, you need to stop soon to rest.\n"
          "After several more miles, you see a road leading off to a hotel\n"
          "seeing nowhere else to stay, you decide to rest here for tonight.")
    time.sleep(2)
    print("Seeing other cars parked up, you'd guess around 10 other people\n"
          "are staying here tonight as well, to wait out the storm.\n"
          "Check in is quickly sorted, you don't bring in many bags\n"
          "as you don't plan to stay here for long.\n"
          "Finding your room on the second floor, sleep comes quickly\n"
          "as you drift off to sound of heavy rain hitting the window")
    zombie()


def zombie():
    zombie_choice = input("Zombie attack door, choose to either\n"
                          "1 to hide:\n2 to fight:\n3 to jump out window:\n")
    if zombie_choice == '1':
        clear()
        print("Hide in closet")
        time.sleep(2)
        print("Door to room breaks in, zombie enters")
        time.sleep(2)
        print("Player is found and dies")
        player_died()
    elif zombie_choice == '2':
        clear()
        print("Player grabs pocket knife from bag and readies")
        time.sleep(2)
        print("Zombie breaks in and fight breaks out")
        fight()
    elif zombie_choice == '3':
        clear()
        print("Jump out second floor window")
        time.sleep(2)
        print("Breaks leg and passes out from pain")
        player_died()
    else:
        clear()
        print(f"{zombie_choice} is not valid. Choose a valid option.\n")
        zombie()


def player_died():
    print("Player has died")
    restart = input("Would you like to try again Y/N?").upper()
    if restart == "Y":
        clear()
        game()
    elif restart == "N":
        clear()
        print("Thank you for playing!")
        subprocess.call(["python", "main_menu.py"])
    else:
        clear()
        print(f"{restart} is an invalid option")
        player_died()


def fight():
    print("Player has knife ready to attack zombie")
    health = 5
    hits = 0
    min = 1
    max = 20
    while hits != 3 and health > 0:
        action = input("You can either:\n"
                       "Press 1 to attack with knife:\n"
                       "Press 2 to push zombie over:")
        if action == '1':
            attack = random.randint(min, max)
            print("Rolling to hit zombie")
            time.sleep(1)
            print(attack)
            if attack >= 8:
                print("Hits zombie")
                hits += 1
            elif attack == 20:
                print("Critical hit!")
                hits += 3
            else:
                print("Player misses and gets hit")
                health -= 1
        if action == '2':
            push = random.randint(min, max)
            print(push)
            if push >= 12:
                print("Zombie falls, plunge knife into head\n")
                hits = 3
            else:
                print("Player fails and gets hit")
                health -= 1
    if hits == 3:
        print("Zombie defeated")
        zombie_loot()
    else:
        player_died()


def zombie_loot():
    lighter = 0
    clear()
    print("Stand over corpse, do you want to loot it?")
    loot = input("Loot the corpse Y/N?").upper()
    if loot == "Y":
        print("You find a lighter")
        lighter = 1 
        corridor()
    elif loot == "N":
        print("Don't loot the corpse")
        corridor()
    else:
        print(f"{loot} is an invalid option")
        zombie_loot()


def corridor():
    print("Step out onto a corridor\n"
          "zombies attacking people left\n"
          "stairs to foyer and exit right.")
    corridor_choice = input("1 to try to save people, 2 to try to exit")
    if corridor_choice == '1':
        print("You distract the zombies so others can escape.\n"
              "You get overwhelmed and perish as they flee.")
        time.sleep(2)
        player_died()
    elif corridor_choice == '2':
        print("You grimace and flee, running down the stairs\n"
              "and try to exit through the foyer")
        time.sleep(2)
        foyer_battle()
    else:
        clear()
        print(f"{corridor_choice} is an invalid option")
        corridor()


def foyer_battle():
    clear()
    health = 5
    hits = 0
    min = 1
    max = 20
    print("As you round the corner to the stairs leading down to the foyer\n"
          "A crazed old man stands in the foyer, babbling nonsense\n"
          "He wields a knife and dressed in what look to be occult robes\n"
          "You start to cautiously make your way down the stairs\n")
    time.sleep(1)
    print("As you step off the stairs, he lunges towards you\n"
          "He swings his knife but you manage to avoid the blow\n"
          "Steadying yourself, you prepare to fight him")
    while hits != 3 and health != 0:
        action = input("You can either:\n"
                       "Press 1 to attack with knife:\n"
                       "Press 2 to tackle the man to the ground:\n")
        if action == '1':
            attack = random.randint(min, max)
            print("Rolling to hit cultist")
            time.sleep(1)
            print(attack)
            if attack >= 10:
                print("Hits cultist")
                hits += 1
            elif attack == 20:
                print("Critical hit!")
                hits += 3
            else:
                print("Player misses and gets hit")
                health -= 1
        if action == '2':
            push = random.randint(min, max)
            print(push)
            if push >= 15:
                print("Cultist is tackled to the ground and subdued\n")
                hits = 3
            else:
                print("Player fails and gets hit")
                health -= 1
        if hits == 3: 
            print("Cultist defeated")
            zombie_loot()
        else:
            player_died()


if __name__ == "__main__":
    game()