# Hangman

This is the game of Hangman. In this game, the player gets six chances to guess a secret word letter by letter. Each misguess brings the player closer to losing the game. Your goal is to guess the secret word before the Hangman is complete.

## Instructions

### Step 1: Preparation

1. Make sure you have **Python** installed on your computer.
2. Create a file called `words.txt` in the same folder as the program and add a list of words that the game will use. Each word should be on its own line for example:

internet  
python  
hangman  
coding

3. Add `words.text` to your `.gitignore` file to make sure its not tracked by Git, as you may not want to share your dictionary with others.

### Step 2: Run the game

1. Open your terminal or command prompt.
2. Navigate to the folder where your Python file is located.
3. Run the game with the following command:

`python <filename>.py`

Replace <filename> with the name of your Python file, example main.py.

### Step 3: Rules

1. When the game starts, you will be asked to enter your name.
2. You get six guesses for guessing the letters of a secret word. For each misguess a portion of the Hangman figure appears in the terminal.
3. To guess, type a letter and press Enter. If the letter is in the secret word, it appears in the correct place.
4. If you guess wrong, the number of misguesses increases and the Hangman figure gets closer to completeness.
5. The game continues until you have either guessed the entire word correctly or the Hangman figure is complete (6 wrong guesses).
6. When the game is over, you'll find out if you won or lost, as well as what the secret word was.

### Step 4: Edit the word-list

To change the dictionary that the game uses, open `words.txt` and add or remove words. Each word should be on its own line. Dont forget to save the file before running the game again.

## System requirements

- Python must be installed.

- A file called `words.txt` with a list of words that the game uses.
