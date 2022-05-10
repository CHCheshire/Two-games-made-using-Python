import random
from animals import animals_list
from countries import countries_list
from cities import cities_list


def choose_word_list():
    player_choice = input("Please choose from one of the following options; 1 for animals, 2 for cities and 3 for countries: \n")
    player_choice = int(player_choice)
    if player_choice == 1:
        print("You've chosen the animals list")
        word = random.choice(animals_list)
        return word.upper()
    elif player_choice == 2:
        print("You've chosen the cities list")
        word = random.choice(cities_list)
        return word.upper()
    elif player_choice == 3:
        print("You've chosen the countries list")
        word = random.choice(countries_list)
        return word.upper()
    else:
        print("Please pick from the list")
        choose_word_list()


def play(word):
    word_complete = "_" * len(word)
    guessed = False
    guessed_ltrs = []
    guessed_words = []
    tries = 6
    print("Let's play a game of Hangman!")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
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


def display_hangman(tries):
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


def main():
    word = choose_word_list()
    play(word)
    while input("Play Again> (Y/N) ").upper == "Y":
        choose_word_list()
        play(word)


if __name__ == "__main__":
    main()

