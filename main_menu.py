import subprocess
import os


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def main():
    clear()
    print("Welcome to my website for games I have made in Python\n"
          "I have made a game for hangman and a text adventure game\n"
          "I hope you enjoy the games please check feel free\n"
          "To check out my other work and Github.")
    option = input("Please choose from the list below for what to play\n"
                   "1 from Hangman\n2 for Escape from the manor\n3 to Exit\n")
    if option == '1':
        subprocess.call(["python", "hangman.py"])
    elif option == '2':
        subprocess.call(["python", "escape_from_the_manor.py"])
    elif option == '3':
        print("Thank you for playing!")
        quit()
    else:
        print(f"{option} is not valid. Please pick from the list.\n")
        main()


if __name__ == "__main__":
    main()
