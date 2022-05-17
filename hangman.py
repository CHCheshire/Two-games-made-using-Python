import os
import random
import subprocess
from words.animals import animals_list
from words.countries import countries_list
from words.cities import cities_list


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def choose_word_list():
    """
    This will let the user decide which list they want to play with
    """
    clear()
    player_choice = input(
        "Please choose from one of the following options\n"
        "1 for animals:\n2 for cities:\n"
        "3 for countries:\n4 to exit:\n")
    if player_choice == '1':
        print("You've chosen the animals list")
        word = random.choice(animals_list)
        # return word.upper()
        play(word)
    elif player_choice == '2':
        print("You've chosen the cities list")
        word = random.choice(cities_list)
        # return word.upper()
        play(word)
    elif player_choice == '3':
        print("You've chosen the countries list")
        word = random.choice(countries_list)
        # return word.upper()
        play(word)
    elif player_choice == '4':
        print("Thank you for playing Hangman!")
        subprocess.call(["python", "main_menu.py"])
    else:
        clear()
        print(f"{player_choice} is not valid. Please pick from the list.\n")
        choose_word_list()


def play(word):
    """
    This is the function for playing the hangman game itself
    """
    word = word.upper()
    clear()
    word_complete = "_" * len(word)
    guessed = False
    guessed_ltrs = []
    guessed_words = []
    tries = 6
    print("Let's play a game of Hangman!")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            clear()
            if guess in guessed_ltrs:
                print("You have already used that letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_ltrs.append(guess)
            else:
                print("Well done", guess, "is a part of the word!")
                guessed_ltrs.append(guess)
                word_as_list = list(word_complete)
                indices = [i for i, ltr in enumerate(word) if ltr == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_complete = "".join(word_as_list)
                if "_" not in word_complete:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_complete = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_complete)
        print("\n")
    if guessed:
        print("Congratulations, you guessed the word!")
    else:
        print("Sorry, you're out of tries. The word was " + word + ".")
    play_again()


def display_hangman(tries):
    """
    This will give a display for the progression of hangman
    as the user gets incorrect answers
    """
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]


def play_again():
    """
    This function will allow the user to either play again or
    go back to the main menu
    """
    restart = input("Play Again (Y/N) ").upper()
    if restart == "Y":
        choose_word_list()
    elif restart == "N":
        clear()
        print("Thank you for playing Hangman")
        subprocess.call(["python", "main_menu.py"])
    else:
        clear()
        print(f"{restart} is an invalid option")
        play_again()


if __name__ == "__main__":
    choose_word_list()
