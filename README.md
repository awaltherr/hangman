# Hangman

## Table of Contents

- [Overview](#overview)
- [Instructions](#instructions)
- [System Requirements](#system-requirements)
- [Gameplay](#gameplay)
- [Editing the Word List](#editing-the-word-list)

## Overview

Hangman is a classic guessing game where players attempt to find a hidden word by
suggesting letters. For each incorrect guess, a portion of a Hangman figure appears. The game ends when either the word is guessed or the Hangman figure is complete.

## Instructions

### Step 1: Preparation

1. Ensure **Python** is installed on your computer.
2. Create a file named `words.txt` in the same directory as the game script.
3. Add a list of words to `words.txt`, one word per line. For example:

```
internet
python
hangman
coding
```

4. Add `words.txt` to your `.gitignore` file to prevent sharing your dictionary.

### Step 2: Run the game

1. Open your terminal or command prompt.
2. Navigate to the directory containing your Python script.
3. Run the game using:

```
python <filename>.py
```

Replace `filename` with the name of your Python file (e.g., main.py).

## System requirements

- Python installed on your computer.
- A file named `words.txt` with a list of words for the game to use.

## Gameplay

1. When the game starts, you will be prompted to enter your name.
2. You get six guesses to identify the secret word letter by letter.
3. For each incorrect guess, a portion of the Hangman figure appears in the terminal
4. To guess, type a letter and press Enter.
5. If the letter is in the secret word, it appears in the right position.
6. If you guess incorrectly, the number of misguesses increases, and the Hangman figure gets closer to completion.
7. Throughout the game, you can view your incorrect guesses, helping you track your progress.
8. The game continues until you've either guessed the entire word correctly or the Hangman figure is complete (six incorrect guesses).
9. When the game ends, you'll find out if you have won or lost the game, along with what the secret word was.

## Editing the Word List

To modify the dictionary used by the game:

1. Open `words.txt` in a text editor.
2. Add or remove words as desired, keeping each on its own line.
3. Save the file before running it again.
