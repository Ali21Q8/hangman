"""
Main file to execute the Hangman game.
"""

# Import the Hangman class from the game module
from utils.game import Hangman

def main():
    """
    Main function to start the Hangman game.
    """
    # Create a new Hangman game instance
    game = Hangman()
    
    # Start the game
    game.start_game()

if __name__ == "__main__":
    main()
