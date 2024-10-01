import random
import time
import os

def load_words():
    with open('words.txt', 'r') as f:
        return [line.strip() for line in f]
    
words_list = load_words()

print("\nWelcome to the game of Hangman.")
player_name = input("Enter your name: ")
print("Hello " + player_name + "! Best of luck guessing the secret word!")
time.sleep(2)
print("Get ready! The game is about to begin. You will get 6 guesses to guess the correct word. \n Let's play Hangman!")
time.sleep(4)

hangman_stages = {0: ("   _____ ",
                       "  |     |",
                       "  |     |",
                       "  |      ",
                       "  |      ",
                       "  |      ",
                       "  |      ",
                       "__|__    "),
                   1: ("   _____ ",
                       "  |     |",
                       "  |     |",
                       "  |     O",
                       "  |      ",
                       "  |      ",
                       "  |      ",
                       "__|__    "),
                   2: ("   _____ ",
                       "  |     |",
                       "  |     |",
                       "  |     O",
                       "  |     |",
                       "  |      ",
                       "  |      ",
                       "__|__    "),
                   3: ("   _____ ",
                       "  |     |",
                       "  |     |",
                       "  |     O",
                       "  |    /|",
                       "  |      ",
                       "  |      ",
                       "__|__    "),
                   4: ("   _____ ",
                       "  |     |",
                       "  |     |",
                       "  |     O",
                       "  |    /|\\",
                       "  |      ",
                       "  |      ",
                       "__|__    "),
                   5: ("   _____ ",
                       "  |     |",
                       "  |     |",
                       "  |     O",
                       "  |    /|\\",
                       "  |    / ",
                       "  |      ",
                       "__|__    "),
                   6: ("   _____ ",
                       "  |     |",
                       "  |     |",
                       "  |     O",
                       "  |    /|\\",
                       "  |    / \\",
                       "  |      ",
                       "__|__    ")}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_hangman(incorrect_guesses):
    print(f"\nIncorrect guesses = {incorrect_guesses}")
    print("\n**************")
    for row in hangman_stages[incorrect_guesses]:
        print(row)
    print("\n**************")

def available_chars(chars):
    print(" ".join(chars))

def display_solution(solution):
    print(" ".join(solution))

def main():
     secret_word = random.choice(words_list)
     hint = ["_"] * len(secret_word)
     incorrect_guesses = 0
     guessed_chars = set()
     is_running = True

     while is_running:
         clear_screen()
         display_hangman(incorrect_guesses)
         available_chars(hint)
         guess = input("\nEnter a letter to solve the unknown word: ").lower()

         if len(guess) != 1 or not guess.isalpha():
             print("Invalid input")
             time.sleep(2)
             continue
         
         if guess in guessed_chars:
             print(f"The letter '{guess}' is already guessed")
             time.sleep(2)
             continue
         
         guessed_chars.add(guess)

         if guess in secret_word:
             for index in range(len(secret_word)):
                 if secret_word[index] == guess: 
                     hint[index] = guess
         else: 
             incorrect_guesses += 1

         if "_" not in hint:
            display_hangman(incorrect_guesses)
            display_solution(secret_word)
            print("\nGood job! You guessed the correct word!")
            print(f"The secret word was indeed '{secret_word}'")
            time.sleep(4)
            is_running = False
            
         elif incorrect_guesses >= len(hangman_stages) - 1:
            display_hangman(incorrect_guesses)
            display_solution(secret_word)
            print("\nSorry you ran out of guesses.")
            print(f"The secret word was '{secret_word}'. Better luck next time!")
            time.sleep(5)
            is_running = False 


if __name__ == "__main__":
    main()