# Two games made in Python

This is a web page made to host two games; Hangman and a text adventure game, Escape from the Manor. I made this as I wanted to both make a hangman game that would allow people to choose different themes and potential difficulty within that (i.e. if know more about animals than city names then one is easier than the other). For the text adventure game, I wanted to make a choose your own adventure game with the mini game within that of fighting the monsters within the Manor as you try to escape.

## Features 

-__Main Menu__

    This part of the page is for a menu whereby the user can navigate back and forth between the two games. It uses subprocesses to do this and and lets the user exit the program fully as well if they want. 

-__Hangman game__

    The game of hangman plays as follows: The user will be asked to choose their theme of words that they will play with, either from animals, cities and countries. Once chosen, the computer will then randomly choose a word from that list. The player then gets to guess either the letters of the word or the word itself and every wrong guess will build the hangman. If the player gets the right word, they'll win but if they guess incorrectly six times, they will lose and the correct word will be shown to them. Regardless of the result, the player will be given the option to play again if they so wish. 

-__Hangman animals list__ 

    This is the list that the player can choose at the start of the hangman game that will make it so that all the words will be in the theme of animals.

-__Hangman cities list__ 

    This is the list that the player can choose at the start of the hangman game that will make it so that all the words will be in the theme of cities.

-__Hangman countries list__ 

    This is the list that the player can choose at the start of the hangman game that will make it so that all the words will be in the theme of countries.



## Testing 

    For the hangman game, some of the testing came from a few things: implementation of the different lists and how to choose them and also the game looping through properly and catching improper inputs from the user. So to start off with, I wanted to have different lists for hangman to make it a bit easier for the user; the themes and the choice effectively give a hint as to what the user will be needing to guess rather than having them all in one big list. It also gives the game a bit more variety and replayability as well. When initially trying to implement this however, I ran into a problem when the user gave an incorrect input. The function would go back to the start and give them the options again but would fail when they gave a correct input. This seemed to be due to the game generating a null value for the "word" variable which caused the game to crash. So to resolve this, I removed the return word.upper part when choosing the list and instead having that at the start of the game function. I also removed the code for having the player_choice variable be turned into an integer to catch invalid answers if the user typed in a word or letter. 

    Another error was caused by the play again section of the code. This was not restarting the game properly at first due to me having the input needing to be equal to an upper case "Y". If the user put in a lower case y the program would just stop all together which wasn't ideal. So to resolve this, I set it so that the input made by the user was returned as an uppercase letter and I also added in a catch for incorrect inputs as well. 

    This wasn't an error but a problem with the program was that the console log of the game would get very cluttered as you played due to all the text showing up as you played. It wasn't hard to play but it just looked messy, especially after playing several games and having a wall of text because of it. To combat this, I made a function to clear the log whenever it was called. This way I could easily clear the log when needed in order to keep the text in one place and easier for the user to read. Once made, I implemented this in several points in the code where it felt necessary to clear it, such as starting a new game, restarting it or when you picked a letter. 

    Finally for the hangman section, there was an error that was thrown due to one of my lines of code being over 80 characters long. This was somewhat unavoidable as it was the line for describing each of the lists that the player could choose from so I initially unsure how to fix this. This error wouldn't have caused any issues per se, it was more so just a warning the text would've ended up on a new line rather than it all being on the same line. However it was an error nonetheless and would've been reported when doing my checks at the end. So in order to resolve this issue, I had added in line breaks for where the input calls for each of the lists and as a byproduct this would also improve the look of the section when running the game. 
