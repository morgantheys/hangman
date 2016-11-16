# Hangman
#
# Morgan Theys
# 10/19/2016

import os
import random

def show_start_screen():

    print(" __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __. ")
    print("|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  | ")
    print("|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  | ")
    print("|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  | ")
    print("|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   | ")
    print("|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__| ")

def show_end_screen():
    print("______            _ ")
    print("| ___ \          | |")
    print("| |_/ /_   _  ___| |")
    print("| ___ \ | | |/ _ \ |")
    print("| |_/ / |_| |  __/_|")
    print("\____/ \__, |\___(_)")
    print("        __/ |       ")
    print("       |___/        ")
    print("By Morgan Theys")
    print("10/19/2016")

def get_category(path):
    files = os.listdir(path)

    print("Choose a category...")
    
    for i, f in enumerate((files),1):
        full_path = path + "/" + f

        with open(full_path, 'r') as file:
            print(str(i) + ") " + file.readline().strip())

    choice = input("Enter selection: ")
    choice = int(choice)

    return path + "/" + files[choice-1]

def get_puzzle(file):
    with open(file, 'r') as f:
        words = f.read().splitlines()

    return random.choice(words[1:])

def check(word, solved, guesses):
    for i in range(len(word)):
        if word[i] in guesses or not word[i].isalpha():
            solved = solved[:i] + word[i] + solved[i+1:]

    return solved

def get_guess():
    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid. Enter just 1 letter.")

        
def display_board(solved, guesses, strikes):

    if strikes == 0:
        print("_________   ")
        print("|         | ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
    elif strikes == 1:
        print("_________   ")
        print("|     |     ")
        print("|     0     ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("|           ")
    elif strikes == 2:
        print("_________   ")
        print("|     |     ")
        print("|     0     ")
        print("|     |     ")
        print("|           ")
        print("|           ")
        print("|           ")
    elif strikes == 3:
        print("_________   ")
        print("|     |     ")
        print("|     0     ")
        print("|     |\    ")
        print("|           ")
        print("|           ")
        print("|           ")
    elif strikes == 4:
        print("_________   ")
        print("|     |     ")
        print("|     0     ")
        print("|    /|\    ")
        print("|           ")
        print("|           ")
        print("|           ")
    elif strikes == 5:
        print("_________   ")
        print("|     |     ")
        print("|     0     ")
        print("|    /|\    ")
        print("|      \    ")
        print("|           ")
        print("|           ")
    elif strikes == 6:
        print("_________   ")
        print("|     |     ")
        print("|     0     ")
        print("|    /|\    ")
        print("|    / \    ")
        print("|           ")
        print("|           ")
        
    print(solved + " [" + guesses + "]")
    
def play_again():
    while True:
        answer = input("Would you like to play again? ")

        if answer == 'no' or answer == 'n':
            return False
        elif answer == 'yes':
            return True

        print("What?!!! Just say yes or no.")

def play():
    puzzle_dir = 'puzzles'
    category_file = get_category(puzzle_dir)
    word = get_puzzle(category_file)
    solved = "-" * len(word)
    
    guesses = ""
    strikes = 0
    limit = 6
    
    solved = check(word, solved, guesses)
    display_board(solved, guesses, strikes)

    while word != solved and strikes < limit:
        letter = get_guess()

        if letter not in word:
            strikes += 1
            
        guesses += letter
        
        solved = check(word, solved, guesses)
        display_board(solved, guesses, strikes)

    if word == solved:
        print("You win!")
    else:
        print("You lose! The correct answer is " + str(word)+ ".")

def main():
    show_start_screen()

    playing = True

    while playing:
        play()
        playing = play_again()

    show_end_screen()

# code execution begins here
if __name__ == "__main__":
    main()

