# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


import random 
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word): 
    word_complete = "_" * len(word)
    guessed = False 
    guessed_letters = []
    guessed_words = []
    tries = 6 
    print ("Let's play a game of Hangman")
    print (display_hangman(tries))
    print (word_complete)
    print ("\n")
    while not guessed and tries > 0: 
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already used that letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Well done", guess, "is a part of the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_complete)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_complete = "".join(word_as_list)
                if "_" not in word_complete:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():

        else:
            print("Not a valid guess.")