import random
import time
import os
class HangmanGame:
    def __init__(self):
        self.words_list = load_words()
        self.hangman_stages = { 
            0: ("   _____ ",
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
        
        self.secret_word = random.choice(self.words_list)
        self.hint = ["_"] * len(self.secret_word)
        self.incorrect_guesses = 0
        self.guessed_chars = set()
        self.incorrect_chars = set()

    def display_hangman(self):
        for row in self.hangman_stages[self.incorrect_guesses]:
            print(row)
        print("\n**************")

    def display_solution(self):
        print(" ".join(self.hint))

    def gameplay(self):
        print("\nWelcome to the game of Hangman.")
        player_name = input("Enter your name: ")
        print(f"Hello {player_name}! Best of luck guessing the secret word!")
        time.sleep(2)
        print("Get ready! The game is about to begin. You will get 6 guesses to guess the correct word. \n Let's play Hangman!")
        time.sleep(4)
    
        is_running = True

        while is_running:
            clear_screen()
            self.display_hangman()
            available_chars(self.hint)

            if self.incorrect_guesses:
                print(f"\nIncorrect guesses: {', '.join(sorted(self.incorrect_chars))}") 
            else:
                print("\nIncorrect characters: None")

            guess = input("\nEnter a letter to solve the unknown word: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input")
                time.sleep(2)
                continue
         
            if guess in self.guessed_chars:
                print(f"The letter '{guess}' is already guessed")
                time.sleep(2)
                continue
         
            self.guessed_chars.add(guess)

            if guess in self.secret_word:
                for index in range(len(self.secret_word)):
                    if self.secret_word[index] == guess: 
                        self.hint[index] = guess
            else: 
                self.incorrect_guesses += 1
                self.incorrect_chars.add(guess)

            if "_" not in self.hint:
                clear_screen()
                self.display_hangman()
                self.display_solution()
                print("\nGood job! You guessed the correct word!")
                print(f"The secret word was indeed '{self.secret_word}'")
                time.sleep(4)
                is_running = False
            
            elif self.incorrect_guesses >= len(self.hangman_stages) - 1:
                clear_screen()
                self.display_hangman()
                self.display_solution()
                print("\nSorry you ran out of guesses.")
                print(f"The secret word was '{self.secret_word}'. Better luck next time!")
                time.sleep(5)
                is_running = False 

def load_words():
    with open('words.txt', 'r') as f:
        return [line.strip() for line in f]
     
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def available_chars(chars):
    print(" ".join(chars))    

if __name__ == "__main__":
    game = HangmanGame()
    game.gameplay()