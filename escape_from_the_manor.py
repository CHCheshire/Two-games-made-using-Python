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
    player_sleeps = input("Please press 1 to continue")
    if player_sleeps == '1':
        zombie()
    else:
        clear()
        print(f"{player_sleeps} is an invalid option\n")
        game()


def zombie():
    time.sleep(2)
    print("You're awoken in the night by screams outside your room\n"
          "And something trying to beat down the door your room.")
    zombie_choice = input("As your door starts to cave in\n"
                          "You must make a choice, will you:\n"
                          "1 to hide:\n2 to fight:\n3 to jump out window:\n")
    if zombie_choice == '1':
        clear()
        print("You hide in the closet, hoping to stay hidden")
        time.sleep(2)
        print("You hear the door give way and the monster enter the room")
        time.sleep(2)
        print("It shuffles over to the closet you're in, sniffing you out\n"
              "and finding you trapped and helpless...")
        time.sleep(2)
        player_died()
    elif zombie_choice == '2':
        clear()
        print("You grab a pocket knife out of your bag and get ready.")
        time.sleep(2)
        print("Door caves in a zombie like creature bursts into the room\n"
              "And tries to attack you")
        fight()
    elif zombie_choice == '3':
        clear()
        print("You jump out the window, the panic making you forget\n"
              "You're on the second floor of this manor.")
        time.sleep(2)
        print("You land awkwardly, breaking your leg as you hit the ground.\n"
              "You scream out in pain and try to crawl away.\n"
              "The last thing you see is an man dressed in occult robes\n"
              "Brandishing a knife as he walks towards you...")
        time.sleep(2)
        player_died()
    else:
        clear()
        print(f"{zombie_choice} is not valid. Choose a valid option.\n")
        zombie()


def player_died():
    print("You have died")
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
    print("")
    health = 5
    hits = 0
    min = 1
    max = 20
    while hits < 3 and health > 0:
        time.sleep(1)
        print("Zombie is attacking you")
        action = input("You can either:\n"
                       "Press 1 to attack with knife:\n"
                       "Press 2 to push zombie over:\n")
        if action == '1':
            attack = random.randint(min, max)
            print("Rolling to hit zombie")
            time.sleep(1)
            print(attack)
            if attack >= 8 and attack != 20:
                print("You hit the zombie")
                time.sleep(1)
                hits += 1
            elif attack == 20:
                print("Critical hit!")
                time.sleep(1)
                hits += 3
            else:
                print("You miss your attack and get hit back")
                time.sleep(1)
                health -= 1
        if action == '2':
            push = random.randint(min, max)
            print(push)
            if push >= 15:
                print("The zombie falls over, you easily plunge\n"
                      "the knife into its head.")
                time.sleep(1)
                hits += 3
            else:
                print("Player fails and gets hit")
                health -= 1
    if hits >= 3:
        clear()
        print("The zombie ")
        zombie_loot()
    if health == 0:
        player_died()


def zombie_loot():
    lighter = 0
    clear()
    print("You stand over the corpse, it's now seemingly defeated\n"
          "Do want you try to scrounge anything off the corpse\n"
          "Or is there not enough time to do so?")
    loot = input("Loot the corpse Y/N?\n").upper()
    if loot == "Y":
        print("You quickly rummage through their pockets\n"
              "finding only a lighter which you take with you.\n"
              "You step out into the hallway.")
        lighter = 1
        time.sleep(1)
        corridor()
    elif loot == "N":
        print("You decide not to loot the corpse\n"
              "And step out into the hallway.")
        time.sleep(1)
        corridor()
    else:
        print(f"{loot} is an invalid option")
        zombie_loot()


def corridor():
    print("You exit your room and step out on to the corridor\n"
          "You see more zombie like creatures attacking people\n"
          "Down the hall on your left\n"
          "And stairs leading to the foyer on your right.")
    time.sleep(1)
    corridor_choice = input("Press 1 to try and help the people:\n"
                            "Press 2 to try and escape via the foyer:\n")
    if corridor_choice == '1':
        print("You distract the zombies so others can escape.\n"
              "You get overwhelmed and perish as they flee.")
        time.sleep(1)
        player_died()
    elif corridor_choice == '2':
        print("You grimace and flee, running down the stairs\n"
              "and try to exit through the foyer")
        time.sleep(1)
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
          "You start to cautiously make your way down the stairs")
    time.sleep(1)
    print("As you step off the stairs, he lunges towards you\n"
          "He swings his knife but you manage to avoid the blow\n"
          "Steadying yourself, you prepare to fight him")
    while hits <= 3 and health != 0:
        time.sleep(1)
        print("The cultist stands in your way")
        action = input("You can either:\n"
                       "Press 1 to attack with knife:\n"
                       "Press 2 to tackle him to the ground:\n")
        if action == '1':
            attack = random.randint(min, max)
            print("Rolling to hit cultist")
            time.sleep(1)
            print(attack)
            if attack >= 10 and attack != 20:
                print("You hit the cultist")
                time.sleep(1)
                hits += 1
            elif attack == 20:
                print("Critical hit!")
                time.sleep(1)
                hits += 3
            else:
                print("You miss and get hit")
                time.sleep(1)
                health -= 1
        if action == '2':
            push = random.randint(min, max)
            print(push)
            if push >= 15:
                print("Rolling to tackle cultist")
                time.sleep(1)
                print("The cultist is tackled to the ground and\n"
                      "you stab him deeply in the abdomen")
                time.sleep(1)
                hits += 2
                time.sleep(1)
                print("He shouts out in pain and stabs you back\n"
                      "Your forced to get off him, clutching your side\n"
                      "as pain flares up your side.")
                health -= 2
                time.sleep(1)
            else:
                print("You fail and gets hit")
                time.sleep(1)
                health -= 1
        if hits >= 3: 
            print("The cultist falls to the ground dead.")
            time.sleep(1)
            foyer()
        if health == 0:
            player_died()

def foyer():
    clear()
    print("With the cultist defeated, you can now exit the manor\n"
          "but the zombies haven't stopped. Someone or\n"
          "something else seems to be causing this. You hear screams\n"
          "from upstairs as people are still being attacked")
    time.sleep(1)
    print


if __name__ == "__main__":
    game()