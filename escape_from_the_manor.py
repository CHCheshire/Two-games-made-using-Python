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
    player_sleeps = input("Please press 1 to continue\n")
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
        print("The zombie falls to the ground, lifeless.\n"
              "You take a few moments to collect yourself\n"
              "Unsure if that really just happened.")
        time.sleep(1)
        print("You hear more noises and screams down the hall\n"
              "You take a deep breath and swallow your fear\n"
              "and step into the corridor to start your escape.")
        corridor()
    if health == 0:
        player_died()


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
            if attack >= 1 and attack != 20:
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
    time.sleep(2)
    print("You glance to your left and, through the dining hall,\n"
          "see a door ajar to a study room with a purple glow\n"
          "shining through the cracks in the door.")
    time.sleep(1)
    foyer_choice = input("Will you either:\n"
                         "Press 1 to exit the manor now\n"
                         "Press 2 to investigate the study\n")
    if foyer_choice == '1':
        time.sleep(1)
        print("You run out the foyer leaving the manor\n"
              "and the screams and the horror behind you.")
        ending_one()
    elif foyer_choice == '2':
        time.sleep(1)
        print("You run through the dining hall and enter the study.\n"
              "You close the door behind, and turn to see\n"
              "what caused such a horribe night.")
        time.sleep(2)
        study()
    else:
        clear()
        print(f"{foyer_choice} is an invalid option")
        foyer()


def study():
    clear()
    print("The purple glow originates from a book on the desk\n"
          "of the study. It's bound in patchwork leather\n"
          "and it's pages are splattered with blood.")
    time.sleep(1)
    print("The purple energy is flowing out of the book\n"
          "You consider maybe trying to close or maybe burn the book\n"
          "But you also still have the chane to leave through\n"
          "Another door out of the study to the car park.")
    time.sleep(1)
    study_choice = input("Will you either:"
                         "Press 1 to try to close the book:\n"
                         "Press 2 to try and burn the book:\n"
                         "Press 3 to exit the study:\n")
    if study_choice == '1':
        time.sleep(1)
        print("You rush over to the desk and slam the book shut\n"
              "The purple energy coming from it cease you do so.")
        time.sleep(1)
        print("You hear the sounds of the zombies cease as well.\n"
              "Relief washes over you as you realise the danger\n"
              "has now passed and you have survived.")
        ending_two()
    if study_choice == '2':
        print("You grab a lit candle from the desk and press\n"
              "it to the pages of the book. The book lights\n"
              "on fire quickly.")
        time.sleep(1)
        print("As smoke rises from the book, it quickly fills\n"
              "the room. You soon hear pounding on the door\n"
              "as the zombies try to stop you destroying the book.\n"
              "You brace the door and try to stop them.")
        time.sleep(1)
        ending_three()
    if study_choice == '3':
        time.sleep(1)
        print("You decide to not mess with the book\n"
              "and instead decide to flee the study.")
        time.sleep(1)
        ending_one()


def ending_one():
    print("You flee the manor and jump into your car.\n"
          "You quickly start your car and look up to see\n"
          "zombies start spilling out of the manor, coming for you.\n"
          "Without a second thought, you pull out of the car park\n"
          "You drive as fast you can into the night, trying your\n"
          "to forget about those you left behind...")
    time.sleep(3)
    congratulations()


def ending_two():
    print("You start to feel the door break and give way.\n"
          "You brace as hard as you can against the door\n"
          "but you're unable to stop all of the monsters by\n"
          "yourself...")
    time.sleep(3)
    print("But then it all suddenly stops and goes quiet.\n"
          "You turn to see the book reduced to cinders and the"
          "the nightmare of tonight comes to a rest.")
    time.sleep(1)
    congratulations()


def ending_three():
    print("You look over at the book, it's dark\n"
          "magic now at rest. You think about\n"
          "the horrible things it did and how it almost\n"
          "got you killed and maybe even turned into one of those\n"
          "things...")
    time.sleep(3)
    print("You sit in the study, exhasuted from the\n"
          "ordeals of tonight and drift off to sleep.\n"
          "As you awake, you see the book sitting on the desk\n"
          "and just can't shake the urge to read it...")
    congratulations()


if __name__ == "__main__":
    game()