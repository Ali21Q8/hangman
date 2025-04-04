# Hangman Game

## Description
A command-line implementation of the classic Hangman game. The player has to guess a word by suggesting letters within a limited number of attempts (5 lives). For each incorrect guess, part of the hangman is drawn. The game ends when the player either correctly guesses the word or runs out of lives.

## Installation
1. Clone this repository:
```bash
git clone https://github.com/Ali21Q8/hangman.git
cd hangman
```

2. Make sure you have Python installed (Python 3.6 or above recommended).

3. No additional dependencies are required as the game uses only Python's standard library.

## Usage
Run the game using the command:
```bash
python main.py
```

### How to Play
1. The game will select a random word from: 'becode', 'learning', 'mathematics', 'sessions'
2. You'll see blanks representing each letter in the word
3. Enter one letter at a time to guess
4. If your guess is correct, the letter will appear in its position(s)
5. If your guess is wrong, you'll lose one life and the hangman will be drawn step by step
6. The game ends when you either:
   - Guess the complete word (you win!)
   - Run out of lives (game over)

## Visuals
The game includes ASCII art to represent the hangman's stages:

```
   -----
   |   |
   O   |
  /|\  |  <- The hangman gradually appears with each wrong guess
  /    |
       |
```

## Project Structure
```
hangman/
├── draft/
│   └── draft.py     # File for draft code and notes
├── utils/
│   └── game.py      # Contains the Hangman class with game logic
└── main.py          # Main executable file
```

## Features
- Random word selection from a predefined list
- Visual ASCII representation of the hangman
- Input validation (single letters only)
- Prevents repeated guesses
- Game statistics tracking (turns played, errors made)
- Properly typed with Python type hints

## Timeline
- Start date: 03 April 2025
- End date: 04 April 2025

## Contributors
- Ali (Ali21Q8) - Initial implementation

## Personal Situation
This project was part of my learning journey in Python programming. Through building this Hangman game, I gained valuable experience in object-oriented programming concepts, input validation, and creating interactive command-line applications. I especially enjoyed implementing the ASCII art visualization as it enhances the gaming experience.
