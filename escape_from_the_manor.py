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
                          "1 to hide:\n2 to fight:\n3 to jump out window:")
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
        print("Player grabs pocketknife from bag and readies")
        time.sleep(2)
        print("Zombie breaks in and fight breaks out")
        zombie_fight()
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


def zombie_fight():
    print("Player has knife ready to attack zombie")
    health = 3
    hits = 0
    min = 1
    max = 20
    while hits != 3 and health != 0:
        action = input("You can either:\n"
                       "Press 1 to attack with knife:\n"
                       "Press 2 to push zombie over:")
        if action == '1':
            attack = random.randint(min, max)
            print(attack)
            if attack >= 8:
                print("Hits zombie")
                hits += 1
            else:
                print("Player misses and gets hit")
                health -= 1
        if action == '2':
            push = random.randint(min, max)
            print(push)
            if push >= 10:
                print("Zombie falls, plunge knife into head\n")
                hits = 3
            else:
                print("Player fails and gets hit")
                health -= 1


if __name__ == "__main__":
    game()