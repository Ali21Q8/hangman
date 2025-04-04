from typing import List

class Hangman:
    """
    Hangman game class that handles the game logic.
    """
    
    def __init__(self) -> None:
        """
        Initialize the Hangman game with default values.
        """
        # List of possible words to guess
        self.possible_words: List[str] = ['becode', 'learning', 'mathematics', 'sessions']
        # Randomly select a word from possible_words
        import random
        self.word_to_find: List[str] = list(random.choice(self.possible_words))
        # Number of lives left
        self.lives: int = 5
        # Letters correctly guessed by the player
        self.correctly_guessed_letters: List[str] = ['_'] * len(self.word_to_find)
        # Letters wrongly guessed by the player
        self.wrongly_guessed_letters: List[str] = []
        # Number of turns played
        self.turn_count: int = 0
        # Number of errors made
        self.error_count: int = 0
    
    def play(self) -> None:
        """
        Ask the player to enter a letter and process the guess.
        """
        # Display current game state
        print(f"Current word: {' '.join(self.correctly_guessed_letters)}")
        
        # Ask for a letter
        while True:
            guess = input("Enter a letter: ").lower()
            # Validate input - must be a single letter
            if len(guess) == 1 and guess.isalpha():
                break
            print("Please enter a single letter.")
        
        # Increment turn count
        self.turn_count += 1
        
        # Check if the letter is in the word
        if guess in self.word_to_find:
            # Update correctly guessed letters
            for i, letter in enumerate(self.word_to_find):
                if letter == guess:
                    self.correctly_guessed_letters[i] = guess
            print(f"Good guess! '{guess}' is in the word.")
        else:
            # Update wrongly guessed letters and error count
            self.wrongly_guessed_letters.append(guess)
            self.error_count += 1
            self.lives -= 1
            print(f"Wrong guess! '{guess}' is not in the word. You lost a life!")
    
    def start_game(self) -> None:
        """
        Start the game and continue until it's over.
        """
        print("Welcome to Hangman!")
        print(f"You have {self.lives} lives to guess a word with {len(self.word_to_find)} letters.")
        
        # Continue playing until the game is over
        while self.lives > 0 and '_' in self.correctly_guessed_letters:
            self.play()
            # Display game status after each turn
            print(f"\nCorrectly guessed letters: {' '.join(self.correctly_guessed_letters)}")
            print(f"Wrongly guessed letters: {', '.join(self.wrongly_guessed_letters)}")
            print(f"Lives: {self.lives}")
            print(f"Errors: {self.error_count}")
            print(f"Turn count: {self.turn_count}")
            print("-" * 30)
        
        # Check if game is over or word is found
        if self.lives == 0:
            self.game_over()
        else:
            self.well_played()
    
    def game_over(self) -> None:
        """
        Display game over message when player runs out of lives.
        """
        print("Game over...")
        print(f"The word was: {''.join(self.word_to_find)}")
    
    def well_played(self) -> None:
        """
        Display congratulation message when player finds the word.
        """
        print(f"You found the word: {''.join(self.word_to_find)} in {self.turn_count} turns with {self.error_count} errors!")
