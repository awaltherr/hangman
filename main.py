import random
import time
import os

words = ("apple", "banana", "cherry", "date", "elderflower", "laptop", "roundabout", "robot", "memory", "electronic", "submarine", "chess", "vortex", "matrix", "telephone", "titanic", "bridge", "tower", "global", "mouse", "universe", "pyramid", "error", "success", "language", "elevator", "internet", "parameter", "traffic", "filter", "picture", "country", "beautiful", "lobster", "mission", "poetry", "landmark", "certificate")

print("\nWelcome to the game of Hangman.")
name = input("Enter your name: ")
print("Hello " + name + "! Best of luck guessing the secret word!")
time.sleep(2)
print("Get ready! The game is about to begin. You will get 6 guesses to guess the correct word. \n Let's play Hangman!")
time.sleep(4)

hangman_drawing = {0: ("   _____ ",
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
    for row in hangman_drawing[incorrect_guesses]:
        print(row)
    print("\n**************")

def available_letters(letters):
    print(" ".join(letters))

def display_solution(solution):
    print(" ".join(solution))

def main():
     answer = random.choice(words)
     hint = ["_"] * len(answer)
     incorrect_guesses = 0
     guessed_letters = set()
     is_running = True

     while is_running:
         clear_screen()
         display_hangman(incorrect_guesses)
         available_letters(hint)
         guess = input("\nEnter a letter to solve the unknown word: ").lower()

         if len(guess) != 1 or not guess.isalpha():
             print("Invalid input")
             time.sleep(2)
             continue
         
         if guess in guessed_letters:
             print(f"The letter '{guess}' is already guessed")
             time.sleep(2)
             continue
         
         guessed_letters.add(guess)

         if guess in answer:
             for index in range(len(answer)):
                 if answer[index] == guess: 
                     hint[index] = guess
         else: 
             incorrect_guesses += 1

         if "_" not in hint:
            display_hangman(incorrect_guesses)
            display_solution(answer)
            print("\nGood job! You guessed the correct word!")
            print(f"The secret word was indeed '{answer}'")
            time.sleep(4)
            is_running = False
            
         elif incorrect_guesses >= len(hangman_drawing) - 1:
            display_hangman(incorrect_guesses)
            display_solution(answer)
            print("\nSorry you ran out of guesses.")
            print(f"The secret word was '{answer}'. Better luck next time!")
            time.sleep(5)
            is_running = False 


if __name__ == "__main__":
    main()